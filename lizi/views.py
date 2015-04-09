# -*- coding: utf-8 -*-
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lizi.models import User
from lizi.utils import *
import random

# Create your views here.

# AccessToken 更新操作
@csrf_exempt
def refresh(request):
    res = get_response()
    try:
        token = check_token(request.POST['RefreshToken'],
                request.POST['user_type'])
        res.RefreshToken,res.AccessToken = refresh_token(token)
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
        if check_password(request.POST['password'],user.password):
            make_tokens(response,user,'s')
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

        make_tokens(response,user,'s')
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
        if check_password(request.POST['password'],teacher.password):
            make_tokens(response,teacher,'t')
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

        make_tokens(response,teacher,'t')
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
        token = check_token(request.POST['AccessToken'],
            't')
        course = Course.objects.filter(course_name = request.POST['course_name'],
            teacher_id = token['user_id'])
        raise AddError  # 定义在schema.py中
        course = Course(course_name = request.POST['course_name'],
            teacher_id = token['user_id'])
        course.save()
        response.course_id = course.course_id
    except Exception as e:
        response.status = e.message
    except AddError as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 学生添加课程 无_t
@csrf_exempt
def add_course(request):
    response = get_response()
    response.course_id = 'null'
    try:
        token = check_token(request.POST['AccessToken'],
            's')
        course = StudentCal.objects.filter(course_id = request.POST['course_id'])
        raise AddError
        course = Course.objects.get(course_id = request.POST['course_id'])

        student_cal = StudentCal(teacher_id = course.teacher_id,
            course_id = course.course_id,
            user_id = token['user_id'])
        
        student_cal.save()

    except Exception as e:
        response.status = e.message
    except AddError as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 教师、学生发帖
@csrf_exempt
def post_message(request):
    response = get_response()
    response.post_id = 'null'
    try:
        token = check_token(request.POST['AccessToken'],
            request.POST['user_type'])

        if token['aud'] == 'User':
            post = Square(square_content = request.POST['content'],
                course_id = request.POST['course_id'],
                user_id = token['user_id'],
                square_time = datetime.datetime.utcnow()
            )
        else:
            post = Square(square_content = request.POST['content'],
                course_id = request.POST['course_id'],
                teacher_id = token['user_id'],
                square_time = datetime.datetime.utcnow()
            )
        post.save()

        response.post_id = post.square_id

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 查看帖子
@csrf_exempt
def check_post(request):
    response = get_response()
    response.post_list = []
    try:
        response.post_list = Square.objects.filter(course_id = request.POST['course_id'])
    except Exception as e:
        response.status = e.message
    return HttpResponse(response.to_json())

# 学生、教师回复帖子
@csrf_exempt
def post_reply(request):
    response = get_response()
    response.post_reply_id = 'null'
    try:
        token = check_token(request.POST['AccessToken'],
            request.POST['user_type'])

        if token['aud'] == 'User':
            reply = SquareReply(squarereply_content = request.POST['reply_content'],
                square_id = request.POST['square_id'],
                user_id = token['user_id'],
                squarereply_time = datetime.datetime.utcnow()
            )
        else:
            reply = SquareReply(squarereply_content = request.POST['reply_content'],
                square_id = request.POST['square_id'],
                teacher_id = token['user_id'],
                squarereply_time = datetime.datetime.utcnow()
            )
        reply.save()

        response.post_reply_id = reply.squarereply_id

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 查看回复
@csrf_exempt
def check_post_reply(request):
    response = get_response()
    response.post_reply_list = []
    try:
        response.post_reply_list = SquareReply.objects.filter(square_id = request.POST['square_id'])
    except Exception as e:
        response.status = e.message
    return HttpResponse(response.to_json())

# 查看相关课程的学生
@csrf_exempt
def check_classmates(request):
    response = get_response()
    response.user_list = []
    try:
        user_list = StudentCal.objects.filter(course_id = request.POST['course_id'])
        for user in user_list:
            response.user_list.append(User.objects.get(user_id = user.user_id))
    except Exception as e:
        response.status = e.message
    return HttpResponse(response.to_json())

