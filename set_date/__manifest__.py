# -*- coding: utf-8 -*-
{
    'name': "internal_transfer_date",

    'summary': """
        To get same date on Second Payment Voucher as was on First Payment Voucher """,

    'description': """
        To get same date on Second Payment Voucher as was on First Payment Voucher
    """,

    'author': "MarkERP",
    'website': "https://markinnovative.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
}
