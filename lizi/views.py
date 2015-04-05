# -*- coding: utf-8 -*-
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lizi.models import user
from lizi.utils import *

# Create your views here.

@csrf_exempt
def login(request):
    response = init()
    try:
        User = user.objects.get(phone_number = request.POST['phone_number'])
        # 检查用户密码
        if check_password(request.POST['password'], User.password):
            makeTokens(response, User, 's')
            #response.setAccessToken = 'ThisIsAAccessToken'
        else:
            response.setStatus('11001')
    # 登陆用户不存在
    except user.DoesNotExist:
        response.setStatus('11001')
    return HttpResponse(response.toJSON())

@csrf_exempt
def reg(request):
    response = init()
    try:
        User = user(phone_number = request.POST['phone_number'],
                password = make_password(request.POST['password']),
                user_real_name = request.POST['real_name'],
                user_mail = request.POST['mail'],
                user_device_token = request.POST['device_token'])
        User.save()

        makeTokens(response, User, 's')
    except IntegrityError:
        # 用户手机已被注册
        response.setStatus('10001')
    except KeyError:
        # POST 信息不完整
        response.setStatus('00001')
    return HttpResponse(response.toJSON())

@csrf_exempt
def refresh(request):
    res = getResponse()
    try:
        token = checkToken(request.POST['RefreshToken'],
                request.POST['user_type'])
        res.RefreshToken, res.AccessToken = refreshToken(token)
    except KeyError as e:
        res.status = e.message
    return HttpResponse(res.toJSON())

@csrf_exempt
def test(request):
    res = getResponse()
    try:
        checkToken(request.POST['AccessToken'], 's')
    except Exception as e:
        res.status = e.message
    return HttpResponse(res.toJSON())
