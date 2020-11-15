# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _

BASE_CHAR_INTELLECT = 25


class Realm(models.Model):
    _name = 'mummy.realm'

    name = fields.Char(string="Name")
    wow_id = fields.Integer(string="WoW Real ID")
    slug_name = fields.Char(string="Slug Name")
    href = fields.Char(string="Href")
