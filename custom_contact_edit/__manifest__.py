
{
    'name': "Contact Quick Edit",
    'version': '17.0.1.0.0',
    'category': 'contacts',
    'summary': """Contact Quick Edit From Kanban.""",
    'description': """
        - We can edit the contact from Kanban view
        - We can also Archieve the contact from kanban
    """,
    'author': 'Test',
    'company': 'Test',
    'website': "www.test.com",
    'depends': ['contacts', "mail"],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_edit.xml',
],

    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False,
}
