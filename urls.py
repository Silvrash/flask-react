from resources.test import TestResource

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

APP_URL = [
    {
        'func': TestResource.test,
        'url': 'test/func',
        'endpoint': 'test_func',
        'methods': [GET]
    }
]

API_URL = [
    {
        'resource': TestResource,
        'url': 'test',
        'endpoint': 'test'
    },
]
