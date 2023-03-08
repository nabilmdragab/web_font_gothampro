# -*- coding: utf-8 -*-
#################################################################################
# Author      : Reson for IT Solutions (<https://reson.ae/>)
# Copyright(c): 2020-Present reson.ae
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
# You should have received a copy of the License along with this program.
# If not, see <https://reson.ae/license/>
#################################################################################
{
    'name': 'Gotham Pro Font',
    'summary': 'Enable Gotham Pro Font',
    'description': 'This module adds Gotham Pro WebFont to Odoo',
    'category': 'Hidden',
    'version': '14.0.1.0.0',
    'author': 'Nabil Mohamed Ali Ragab',
    'company': 'Reson for IT Solutions',
    'maintainer': 'Reson for IT Solutions',
    'website': "https://www.reson.ae",
    'depends': [
        'web',
        'website',
        'portal'
    ],
    'data': [],
    'assets': {
        'web._assets_primary_variables': [
            '/web_font_gothampro/static/src/scss/stylesheet.scss'
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'Other proprietary',
    'images': ['static/description/banner.jpg'],
    'currency': 'USD',
    'price': 0,
    'support': 'nabil@reson.ae',

}
