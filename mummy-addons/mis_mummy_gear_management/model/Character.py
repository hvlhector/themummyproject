# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _

BASE_CHAR_INTELLECT = 25
BASE_CHAR_AGILITY = 25
BASE_CHAR_STRENGHT = 25
BASE_CHAR_VERSATILITY = 25
BASE_CHAR_HASTE = 25
BASE_CHAR_MASTERY = 25
BASE_CHAR_CRITICAL = 25
BASE_CHAR_STAMINA = 25


class Character(models.Model):
    _inherit = 'mummy.character'

    pj_intellect = fields.Integer(string="Intellect",readonly=True,compute='_get_gear_intellect')
    pj_agility = fields.Integer(string="Agility",readonly=True, compute='_get_gear_agility')
    pj_strenght = fields.Integer(string="Strenght",readonly=True, compute='_get_gear_strenght')
    pj_versatility = fields.Integer(string="Versatility",readonly=True, compute='_get_gear_versatility')
    pj_haste = fields.Integer(string="Haste",readonly=True, compute='_get_gear_haste')
    pj_mastery = fields.Integer(string="Mastery",readonly=True, compute='_get_gear_mastery')
    pj_critical = fields.Integer(string="Critical Strike",readonly=True, compute='_get_gear_critical')
    pj_stamina = fields.Integer(string="Stamina",readonly=True, compute='_get_gear_stamina')
    inventory_items_ids = fields.Many2many('mummy.item')
    gear_items_id = fields.Many2one('mummy.gear',string="Actual Gear")


    def _get_gear_intellect(self):
        self.pj_intellect = self.gear_items_id.total_intellect + (BASE_CHAR_INTELLECT * self.level)
        #TODO Averiguar cálculo de intelecto base de un pj en pelotas de X nivel.

    def _get_gear_agility(self):
        self.pj_agility = self.gear_items_id.total_agility + (BASE_CHAR_AGILITY * self.level)

    def _get_gear_strenght(self):
        self.pj_strenght = self.gear_items_id.total_strenght + (BASE_CHAR_STRENGHT * self.level)

    def _get_gear_versatility(self):
        self.pj_versatility = self.gear_items_id.total_versatility + (BASE_CHAR_VERSATILITY * self.level)

    def _get_gear_haste(self):
        self.pj_haste = self.gear_items_id.total_haste + (BASE_CHAR_HASTE * self.level)

    def _get_gear_mastery(self):
        self.pj_mastery = self.gear_items_id.total_mastery + (BASE_CHAR_MASTERY * self.level)

    def _get_gear_critical(self):
        self.pj_critical = self.gear_items_id.total_critical + (BASE_CHAR_CRITICAL * self.level)

    def _get_gear_stamina(self):
        self.pj_stamina = self.gear_items_id.total_stamina + (BASE_CHAR_STAMINA * self.level)

    #TODO Completar todos los _get_gear_<stat> del character
    #DONE Completado