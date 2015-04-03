# -*- coding: utf-8 -*-
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lizi.models import user
from lizi.common import Utils

# Create your views here.

@csrf_exempt
def login(request):
    status, AccessToken, RefreshToken = Utils.init()
    try:
        User = user.objects.get(phone_number = request.POST['phone_number'])
        # 检查用户密码
        if check_password(request.POST['password'], User.password):
            AccessToken = 'ThisIsAAccessToken'
        else:
            status = '11001'
    # 登陆用户不存在
    except user.DoesNotExist:
        status = '11001'
    return HttpResponse('''{"status" : "%s" , "AccessToken" : "%s", "RerfreshToken" : "%s"}'''
            % (status, AccessToken, RefreshToken))

@csrf_exempt
def reg(request):
    status, AccessToken, RefreshToken = Utils.init()
    try:
        User = user(phone_number = request.POST['phone_number'],
                password = make_password(request.POST['password']),
                user_real_name = request.POST['real_name'],
                user_mail = request.POST['mail'],
                user_device_token = request.POST['device_token'])
        User.save()
        status = User.user_id
    except IntegrityError:
        # 用户手机已被注册
        status = '10001'
    except KeyError:
        # POST 信息不完整
        status = 'fail'
    return HttpResponse('''{"status" : "%s" , "AccessToken" : "%s", "RerfreshToken" : "%s"}'''
            % (status, AccessToken, RefreshToken))
