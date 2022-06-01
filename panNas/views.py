import json
import logging

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .panNasApi import BaiDuPan


class ResObj:
    response = HttpResponse
    is_login = False
    result = {}


duPan = BaiDuPan()


def is_method_HttpResponse(request, method: str = "GET"):
    request.encoding = 'utf-8'
    status_code = 200
    result = {
        "code": 200,
        "msg": "请求成功！",
        "result": {}
    }
    res_obj = ResObj
    res_obj.response = HttpResponse(content_type='application/json', status=status_code)
    if request.method == method:
        res_obj.is_login = request.user.is_authenticated
    else:
        result['code'] = 400
        result['msg'] = '方法不存在！'
    res_obj.result = result
    return res_obj


def index_view(request):
    return redirect("/home/")


def home(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect("/login/")


def login_html(request):
    if request.user.is_authenticated:
        return redirect("/home/")
    else:
        return render(request, "login.html")


@csrf_exempt
def login_api(request):
    request.encoding = 'utf-8'
    status_code = 200
    result = {
        "code": 200,
        "msg": "请求成功！",
        "result": {}
    }
    try:
        request.POST = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        logging.warning("request.post和request.body为空")
    if request.method == "POST" and request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_date = {'username': username, 'password': password}
        user_obj = auth.authenticate(request, **user_date)
        if user_obj is not None:
            auth.login(request, user_obj)
            result['msg'] = "登录成功！"

        else:
            result['code'] = 401
            result['msg'] = "登录失败！账号或密码不存在！"
    else:
        result['code'] = 400
        result['msg'] = "请求的方法不存在！"
    return HttpResponse(json.dumps(result), content_type="application/json", status=status_code)


def logout_api(request):
    r = is_method_HttpResponse(request, method="POST")
    if r.is_login:  # 验证是否登录
        auth.logout(request)
        r.result['msg'] = "退出成功！"
        r.response.delete_cookie("csrftoken")
        r.response.delete_cookie("sessionid")
    r.response.content = json.dumps(r.result)
    return r.response


def is_login_api(request):
    r = is_method_HttpResponse(request, method="POST")
    try:
        request.POST = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        logging.warning("request.post和request.body为空")
    if r.is_login and request.POST:  # 验证是否登录
        r.result['result'] = duPan.is_login(request.POST.get("sign"), True)
    r.response.content = json.dumps(r.result)
    return r.response


def qrcode_sign_api(request):
    r = is_method_HttpResponse(request, method="POST")
    if r.is_login:
        dupan_res = duPan.getSign()
        r.result['result'] = {
            "sign": dupan_res.sign,
            "img_url": dupan_res.imgurl
        }
    r.response.content = json.dumps(r.result)
    return r.response


def qrcode(request):
    if request.method == "GET" and request.GET:
        return HttpResponse(duPan.getQrcode(request.GET.get("sign")), content_type="image/png;")
