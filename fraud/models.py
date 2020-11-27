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


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        if self.session.config.get('single_player'):
            return waiting_players[0]



class Group(BaseGroup):
    def after_voting(self):
        print('MY GROUP JUST CHECK', self.get_players())



class Player(BasePlayer):
    def role(self):
        if self.session.config.get('single_player'):
            return self.session.config.get('role')

