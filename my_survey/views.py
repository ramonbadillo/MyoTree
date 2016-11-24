from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):

    form_model = models.Player
    form_fields = ['q_country',
                  'q_age',
                  'q_gender']


class StarWarsTest(Page):

    form_model = models.Player
    form_fields = ['sw_bat',
                  'sw_widget',
                  'sw_choices',
                  'sw_lake']

    def before_next_page(self):
        self.player.set_payoff()

page_sequence = [
    Demographics,
    StarWarsTest
]
