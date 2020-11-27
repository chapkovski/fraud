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
    num_rounds = 1
    num_players = 7
    num_candidates = 2
    num_voters = num_players - num_candidates
    vote_cost = 1
    fraud_cost = 1
    win_voter_payoff = 10
    win_candidate_payoff = 10
    parties = ['Red', 'Blue']


class SingleMixin:
    @property
    def single(self):
        return self.session.config.get('single_player')


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
            return waiting_players[0]


class Group(SingleMixin, BaseGroup):
    # TODO: these are actulaly  not needed, but for fast developemnt may work
    red_fraud = models.BooleanField()
    blue_fraud = models.BooleanField()
    red_revealing = models.BooleanField()
    blue_revealing = models.BooleanField()
    # TODO: again this is for single player mode only. Maybe there is more smart way of dealing with this,
    # have no time to think about it at the moment
    other_votes = JsonField()

    def get_fraud(self, party):
        if self.single:
            return getattr(self, f'{party}_fraud')

    def get_fraud_info(self, party):
        if self.single:
            return getattr(self, f'{party}_revealing')

    def after_fraud(self):
        print('AFTER FRAUD')

    def after_fraud_revealing(self):
        print('AFTER FRAUD REVEALING')

    def after_voting(self):
        self.other_votes = random.choices([False, True], k=Constants.num_voters - 1)


class Player(SingleMixin, BasePlayer):
    fraud = models.BooleanField()
    revealing = models.BooleanField()
    vote = models.BooleanField()
    party = models.StringField(choices=Constants.parties)

    def role(self):
        if self.single:
            return self.session.config.get('role')
