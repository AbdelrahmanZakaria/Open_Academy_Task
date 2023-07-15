{
    'name': "Open Academy",

    'summary': """For Trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
        """,
    'author': "Abdelrahman",
    'website': "http://www.my_company.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/partner.xml',
        'views/wizard_views.xml',
        'reports/open_academy_report.xml',
    ]
}
