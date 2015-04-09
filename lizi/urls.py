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
    url(r'^t/reg/', views.reg_t, name='reg_t'),
	#测试用
	url(r'^test/', views.test, name='test'),
	#刷新token
	url(r'^refresh/', views.refresh, name='refresh'),
	#添加课程
	url(r'^t/addcourse/', views.add_course_t, name='addCourse_t'),
	url(r'^addcourse/', views.add_course, name='addCourse'),
	#发布消息、回复消息
	url(r'^postmessage/', views.post_message, name='postMessage'),	
	url(r'^postreply/', views.post_reply, name='postReply'),
	#查看消息、查看回复
	url(r'^checkmessage/', views.check_post, name='checktMessage'),	
	url(r'^checkreply/', views.check_post_reply, name='checkReply'),
	#查找某门课
	url(r'^searchcourse/', views.search_course, name='searchCourse'),
	#查看课表
	url(r'^coursetable/', views.course_table, name='coursetable'),
	#查看相关课程学生
	url(r'^checkclassmates/', views.check_classmates, name='checkclassmates'),
	#为某一门课添加点名码
	url(r'^t/addendcode', views.set_addend_code, name='addendcode'),
	#学生点名接口
	url(r'^rollcall/', views.rollcall, name='rollcall'),
	#查看点名人员的接口
	url(r'^t/checkattendsec/', views.check_attend_sec, name='checkAttendSec'),
	url(r'^checkattend/', views.check_attend, name = 'checkAttend'),
)
