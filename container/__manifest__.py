# -*- coding: utf-8 -*-
{
    'name': "Container",
    'summary': """ Container """,
    'description': """
    """,

    'author': "Techversant",
    'website': "http://www.techversant.com.sa/",
    'category': '',
    'version': '0.1',

    'depends': ['base', 'sale',
                'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/container_view.xml',
    ],
    "installable": True,
    "application": True,

}