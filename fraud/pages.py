from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    group_by_arrival_time = 'true'


class Fraud(Page):
    def is_displayed(self):
        return self.player.role() == 'candidate' and self.subsession.fraud


class AfterFraudWP(WaitPage):
    after_all_players_arrive = 'after_fraud'


class FraudRevealing(Page):

    def is_displayed(self):
        return self.player.role() == 'candidate' and self.subsession.info


class AfterFraudRevealingWP(WaitPage):
    after_all_players_arrive = 'after_fraud_revealing'


class Voting(Page):
    def is_displayed(self):
        return self.player.role() == 'voter'


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
