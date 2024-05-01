# -*- coding: utf-8 -*-
{
    'name': "test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','phone_validation','website','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_access.xml',
        'views/views.xml',
        'views/q5saleorder.xml',
        'views/q6_product.xml',
        # 'wizard/q4purchasereport.xml',
        # 'wizard/wizardform.xml',

        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
