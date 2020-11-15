# Copyright 2015-29/10/20 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class GenericDataSync(models.Model):
    _name = 'mummy.generic.data.sync'


    def get_active_realms(self):
        api = WowApi.WowApi(self.env.user.wow_client_id, self.env.user.wow_client_secret)
        data = api.get_realm_index('eu', namespace='dynamic-eu', locale='es_ES')



