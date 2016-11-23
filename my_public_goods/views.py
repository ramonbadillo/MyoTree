from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


class Contribute(Page):

    form_model = models.Player
    form_fields = ['contribution']

page_sequence = [
    Contribute,
    ResultsWaitPage,
    Results
]
