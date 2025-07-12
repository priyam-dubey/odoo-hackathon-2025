{
    'name': 'Skill Swap Platform',
    'version': '1.0',
    'summary': 'A platform to exchange skills with others.',
    'author': 'Priyambad Dubey',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/skill_views.xml',
        'views/swap_request_views.xml',
    ],
    'installable': True,
    'application': True,
}
