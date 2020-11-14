# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class Talent(models.Model):
    _name = 'mummy.talent'

    name = fields.Char(string="Name")
    icon = fields.Binary(string="Icon")
    wow_talent_id = fields.Integer(string="WoW Talent ID")

