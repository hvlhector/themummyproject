from odoo import fields, models, api, _
import logging
from datetime import datetime, timedelta

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from requests.packages.urllib3.util.retry import Retry

from . import WowApi

logger = logging.getLogger('wowapi')
logger.addHandler(logging.NullHandler())


class ResUsers(models.Model):

    _inherit = 'res.users'

    wow_client_id = fields.Char(string="WoW Client ID")
    wow_client_secret = fields.Char(string="WoW Client Secret")
    wow_region = fields.Char(string="Region")
    wow_namespace = fields.Char(string="Namespace")


    def synchronize_pjs(self):
        api = WowApi.WowApi(self.wow_client_id, self.wow_client_secret)
        print(api._access_tokens)
        #result = api.get_account_profile_summary('eu','profile-eu',api._access_tokens[self.wow_region]['token'])
        #print(result)
        return True

    def synchronize_realms(self):
        api = WowApi.WowApi(self.wow_client_id, self.wow_client_secret)
        data = api.get_realm_index('eu', namespace='dynamic-eu', locale='es_ES')
        for realm_data in data['realms']:
            print(realm_data)
            if not self.env['mummy.realm'].search([('name','=',realm_data['name'])],limit=1):
                self.env['mummy.realm'].create({
                    'name':realm_data['name'].encode('utf-8'),
                    'wow_id':realm_data['id'],
                    'slug_name':realm_data['slug'].encode('utf-8'),
                    'href':realm_data['key']['href']
                })
        return True
