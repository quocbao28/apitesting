'''
:Author: Minh.Pham (MXStudios)
'''

import json
import os
import sys
import random
import string
from datetime import datetime
from common.constant import *


# os.path.dirname(sys.modules['__main__'].__file__)
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# def get_env():    
#     return "Staging"


def get_values(env):
    '''
    :return: All data in env setting file
    '''
    switcher = {
        "test": PROJECT_PATH+"/../settings/test.json",
        "staging": PROJECT_PATH+"/../settings/staging.json",
        "production": PROJECT_PATH+"/../settings/production.json",
    }

    with open(switcher.get(str(env), lambda: 'Invalid')) as outfile:
        _values = json.load(outfile)
        return _values

    return ""


def get_domain(env):
    '''
    :return: DOMAIN value which get from setting env json file
    '''
    return get_values(env)['DOMAIN']


def get_protocal(env):
    '''
    :return: PROTOCAL value which get from setting env json file
    '''
    return get_values(env)['PROTOCAL']


def getValueRespone(response, value, value1):
    return json.loads(response.content)[value][value1]


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def getCurrentTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_value_setting(env, value):
    '''
    :return: selected value which get from setting env json file
    '''
    return get_values(env)[value]