from os import environ

SESSION_CONFIGS = [
    dict(
        name='baseline_single_voter',
        display_name="Baseline (single player) - Voter",
        num_demo_participants=1,
        app_sequence=['fraud'],
        single_player=True,
        role='voter'
    ),
    dict(
        name='baseline_single_candidate',
        display_name="Baseline (single player) - Candidate",
        num_demo_participants=1,
        app_sequence=['fraud'],
        single_player=True,
        role='candidate'
    ),
    dict(
        name='fraud_single_voter',
        display_name="Fraud (single player) - Voter",
        num_demo_participants=1,
        app_sequence=['fraud'],
        single_player=True,
        role='voter',
        fraud=True,
        info=False
    ),
    dict(
        name='fraud_single_candidate',
        display_name="Fraud (single player) - Candidate",
        num_demo_participants=1,
        app_sequence=['fraud'],
        single_player=True,
        role='candidate',
        fraud=True,
        info=False
    ),
    dict(
        name='fraud_info_single_voter',
        display_name="Fraud+INFO (single player) - Voter",
        num_demo_participants=1,
        app_sequence=['fraud'],
        single_player=True,
        role='voter',
        fraud=True,
        info=True
    ),
    dict(
        name='fraud_info_single_candidate',
        display_name="Fraud+INFO (single player) - Candidate",
        num_demo_participants=1,
        app_sequence=['fraud'],
        single_player=True,
        role='candidate',
        fraud=True,
        info=True
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'x1_!yc!)iat*+1-r)b9!nt$&t_qu_qy)vjq!y0%v7zgf^(7dl&'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
