{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Services',
    'sequence': -12,
    'summary': 'Manage patient\'s records',
    'description': "",
    'website': 'https://github.com/bugd0ne',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale_order.xml'
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
