from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    # TODO: remember that for non-single-player version this should be only ran once otherwise there will
    # be no stable group composition
    group_by_arrival_time = 'true'

    after_all_players_arrive = 'after_round_starts'


class Fraud(Page):
    form_model = 'player'
    form_fields = ['fraud']

    def is_displayed(self):
        return self.player.role() == 'candidate' and self.subsession.fraud


class AfterFraudWP(WaitPage):
    after_all_players_arrive = 'after_fraud'


class FraudRevealing(Page):
    form_model = 'player'
    form_fields = ['revealing']

    def is_displayed(self):
        return self.player.role() == 'candidate' and self.subsession.info

    def vars_for_template(self):
        if self.player.party == 'Red':
            other_candidate_decision = self.group.blue_fraud
        else:
            other_candidate_decision = self.group.red_fraud
        return dict(other_candidate_decision=other_candidate_decision)


class AfterFraudRevealingWP(WaitPage):
    after_all_players_arrive = 'after_fraud_revealing'


class Voting(Page):
    form_model = 'player'
    form_fields = ['vote']

    def is_displayed(self):
        return self.player.role() == 'voter'


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'after_voting'


class Results(Page):
    def vars_for_template(self):
        return dict(
            num_reds='num_reds',
            num_blues='num_blues',
            winner='winner'
        )


page_sequence = [
    FirstWP,
    Fraud,
    AfterFraudWP,
    FraudRevealing,
    AfterFraudRevealingWP,
    Voting,
    ResultsWaitPage,
    Results
]
