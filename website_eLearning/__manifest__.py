{
    'name': 'Website & eLearning',
    'summary': """ this model is create a many2One field to show a e learing data in website side""",
    'description': """
        create many2One field and add new field in website
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['website_sale','website_slides','website'],
    'data': [
      'views/product_template_only_form_view_inherit.xml',
      'views/web_inherit_template_website_layout.xml'
    ],


    'installable': True,
    'application': True,
}
