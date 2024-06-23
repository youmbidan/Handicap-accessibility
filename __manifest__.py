# -*- coding: utf-8 -*-
{
    'name': "Handicap Access",

    'summary': """
        Module qui uen fois implémenté permettra à l'handicapé d'acceder facilement à n'importe qu'elle site web""",

    'description': """
     Propose une gamme de personnalisations pour site web qui s'adapte aux besoins spécifiques de l'utilisateur en situation de handicap
    """,

    'author': "YOUMBI CHATUE Danièle",
   # 'website': ",

    # Categories can be used to filter modules in modules listing
   
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'views/handicap_views.xml',
        'views/utilisateur_views.xml',
        'views/menu_views.xml',
        'views/homepage_template.xml',
        #'views/assets.xml',
        'security/ir.model.access.csv',
        #'security/security.xml',
        
        
     
       
        
        
        ],
    
     'assets': {
        'web.assets_backend': [
            '/handicap/static/src/css/handicap.scss',
            '/handicap/static/src/css/homepage.css',
            
            '/handicap/static/src/js/handicap_custom.js',
            
            
        ],
    },
    
    

   
    
   'qweb':[],
    
    'installable': True,
    'application': True,
}