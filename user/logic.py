from json import dumps
import random

import requests
# import urllib
from django.core.cache import cache

from transparent import config
from worker import call_by_worker


def get_verify_code(len=6):
    return random.randrange(10 ** (len - 1), 10 ** len)

@call_by_worker
def send_verify_code(phone):
    vcode = get_verify_code()
    key = 'VerifyCode-%s' % phone
    cache.set(key, vcode, 120)
    params = config.HY_SMS_PARAMS.copy()
    params['content'] = params['content'] % vcode
    params['mobile'] = phone
    return requests.post(config.HY_SMS_URL, data=dumps(params))

def check_verify_code(phone, vcode):
    key = 'VerifyCode-%s' % phone
    savedCode = cache.get(key)
    return savedCode == vcode

