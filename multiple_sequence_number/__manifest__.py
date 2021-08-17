# -*- coding: utf-8 -*-
{
    'name': 'Multiple Sequence Number',
    'version': '14.0.1.0.0',
    'summary': """Multiple sequence number for sale order""",
    'description': 'Generate multiple sequence number for sale order based on order type',
    'category': 'Sales',
    'author': 'Techversant Infotech',
    'company': 'Techversant Infotech',
    'website': "https://www.techversantinfo.com",
    'depends': ['base', 'sale', 'sales_team'],
    'data': [
            'data/order_type_data.xml',
            'security/ir.model.access.csv',
            'views/sale_order_view_inherit.xml',
            ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
