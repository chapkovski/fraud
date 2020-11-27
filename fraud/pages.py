from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    group_by_arrival_time = 'true'


class Fraud(Page):
    pass


class AfterFraudWP(WaitPage):
    pass


class FraudRevealing(Page):
    pass


class AfterFraudRevealingWP(WaitPage):
    pass


class Voting(Page):
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'after_voting'


class Results(Page):
    pass


page_sequence = [
    Fraud,
    AfterFraudWP,
    FraudRevealing,
    AfterFraudRevealingWP,
    Voting,
    ResultsWaitPage,
    Results
]
