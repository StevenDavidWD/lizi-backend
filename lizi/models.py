from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key = True)
    phone_number = models.CharField(max_length = 11, unique = True)
    password = models.CharField(max_length = 120)
    user_real_name = models.CharField(max_length = 20)
    user_points = models.IntegerField(default = 0)
    user_mail = models.CharField(max_length = 50)
    user_head_img = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True, null = True)
    user_sex = models.IntegerField(default = 0)
    user_device_token = models.CharField(max_length = 255)

class teacher(models.Model):
    teacher_id = models.AutoField(primary_key = True)
    phone_number = models.CharField(max_length = 11, unique = True)
    password = models.CharField(max_length = 32)
    teacher_real_name = models.CharField(max_length = 20)
    teacher_points = models.IntegerField(default = 0)
    teacher_mail = models.CharField(max_length = 50)
    teacher_head_img = models.CharField(max_length = 255)
    teacher_sex = models.IntegerField(default = 0)
    teacher_device_token = models.CharField(max_length = 255)

class course(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 255)
    teacher_id = models.ForeignKey(teacher)

class studentCal(models.Model):
    cal_id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(course)
    user_id = models.ForeignKey(user)

class square(models.Model):
    square_id = models.AutoField(primary_key = True)
    square_content = models.CharField(max_length = 2000)
    course_id = models.ForeignKey(course)
    user_id = models.ForeignKey(user)
    square_time = models.DateTimeField()

class square_reply(models.Model):
    squarereply_id = models.AutoField(primary_key = True)
    squarereply_content = models.CharField(max_length = 1000)
    square_id = models.ForeignKey(square)
    user_id = models.ForeignKey(user)
    squarereply_time = models.DateTimeField()

class attendance(models.Model):
    course_id = models.AutoField(primary_key = True)
    teacher_id = models.ForeignKey(teacher)
    student_id = models.ForeignKey(user)
    attend_time = models.DateTimeField()
    attend_status = models.CharField(max_length = 10)
    attend_code = models.BigIntegerField()

class code(models.Model):
    id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(course)
    attend_code = models.BigIntegerField()
    attend_time = models.DateTimeField()
