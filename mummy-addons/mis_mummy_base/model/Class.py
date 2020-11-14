# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class Class(models.Model):
    _name = 'mummy.class'

    icon = fields.Binary(string="Class Icon")
    name = fields.Char(string="Name")