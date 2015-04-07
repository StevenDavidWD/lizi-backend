# -*- coding: utf-8 -*-
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lizi.models import User
from lizi.utils import *

# Create your views here.

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
    response.course_id = 'null'
    try:
        teacher = Teacher.objects.get(phone_number = request.POST['phone_number'])
        token = check_token(request.POST['RefreshToken'], 
            request.POST['user_type'])
        course = Course(course_name = request.POST['course_name'],
            teacher_id = teacher.teacher_id)
        course.save()
        response.course_id = course.course_id
    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 学生添加课程 无_t
@csrf_exempt
def add_course(request):
    response = get_response()
    response.course_id = 'null'
    try:
        student = User.objects.get(phone_number = request.POST['phone_number'])
        token = check_token(request.POST['RefreshToken'], 
            request.POST['user_type'])
        course = Course.objects.get(course_id = request.POST['course_id'])

        student_cal = StudentCal(teacher_id = course.teacher_id,
            course_id = course.course_id,
            user_id = student.user_id)
        
        student_cal.save()

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 发帖，学生、老师发帖一个接口
@csrf_exempt
def post_message(request):
    response = get_response()
    response.post_id = 'null'
    try:
        poster_type = request.POST['poster_type']
        if poster_type == 'User':
            poster = User.objects.get(phone_number = request.POST['phone_number'])
            poster_id = poster.user_id
        else:
            poster = Teacher.objects.get(phone_number = request.POST['phone_number'])
            poster_id = teacher_id

        token = check_token(request.POST['RefreshToken'], 
            poster_type)
        post = Square(square_content = request.POST['content'],
            course_id = request.POST['course_id'],
            user_id = poster_id,
            square_time = datetime.datetime.utcnow())
        post.save()

        response.post_id = post_id

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())


# 回复帖子
@csrf_exempt
def post_reply(request):
    response = get_response()
    response.post_reply_id = 'null'
    try:
        replyer_type = request.POST['replyer_type']
        if replyer_type == 'User':
            replyer = User.objects.get(phone_number = request.POST['phone_number'])
            replyer_id = replyer.user_id
        else:
            replyer = Teacher.objects.get(phone_number = request.POST['phone_number'])
            replyer_id = replyer.teacher_id

        token = check_token(request.POST['RefreshToken'],
            replyer_type)
        reply = SquareReply(squarereply_content = request.POST['reply_content'],
            square_id = request.POST['square_id'],
            user_id = replyer_id
            squarereply_time = datetime.datetime.utcnow())
        reply.save()

        response.post_reply_id = reply.squarereply_id

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())


# 搜索课程
@csrf_exempt
def search_course(request):
    response = get_response()
    response.course_list = []
    try:
        cour_id = request.POST['course_id']
        tea_name = request.POST['teacher_real_name']
        cour_name = request.POST['course_name']
        if cour_id.strip():
            response.course_list = Course.objects.filter(
                course_id = cour_id)
        if tea_name.strip():
            response.course_list = Course.objects.filter(
                Teacher.objects.filter(teacher_real_name = tea_name))  #需测试二层filter是否可行
        if cour_name.strip():
            response.course_list = Course.objects.filter(
                course_name = cour_name)

        except Exception as e:
            response.status = e.message

    return HttpResponse(response.to_json())

# 学生老师看课表
@csrf_exempt
def course_table(request):
    response = get_response()
    response.course_list = []
    try:
        viewer_name = request.POST['viewer_name']
        viewer_type = request.POST['viewer_type']
        if viewer_type == 'User':
            user_id = User.objects.get(user_real_name = 'viewer_name')
            course_id_list = StudentCal.objects.filter(user_id = user_id)
            for cid in course_id_list:
                response.course_list.append(
                    Course.objects.get(course_id = cid))
        else:
            user_id = User.objects.get(teacher_real_name = 'viewer_name')
            course_id_list = StudentCal.objects.filter(teacher_id = user_id)
            for cid in course_id_list:
                response.course_list.append(
                    Course.objects.get(course_id = cid))
    except Exception as e:
            response.status = e.message

    return HttpResponse(response.to_json())

# 老师开始点名，初始化code
@csrf_exempt
def set_attend_code(request):
    response = get_response()
    response.code_id = 'null'
    try:
        teacher_name = request.POST['teacher_real_name']
        course_name = request.POST['course_name']
        teacher_id = Teacher.objects.get(teacher_real_name = teacher_name)
        course = Course.objects.get(course_name = cour_name, teacher_id = teacher_id)
        code = Code(
            course_id = course.course_id,
            teacher_id = teacher_id,
            attend_code = request.POST['attend_code'],
            attend_time = datetime.datetime.utcnow())
        code.save()

        response.code_id = code.code_id

    except Exception as e:
            response.status = e.message

    return HttpResponse(response.to_json())

# 学生获得attend_code， 进行点名
@csrf_exempt
def rollcall(request):
    

# 验证AccessToken, 临时使用
@csrf_exempt
def test(request):
    res = get_response()
    try:
        check_token(request.POST['AccessToken'], 's')
    except Exception as e:
        res.status = e.message
    return HttpResponse(res.toJSON())
