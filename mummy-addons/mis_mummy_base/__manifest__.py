# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
   'name': 'MiS Base - The mummies project',
   'summary': '',
   'version': '12.0.1.0.0',
   'author': 'Mummies S.L.',
   'website': '',
   'category': 'Mummy - Tools',
   'license': 'AGPL-3',
   'contributors': [
       'Héctor',
   ],
   'maintainers': [
       'Héctor',
   ],
   'depends': [
       # Project Dependencies
       # Base Dependencies
       'base',
       'mis_mummy_wowapi',
   ],
   'demo': [],
   'data': [
       # Security
       # Data
       # Views
      'views/menu_views.xml',
      'views/character_views.xml',
      'views/class_views.xml',
   ],
   'qweb': [],
   'demo': [],
   'test': [],
   'installable': True,
   'auto_install': False,
   'application': False,
   'sequence': 10,
}
