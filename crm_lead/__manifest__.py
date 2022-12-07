{
    'name': 'Lead & Opportunity',
    'version': '1.0',
    'author': 'Odoo India',
    'summary': 'this model is create a boolean field and dispaly a filter in search view and add a lost ribbon on kanban view and form view',
    'description': """
         Task ID - 3017340 """,
    'depends': ['crm'],
    'data': [
        'data/crm_lead_data.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
