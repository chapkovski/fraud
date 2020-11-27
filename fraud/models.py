from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from .fields import JsonField
import random

author = 'Philipp Chapkovski, Valeria Maggian'

doc = """
Experiment on Electoral fraud
"""


class Constants(BaseConstants):
    name_in_url = 'fraud'
    players_per_group = None
    num_rounds = 10
    num_players = 7
    num_candidates = 2
    num_voters = num_players - num_candidates
    vote_cost = 1
    fraud_cost = 15
    win_voter_payoff = 10
    win_candidate_payoff = 20
    parties = ['Red', 'Blue']
    revealing_stubs = {False: 'No information available',
                       True: 'Candidate from party {party} is planning to commit fraud'}


class SingleMixin:
    @property
    def single(self):
        return self.session.config.get('single_player')

    def single_role(self):
        return self.session.config.get('role')


class Subsession(SingleMixin, BaseSubsession):

    # TODO: villeicht move these properties to db fields.
    @property
    def fraud(self):
        return self.session.config.get('fraud')

    @property
    def info(self):
        return self.session.config.get('info')

    def group_by_arrival_time_method(self, waiting_players):
        if self.single:
            return [waiting_players[0]]


class Group(SingleMixin, BaseGroup):
    # TODO: these are actulaly  not needed, but for fast developemnt may work
    red_fraud = models.BooleanField()
    blue_fraud = models.BooleanField()
    red_revealing = models.BooleanField()
    blue_revealing = models.BooleanField()
    # TODO: again this is for single player mode only. Maybe there is more smart way of dealing with this,
    # have no time to think about it at the moment
    other_votes = JsonField()
    num_reds = models.IntegerField()
    num_blues = models.IntegerField()
    divider = models.IntegerField()
    winner = models.StringField()

    @property
    def player(self):
        if self.single:
            return self.get_players()[0]
        raise Exception('Cant find single player for multi-player setting')

    def after_round_starts(self):

        if self.single:
            for p in self.get_players():
                if p.role() == 'voter' or self.round_number == 1:
                    p.party = random.choice(Constants.parties)
                else:
                    p.party = p.in_round(1).party

    def get_fraud(self, party):
        if self.single:
            return getattr(self, f'{party}_fraud')

    def get_fraud_info(self, party):
        if self.single:
            return getattr(self, f'{party}_revealing')

    def get_red_decision(self):
        revealing = self.get_fraud_info('red')
        return Constants.revealing_stubs.get(revealing).format(party='BLUE')

    def get_blue_decision(self):
        revealing = self.get_fraud_info('blue')
        return Constants.revealing_stubs.get(revealing).format(party='RED')

    def after_fraud(self):
        if self.single:
            if self.player.role() == 'voter':
                self.red_fraud = random.choice([True, False])
                self.blue_fraud = random.choice([True, False])
            else:
                fraud_decision = self.player.fraud
                party = self.player.party
                setattr(self, f'{party.lower()}_fraud', fraud_decision)
                if party == 'Red':
                    self.blue_fraud = random.choice([True, False])
                else:
                    self.red_fraud = random.choice([True, False])

    def after_fraud_revealing(self):
        if self.single and self.single_role() == 'voter':
            self.red_revealing = random.choice([True, False])
            self.blue_revealing = random.choice([True, False])

    def after_voting(self):
        if self.single:
            p = self.player
            party = p.party
            if p.role() == 'voter':
                self.other_votes = random.choices([False, True], k=Constants.num_voters - 1)
                reds = self.other_votes[:2]
                blues = self.other_votes[2:]
            else:
                self.divider = random.randint(2, 3)
                self.other_votes = random.choices([False, True], k=Constants.num_voters)
                reds = self.other_votes[:self.divider]
                blues = self.other_votes[self.divider:]
            print('RED', reds, 'BLUE', blues)
            if p.role() == 'voter':
                vote = p.vote
                if party == 'Red':
                    reds.append(vote)
                else:
                    blues.append(vote)
            self.num_reds = sum(reds)
            self.num_blues = sum(blues)

            if self.subsession.fraud:
                if self.red_fraud:
                    self.num_reds += 1
                    self.num_blues = max([self.num_blues - 1, 0])
                if self.blue_fraud:
                    self.num_reds = max([self.num_reds - 1, 0])
                    self.num_blues += 1
            if self.num_blues > self.num_reds:
                self.winner = 'Blue'
            elif self.num_blues < self.num_reds:
                self.winner = 'Red'
            else:
                self.winner = random.choice(Constants.parties)

            if self.winner == p.party:
                if p.role() == 'voter':
                    p.payoff = Constants.win_voter_payoff - Constants.vote_cost * p.vote
                else:
                    p.payoff = Constants.win_candidate_payoff - Constants.fraud_cost * p.fraud
            else:
                if p.role() == 'voter':
                    p.payoff = - Constants.vote_cost * p.vote
                else:
                    p.payoff = - Constants.fraud_cost * p.fraud


class Player(SingleMixin, BasePlayer):
    party = models.StringField()
    fraud = models.BooleanField(label='Would you like to commit a fraud in this period?')
    revealing = models.BooleanField(label='Would you like to inform voters that an opposite party is planning a fraud?')
    vote = models.BooleanField(label='Would you like to vote for your party in this period?')
    party = models.StringField(choices=Constants.parties)

    def role(self):
        if self.single:
            return self.session.config.get('role')
