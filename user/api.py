from user.logic import send_verify_code, check_verify_code
from lib.http import render_json

# Create your views here.
from user.models import User
from common import error


def get_verify_code(request):
    '''手机注册'''
    phone = request.POST.get('phone')
    send_verify_code(phone)
    return render_json(None, 0)

def login(request):
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')
    if check_verify_code(phone, vcode):
        user, created = User.objects.get(phone=phone)
        request.session['uid'] = user.id
        return render_json(user.to_dict(), 0)
    else:
        return render_json(None, error.VCODE_ERR)

def get_profile(request):
    user = request.user
    return render_json(user.profile.to_dict())

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




def logout(request):
    '''登出'''
    pass


def upload_avatar(request):
    '''上传头像'''
    pass


def modify_user_info(request):
    '''修改用户信息'''
    pass
