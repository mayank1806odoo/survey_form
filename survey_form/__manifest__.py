{
    'name': 'Survey Form',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Collect input from website users via a form',
    'description': 'Create records from website form submissions in Odoo 17',
    'author': 'Mayank Prajapati',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_form_views.xml',
        'views/menu.xml',
        'views/website_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
