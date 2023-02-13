# -*- coding: utf-8 -*-
#################################################################################
# Author      : ROOK FZ LLC (<https://rook.ae/>)
# Copyright(c): 2020-Present ROOK.ae
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
# You should have received a copy of the License along with this program.
# If not, see <https://rook.ae/license/>
#################################################################################
{
    'name': 'Gotham Pro Font',
    'summary': 'Enable Gotham Pro Font',
    'description': 'This module adds Gotham Pro WebFont to Odoo',
    'category': 'Hidden',
    'version': '14.0.1.0.0',
    'author': 'Nabil Mohamed Ali Ragab',
    'company': 'ROOK FZ LLC',
    'maintainer': 'ROOK FZ LLC',
    'website': "https://www.rook.ae",
    'depends': [
        'web',
        'website',
        'portal'
    ],
    'data': [
        'views/frontend_assets.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'Other proprietary',
    'images': ['static/description/banner.jpg'],
    'currency': 'USD',
    'price': 0,
    'support': 'nabil@rook.ae',

}
