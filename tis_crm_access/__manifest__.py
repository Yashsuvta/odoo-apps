{
    "name": "TIS CRM",
    "version": "17.0.1.0.0",
    "author": "Techinfini Solutions Pvt. Ltd.",
    "summary": "Module to manage user access rights for CRM and Contacts with three levels: Super Admin, Admin, Intern.",
    "description": """
        This module enables managing user access rights for CRM and Contacts.
        It provides three levels of access: Super Admin, Admin, and Intern.
    """,
    "website": "https://www.techinfini.in",
    "support": "yash.suvta@techifini.in",
    "depends": ['base', 'contacts', 'crm', 'sale_crm'],
    "data": [
        'views/res_user.xml',
        'data/security.xml',
        'views/menus.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,  
    'images': [],
    'price': 10.00,
    'currency': 'USD',
}
