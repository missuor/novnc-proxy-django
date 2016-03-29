# coding=utf-8
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import loader, Context
from django.core.exceptions import ValidationError

from .models import Server

def vnc_proxy(request):
    """VNC远程控制代理"""

    token = request.GET.get('token')
    try:
        obj = Server.objects.get(pk=token)

    except Server.DoesNotExist:
        raise ValidationError(u'错误的标识符', code=404)

    except Exception, e:
        raise ValidationError(str(e), code=500)

    host = settings.VNC_PROXY_HOST
    port = settings.VNC_PROXY_PORT
    # password = obj.vnc_password

    return JsonResponse({
        'token': token,
        'host': host,
        'port': port,
        # 'password': password,
        'password': 'os9527'
    })

def vnc_proxy_http(request):
    """VNC远程控制代理"""

    token = request.GET.get('token')
    try:
        obj = Server.objects.get(token=token)

    except Server.DoesNotExist:
        return HttpResponse('Token missing or incorrect.', status=404)

    except Exception, e:
        return HttpResponse(str(e), status=500)

    host = settings.VNC_PROXY_HOST
    port = settings.VNC_PROXY_PORT
    # password = obj.vnc_password

    template = loader.get_template('novnc/vnc_auto.html')
    context = Context({
        'token': token,
        'host': host,
        'port': port,
        # 'password': password,
        'password': 'os9527'
    })
    return HttpResponse(template.render(context))
