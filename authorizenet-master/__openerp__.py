{
    'name': 'Authorize.net',
    'version': '1.1',
    'author': 'Kyle Waid',
    'category': 'Sales Management',
    'depends': [ 'payment', 'account_voucher', 'account_cancel'],
    'website': 'samp',
    'description': """ 
    """,
    'data': ['views/authorize_config.xml',
	     'wizard/authorize_payment.xml',
         
	     'views/profiles.xml',
	     'views/partner.xml',
          'views/sale.xml',
          'views/payment_method.xml',
	     'views/account_voucher.xml',
	     'views/account_journal.xml',
         'views/payment_method.xml',
	     'data/journal.xml',
	     'data/profiles_seq.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['suds'],
    },
}
