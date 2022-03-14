# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project_work',
    'summary': """
        This module is project app the main task and sub-task and
        We want that in sub task the main task .
    """,
    'description': """
    Task id : 2763106
        We want that in sub task the main task.
     """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ['base', 'project'],
    'data': [
        'views/project_task_view.xml'
    ],
    'installable': True,
    'application': True,
}
