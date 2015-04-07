# -*- coding: utf-8 -*-
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lizi.models import User
from lizi.utils import *

# Create your views here.

# 学生登录操作
@csrf_exempt
def login(request):
    response = init()
    try:
        user = User.objects.get(phone_number = request.POST['phone_number'])
        # 检查用户密码
        if check_password(request.POST['password'], user.password):
            make_tokens(response, user, 's')
        else:
            response.set_status('11001')
    # 登陆用户不存在
    except User.DoesNotExist:
        response.set_status('11001')
    # POST 信息不完整
    except KeyError:
        response.set_status('00001')
    return HttpResponse(response.to_json())

# 学生注册操作
@csrf_exempt
def reg(request):
    response = init()
    try:
        user = User(phone_number = request.POST['phone_number'],
                password = make_password(request.POST['password']),
                user_real_name = request.POST['real_name'],
                user_mail = request.POST['mail'],
                user_device_token = request.POST['device_token'])
        user.save()

        make_tokens(response, user, 's')
    except IntegrityError:
        # 用户手机已被注册
        response.set_status('10001')
    except KeyError:
        # POST 信息不完整
        response.set_status('00001')
    return HttpResponse(response.to_json())

# 教师登录操作
@csrf_exempt
def login_t(request):
    response = init()
    try:
        teacher = Teacher.objects.get(phone_number = request.POST['phone_number'])
        # 检查用户密码
        if check_password(request.POST['password'], teacher.password):
            make_tokens(response, teacher, 't')
        else:
            response.set_status('11001')
    except Teacher.DoesNotExist:
        # 教师用户不存在
        response.set_status('11001')
    except KeyError:
        # POST 信息不完整
        response.set_status('00001')
    return HttpResponse(response.to_json())

# 教师注册操作
@csrf_exempt
def reg_t(request):
    response = init()
    try:
        teacher = Teacher(phone_number = request.POST['phone_number'],
                password = make_password(request.POST['password']),
                teacher_real_name = request.POST['real_name'],
                teacher_mail = request.POST['mail'],
                teacher_device_token = request.POST['device_token'])
        teacher.save()

        make_tokens(response, teacher, 't')
    except IntegrityError:
        # 用户手机已被注册
        response.set_status('10001')
    except KeyError:
        # POST 信息不完整
        response.set_status('00001')
    return HttpResponse(response.to_json())

# 教师添加课程
@csrf_exempt
def add_course_t(request):
    response = get_response()


# AccessToken 更新操作
@csrf_exempt
def refresh(request):
    res = get_response()
    try:
        token = check_token(request.POST['RefreshToken'],
                request.POST['user_type'])
        res.RefreshToken, res.AccessToken = refresh_token(token)
    except Exception as e:
        res.status = e.message
    return HttpResponse(res.to_json())

# 验证AccessToken, 临时使用
@csrf_exempt
def test(request):
    res = getResponse()
    try:
        check_token(request.POST['AccessToken'], 's')
    except Exception as e:
        res.status = e.message
    return HttpResponse(res.toJSON())
