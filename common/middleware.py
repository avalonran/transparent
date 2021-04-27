from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from lib.http import render_json
from user.models import User
from common import error


class AuthorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, error.LOGIN_ERR)

class CorsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = HttpResponse()
            response['Content-length'] = '0'
            response['Access-Control-Allow-Headers'] = request.META['HTTP-ACCESS_CONTROL_REQUEST_HEADERS']
            response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8080'
            return response

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8080'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
