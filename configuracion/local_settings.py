# -*- coding: utf-8 -*-

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR+'/dbsqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# dreams de pruebas
# STRIPE_API_KEY = "sk_test_eO9BBhNHESY0Nee47epHgyrO"
# STRIPE_API_KEY_PUBLIC = "pk_test_riylhLG0B07fx3qRKde6W8kr"
# STRIPE_ENDPOINT_SECRET = "whsec_IHfzKCp7h6A1SUt3avqc3XITGaZhAyOE"

URL_SERVER = "http://miip:8000"