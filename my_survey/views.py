from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):

    form_model = models.Player
    form_fields = ['q_country',
                  'q_age',
                  'q_gender']

class Submarine(Page):
    pass

class FirstPage(Page):
    form_model = models.Player
    form_fields = ['offer_{}'.format(i) for i in range(1, 6)]

    def vars_for_template(self):
        return {'offer_numbers': range(1, 6)}

class StarWarsTest(Page):

    form_model = models.Player
    form_fields = ['sw_bat',
                   'sw_widget',
                   'sw_choices',
                   'sw_lake',
                   'sw_level',
                   'sw_level',
                   'sw_slider',
                   ]


    def before_next_page(self):
        self.player.set_payoff()

page_sequence = [
    Submarine,
    Demographics,
    FirstPage,
    StarWarsTest
]
