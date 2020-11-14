# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class Item(models.Model):
    _name = 'mummy.item'

    name = fields.Char(string="Name")
    item_wow_id = fields.Integer(string="Item WoW ID")
    #TODO add el resto de tipos
    #DONE. He cambiado Gloves por Hands, Pants por Legs, Boots por Feet, Ring por Finger, Main hand por One hand
    type = fields.Selection([('head', 'Head'), ('neck', 'Neck'), ('shoulder', 'Shoulder'), ('back', 'Back'), ('chest', 'Chest'), ('wrist', 'Wrist'), ('hands', 'Hands'), ('waist', 'Waist'), ('legs', 'Legs'), ('feet', 'Feet'), ('finger', 'Finger'), ('trinket', 'Trinket'), ('one_hand', 'One_hand'), ('off_hand', 'Off_hand')])
    intellect = fields.Integer(string="Intellect")
    agility = fields.Integer(string="Agility")
    strenght = fields.Integer(string="Strenght")
    versatility = fields.Integer(string="Versatility")
    haste = fields.Integer(string="Haste")
    mastery = fields.Integer(string="Mastery")
    critical = fields.Integer(string="Critical Strike")
    stamina = fields.Integer(string="Stamina")
