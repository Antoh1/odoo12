# -*- coding: utf-8 -*-
{
    'name': "rt_prescription",

    'summary': """
        This module aids in requiring the pharmacy attendant to capture prescription
        of a controlled drug before selling""",

    'description': """
        Prescription drugs control
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'rt_pharmacy'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/import.xml',
        'views/pos_config.xml',
        'views/pos_order_line.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}