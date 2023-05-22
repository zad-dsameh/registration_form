# -*- coding: utf-8 -*-
{
    'name': "Registration Form edit",

    'summary': """
    Registration Form edit
        """,

    'description': """
        We need to add a new fields on the registration form (Mobile and Phone)
        Fields should be required
        Fields allow only numbers
        Data should be saved on partner form related to the created user

    """,

    'author': "Dina Sameh",
    'website': "http://www.zadsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'auth_signup'],

    # always loaded
    'data': [
        'views/registration_form_view.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'registration_form/static/**/*',
        ],
    },
    "license": "LGPL-3",
}
