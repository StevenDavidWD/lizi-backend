# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# 学生用户信息表
class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    phone_number = models.CharField(max_length = 11, unique = True)
    password = models.CharField(max_length = 120)
    user_real_name = models.CharField(max_length = 20)
    user_points = models.IntegerField(default = 0)
    user_mail = models.EmailField(max_length = 50)
    user_head_img = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True, null = True)
    user_sex = models.IntegerField(default = 0)
    user_device_token = models.CharField(max_length = 255)

# 教师用户信息表
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key = True)
    phone_number = models.CharField(max_length = 11, unique = True)
    password = models.CharField(max_length = 32)
    teacher_real_name = models.CharField(max_length = 20)
    teacher_points = models.IntegerField(default = 0)
    teacher_mail = models.EmailField(max_length = 50)
    teacher_head_img = models.CharField(max_length = 255)
    teacher_sex = models.IntegerField(default = 0)
    teacher_device_token = models.CharField(max_length = 255)

# 课程信息表
class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 255)
    teacher_id = models.ForeignKey(Teacher)

# 学生选课关系表
class StudentCal(models.Model):
    cal_id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(Course)
    teacher_id = models.ForeignKey(Teacher)
    user_id = models.ForeignKey(User)

# 课程交流信息表
class Square(models.Model):
    square_id = models.AutoField(primary_key = True)
    square_content = models.TextField
    course_id = models.ForeignKey(Course)
    user_id = models.ForeignKey(User)
    teacher_id = models.ForeignKey(Teacher)
    square_time = models.DateTimeField()

    class Meta:
        ordering = ['-square_time']

# 课程交流信息回复表
class SquareReply(models.Model):
    squarereply_id = models.AutoField(primary_key = True)
    squarereply_content = models.TextField
    square_id = models.ForeignKey(Square)
    user_id = models.ForeignKey(User)
    teacher_id = models.ForeignKey(Teacher)
    squarereply_time = models.DateTimeField()

    class Meta:
        ordering = ['-squarereply_time']

# 签到信息表
class Attendance(models.Model):
    attend_id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(Course)
    teacher_id = models.ForeignKey(Teacher)
    student_id = models.ForeignKey(User)
    attend_time = models.DateTimeField()
    attend_status = models.CharField(max_length = 10)
    attend_code = models.BigIntegerField()

    class Meat:
        ordering = ['-attend_time']


# 签到验证码信息表
class Code(models.Model):
    code_id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(Course)
    teacher_id = models.ForeignKey(Teacher)
    attend_code = models.BigIntegerField()
    attend_time = models.DateTimeField()
