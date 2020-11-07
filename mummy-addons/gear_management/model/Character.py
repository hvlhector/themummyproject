# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class Character(models.Model):
    _name = 'mummy.character'

    name = fields.Char(string="Name")
    avatar = fields.Binary(string="Avatar")
    user_id = fields.Many2one('res.users', string="User")
    pj_intellect = fields.Integer(string="Intellect")
    pj_agility = fields.Integer(string="Agility")
    pj_strenght = fields.Integer(string="Strenght")
    pj_versatility = fields.Integer(string="Versatility")
    pj_haste = fields.Integer(string="Haste")
    pj_mastery = fields.Integer(string="Mastery")
    pj_critical = fields.Integer(string="Critical Strike")
    pj_stamina = fields.Integer(string="Stamina")
    clase_id = fields.Many2one('mummy.class',string="Class")
    spec_id = fields.Many2one('mummy.spec',string="Spec")
    talent_ids = fields.Many2many('mummy.talent',string="Talents")

