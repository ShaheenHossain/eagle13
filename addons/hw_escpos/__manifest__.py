# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

{
    'name': 'ESC/POS Hardware Driver',
    'category': 'Sales/Point Of Sale',
    'sequence': 6,
    'website': 'https://www.eagle.com/page/point-of-sale-hardware',
    'summary': 'Hardware Driver for ESC/POS Printers and Cashdrawers',
    'description': """
ESC/POS Hardware Driver
=======================

This module allows Eagle to print with ESC/POS compatible printers and
to open ESC/POS controlled cashdrawers in the point of sale and other modules
that would need such functionality.

""",
    'depends': ['hw_proxy'],
    'external_dependencies': {
        'python' : ['pyusb','pyserial','qrcode'],
    },
    'installable': False,
}
