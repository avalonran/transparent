from json import dumps
import random

import requests
# import urllib

from transparent import config
from worker import call_by_worker


def get_verify_code(len=6):
    return random.randrange(10 ** (len - 1), 10 ** len)

@call_by_worker
def send_verify_code(phone):
    vcode = get_verify_code()
    params = config.HY_SMS_PARAMS.copy()
    params['content'] = params['content'] % vcode
    params['mobile'] = phone
    return requests.post(config.HY_SMS_URL, data=dumps(params))

