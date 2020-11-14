# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _

class Gear(models.Model):
    _name = 'mummy.gear'

    #TODO completar restricciones de los campos (dominios)
    #DONE completado

    name = fields.Char(string="Gear Set Name")
    character_id = fields.Many2one('mummy.character',string="Character")
    head_id = fields.Many2one('mummy.item',string="Head",domain="[('type','=','head')]")
    neck_id = fields.Many2one('mummy.item',string="Neck",domain="[('type','=','neck')]")
    shoulder_id = fields.Many2one('mummy.item',string="Shoulder",domain="[('type','=','shoulder')]")
    back_id = fields.Many2one('mummy.item',string="Back",domain="[('type','=','back')]")
    chest_id = fields.Many2one('mummy.item',string="Chest",domain="[('type','=','chest')]")
    wrist_id = fields.Many2one('mummy.item',string="Wrist",domain="[('type','=','wrist')]")
    hands_id = fields.Many2one('mummy.item',string="Hands",domain="[('type','=','hands')]")
    waist_id = fields.Many2one('mummy.item',string="Waist",domain="[('type','=','waist')]")
    pants_id = fields.Many2one('mummy.item',string="Legs",domain="[('type','=','legs')]")
    boots_id = fields.Many2one('mummy.item',string="Feet",domain="[('type','=','feet')]")
    ## Creo que solo hay que definir un tipo de restriccion para ring y para trinket, confirmar luego.
    ring_1_id = fields.Many2one('mummy.item',string="Finger 1",domain="[('type','=','finger')]")
    ring_2_id = fields.Many2one('mummy.item',string="Finger 2",domain="[('type','=','finger')]")
    trinket_1_id = fields.Many2one('mummy.item',string="Trinket 1",domain="[('type','=','trinket')]")
    trinket_2_id = fields.Many2one('mummy.item',string="Trinket 2",domain="[('type','=','trinket')]")
    main_hand_id = fields.Many2one('mummy.item',string="One Hand",domain="[('type','=','one_hand')]")
    off_hand_id = fields.Many2one('mummy.item',string="Off Hand",domain="[('type','=','off_hand')]")

    #Total variables
    total_intellect = fields.Integer(string="Total Gear Intellect",readonly=True,compute='_get_gear_intellect')
    total_stamina = fields.Integer(string="Total Gear Stamina",readonly=True,compute='_get_gear_stamina')
    total_agility = fields.Integer(string="Total Gear Agility",readonly=True,compute='_get_gear_agility')
    total_strenght = fields.Integer(string="Total Gear Strenght",readonly=True,compute='_get_gear_strenght')
    total_critical = fields.Integer(string="Total Gear Critical",readonly=True,compute='_get_gear_critical')
    total_haste = fields.Integer(string="Total Gear Haste",readonly=True,compute='_get_gear_haste')
    total_versatility = fields.Integer(string="Total Gear Versatility",readonly=True,compute='_get_gear_versatility')
    total_mastery = fields.Integer(string="Total Gear Mastery",readonly=True,compute='_get_gear_mastery')


    ##TODO completar resto de atributos.
    ##DONE completado resto de atributos.

    def _get_gear_intellect(self):
        self.total_intellect = self.head_id.intellect + self.shoulder_id.intellect + self.back_id.intellect + self.chest_id.intellect + self.wrist_id.intellect + self.hands_id.intellect + self.waist_id.intellect + self.legs_id.intellect + self.feet_id.intellect + self.finger_1_id.intellect + self.finger_2_id.intellect + self.trinket_1_id.intellect + self.trinket_2_id.intellect + self.one_hand_id.intellect + self.off_hand_id.intellect

    def _get_gear_stamina(self):
        self.total_stamina = self.head_id.stamina + self.shoulder_id.stamina + self.back_id.stamina + self.chest_id.stamina + self.wrist_id.stamina + self.hands_id.stamina + self.waist_id.stamina + self.legs_id.stamina + self.feet_id.stamina + self.finger_1_id.stamina + self.finger_2_id.stamina + self.trinket_1_id.stamina + self.trinket_2_id.stamina + self.one_hand_id.stamina + self.off_hand_id.stamina

    def _get_gear_agility(self):
        self.total_agility = self.head_id.agility + self.shoulder_id.agility + self.back_id.agility + self.chest_id.agility + self.wrist_id.agility + self.hands_id.agility + self.waist_id.agility + self.legs_id.agility + self.feet_id.agility + self.finger_1_id.agility + self.finger_2_id.agility + self.trinket_1_id.agility + self.trinket_2_id.agility + self.one_hand_id.agility + self.off_hand_id.agility

    def _get_gear_strenght(self):
        self.total_strenght = self.head_id.strenght + self.shoulder_id.strenght + self.back_id.strenght + self.chest_id.strenght + self.wrist_id.strenght + self.hands_id.strenght + self.waist_id.strenght + self.legs_id.strenght + self.feet_id.strenght + self.finger_1_id.strenght + self.finger_2_id.strenght + self.trinket_1_id.strenght + self.trinket_2_id.strenght + self.one_hand_id.strenght + self.off_hand_id.strenght

    def _get_gear_critical(self):
        self.total_critical = self.head_id.critical + self.shoulder_id.critical + self.back_id.critical + self.chest_id.critical + self.wrist_id.critical + self.hands_id.critical + self.waist_id.critical + self.legs_id.critical + self.feet_id.critical + self.finger_1_id.critical + self.finger_2_id.critical + self.trinket_1_id.critical + self.trinket_2_id.critical + self.one_hand_id.critical + self.off_hand_id.critical

    def _get_gear_haste(self):
        self.total_haste = self.head_id.haste + self.shoulder_id.haste + self.back_id.haste + self.chest_id.haste + self.wrist_id.haste + self.hands_id.haste + self.waist_id.haste + self.legs_id.haste + self.feet_id.haste + self.finger_1_id.haste + self.finger_2_id.haste + self.trinket_1_id.haste + self.trinket_2_id.haste + self.one_hand_id.haste + self.off_hand_id.haste

    def _get_gear_versatility(self):
        self.total_versatility = self.head_id.versatility + self.shoulder_id.versatility + self.back_id.versatility + self.chest_id.versatility + self.wrist_id.versatility + self.hands_id.versatility + self.waist_id.versatility + self.legs_id.versatility + self.feet_id.versatility + self.finger_1_id.versatility + self.finger_2_id.versatility + self.trinket_1_id.versatility + self.trinket_2_id.versatility + self.one_hand_id.versatility + self.off_hand_id.versatility

    def _get_gear_mastery(self):
        self.total_mastery = self.head_id.mastery + self.shoulder_id.mastery + self.back_id.mastery + self.chest_id.mastery + self.wrist_id.mastery + self.hands_id.mastery + self.waist_id.mastery + self.legs_id.mastery + self.feet_id.mastery + self.finger_1_id.mastery + self.finger_2_id.mastery + self.trinket_1_id.mastery + self.trinket_2_id.mastery + self.one_hand_id.mastery + self.off_hand_id.mastery