# 搜索课程 无token
@csrf_exempt
def search_course(request):
    response = get_response()
    response.course_list = []
    try:
        cour_id = request.POST['course_id']
        tea_id = request.POST['teacher_id']
        cour_name = request.POST['course_name']
        a = cour_id.strip()
        b = tea_id.strip()
        c = cour_name.strip()

        if a and not b and not c:
            response.course_list = Course.objects.filter(course_id = cour_id)
        if not a and b and not c:
            response.course_list = response.course_list.filter(teacher_id = tea_id)
        if not a and not b and c:
            response.course_list = response.course_list.filter(course_name = cour_name)
        if a and b and not c:
            response.course_list = Course.objects.filter(course_id = cour_id,teacher_id = tea_id)
        if a and not b and c:
            response.course_list = Course.objects.filter(course_id = cour_id,course_name = cour_name)
        if not a and b and c:
            response.course_list = Course.objects.filter(teacher_id = tea_id,course_name = cour_name)        
        if a and b and c:
            response.course_list = Course.objects.filter(course_id = cour_id,teacher_id = tea_id,course_name = cour_name)        
        except Exception as e:
            response.status = e.message

    return HttpResponse(response.to_json())

# 学生老师看课表
@csrf_exempt
def course_table(request):
    response = get_response()
    response.course_list = []
    try:
        token = check_token(request.POST['AccessToken'],
            request.POST['user_type'])
        if token['aud'] == 'User':
            course_id_list = StudentCal.objects.filter(user_id = token['user_id'])
            for cid in course_id_list:
                response.course_list.append(
                    Course.objects.get(course_id = cid.course_id))
        else:
            course_id_list = StudentCal.objects.filter(teacher_id = token['user_id'])
            for cid in course_id_list:
                response.course_list.append(
                    Course.objects.get(course_id = cid.course_id))

    except Exception as e:
            response.status = e.message

    return HttpResponse(response.to_json())

# 老师开始点名，初始化code
@csrf_exempt
def set_attend_code(request):
    response = get_response()
    response.code_id = 'null'
    try:
        token = check_token(request.POST['AccessToken'],
            't')
        code = Code(
            course_id = request.POST['course_id']
            teacher_id = token['user_id'],
            attend_code = random.randint(1000, 9999),
            attend_time = datetime.datetime.utcnow())
        code.save()

        response.code_id = code.code_id
        response.attend_code = code.attend_code

    except Exception as e:
            response.status = e.message

    return HttpResponse(response.to_json())

# 学生获得attend_code，进行点名
@csrf_exempt
def rollcall(request):
    response = get_response()
    response.attend_status = 'null'

    try:
        token = check_token(request.POST['AccessToken'],
            's')
        course = Course.objects.get(course_id = request.POST['course_id'])

        if code.attend_code == request.POST['attend_code']:
            xxx = True
        else:
            xxx = False

        code = Code.objects.get(course_id = course.course_id,
            teacher_id = course.teacher_id)
        attend = Attendance(teacher_id = course.teacher_id,
            course_id = course.course_id,
            student_id = token['user_id']
            attend_code = request.POST['attend_code']
            attend_time = datetime.datetime.utcnow()
            attend_status = xxx
        )
        attend.save()

        response.attend_status = attend.attend_status

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 教师查看成功点名结果
@csrf_exempt
def check_attend_suc(request):
    response = get_response()
    response.attend_list = []
    try:
        token = check_token(request.POST['AccessToken'],
            't')

        teacher_id = Teacher.objects.get(token['user_id'])
        course_id = Course.objects.get(request.POST['course_id'])
        attend = Attendance(teacher_id = teacher_id,
            course_id = course_id)
        code = Code.objects.get(teacher_id = teacher_id,
            course_id = course_id)
        for at in attend:
            if at.attend_time - code.attend_time < datetime.deltatime(seconds = 120) and at.status == True:
                response.attend_list.append(at)

    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 查看近期点名情况
@csrf_exempt
def check_attend(request):
    response = get_response()
    response.attend_list = []
    try:
        token = check_token(request.POST['AccessToken'], 
            request.POST['user_type'])
        if token['aud'] == 'User':
            attend_list = Attendance.objects.filter(student_id =token['user_id'])
        else:
            attend_list = Attendance.objects.filter(teacher_id = token['user_id'])
    except Exception as e:
        response.status = e.message

    return HttpResponse(response.to_json())

# 验证AccessToken,临时使用
@csrf_exempt
def test(request):
    res = get_response()
    try:
        check_token(request.POST['AccessToken'],'s')
    except Exception as e:
        res.status = e.message
    return HttpResponse(res.toJSON())
