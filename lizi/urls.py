from django.conf.urls import patterns, url

from lizi import views

# url中t/下的url为教师特有接口
# 其他为共有接口

urlpatterns = patterns('',
	#登陆
    url(r'^login/', views.login, name='login'),
    url(r'^t/login/', views.login_t, name='login_t'),
    #注册
    url(r'^reg/', views.reg, name='reg'),
<<<<<<< HEAD
    url(r'^t/reg/', views.reg_t, name='reg_t'),
	#测试用
	url(r'^test/', views.test, name='test'),
	#刷新token
	url(r'^refresh/', views.refresh, name='refresh'),
	#添加课程
	url(r'^t/addCourse/', views.add_course_t, name='addCourse_t'),
	url(r'^addCourse/', views.add_course, name='addCourse'),
	#发布消息、回复消息
	url(r'^postMessage/', views.post_message, name='postMessage'),	
	url(r'^postReply/', views.post_reply, name='postReply'),
	#查找某门课
	url(r'^searchCourse/', views.search_course, name='searchCourse'),
	#查看课表
	url(r'^course_table/', views.course_table, name='course_table'),
	#为某一门课添加点名码
	url(r'^t/addend_code', views.set_addend_code, name='addend_code'),
	#学生点名接口
	url(r'^rollCall/', views.rollcall, name='rollcall'),
	#查看点名人员的接口
	url(r'^t/checkAttend/', views.checkattend, name='checkAttend'),
	
    url(r'^test/', views.test, name='test'),
    url(r'^refresh/', views.refresh, name='refresh')
)
