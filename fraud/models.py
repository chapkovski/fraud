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

author = 'Your name here'

doc = """
Your app description
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


class Subsession(BaseSubsession):
    @property
    def single(self):
        return self.session.config.get('single_player')

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


class Group(BaseGroup):
    def after_fraud(self):
        print('AFTER FRAUD')

    def after_fraud_revealing(self):
        print('AFTER FRAUD REVEALING')

    def after_voting(self):
        print('AFTER VOTING')


class Player(BasePlayer):
    def role(self):
        if self.subsession.single:
            return self.session.config.get('role')
