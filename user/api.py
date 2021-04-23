from json import dumps

from django.http import HttpResponse
from django.shortcuts import render

from logic import send_verify_code


# Create your views here.

def render_json(data, code=None):
    json_data = dumps({
        'code': code,
        'data': data
    })
    return HttpResponse(json_data)


def phone_register(request):
    phone = request.GET['phone']
    send_verify_code(phone)


def register(request):
    '''注册'''
    data = {
        'aa': 'bb',
        'cc': 'bb',
    }
    from user.models import User

    user = User.objects.create(
        nickname='neo',
        phone='1232134123',
        sex='F',
        birth_time='1990-3-17 12:00:00'
    )

    return render_json(data, 1111)


def login(request):
    '''登录'''
    pass


def logout(request):
    '''登出'''
    pass


def upload_avatar(request):
    '''上传头像'''
    pass


def modify_user_info(request):
    '''修改用户信息'''
    pass
