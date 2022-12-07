{
    'name':'salary slip',
    'version':'15.0',
    'depends':['hr_payroll','l10n_in_hr_payroll'],
    'data':[
        'data/hr_employee_form_data.xml',
        'views/hr_employee_view.xml',
        'report/payslip_template_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}