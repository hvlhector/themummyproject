# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _

BASE_CHAR_INTELLECT = 25


class Character(models.Model):
    _name = 'mummy.character'

    name = fields.Char(string="Name")
    level = fields.Integer(string="Level")
    avatar = fields.Binary(string="Avatar")
    user_id = fields.Many2one('res.users', string="User")
    clase_id = fields.Many2one('mummy.class',string="Class")
    spec_id = fields.Many2one('mummy.spec',string="Spec")
    talent_ids = fields.Many2many('mummy.talent',string="Talents")
