# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class Item(models.Model):
    _name = 'mummy.item'

    name = fields.Char(string="Name")
    item_wow_id = fields.Integer(string="Item WoW ID")
    intellect = fields.Integer(string="Intellect")
    agility = fields.Integer(string="Agility")
    strenght = fields.Integer(string="Strenght")
    versatility = fields.Integer(string="Versatility")
    haste = fields.Integer(string="Haste")
    mastery = fields.Integer(string="Mastery")
    critical = fields.Integer(string="Critical Strike")
    stamina = fields.Integer(string="Stamina")
