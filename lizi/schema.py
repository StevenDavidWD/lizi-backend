# -*- coding: utf-8 -*-
# Create for lizi-backend
import json
import datetime

# 自定义的类对象转变为JSON的依赖函数
def convert_to_builtin_type(obj):
    builtin_type = {}
    builtin_type.update(obj.__dict__)
    return builtin_type

# token的基本结构, AccessToken 和 RefreshToken 不同之处在于
# token_type分别为 'a', 'r'. time 为 1, 30.
# user_type 用于区分学生与教师
def access_token(user_id, user_type, time, token_type):
	return {
		'user_id' : user_id,
		'token_type' : token_type,
		'aud' : user_type,
		'iss' : 'SundayDX',
		'exp' : datetime.datetime.utcnow() \
				+ datetime.timedelta(days = time)
	}

# 每次回复的基本结构信息
class Response(object):

	def __init__(self):
		self.status = "00000"

	def to_json(self):
		return json.dumps(self, default = convert_to_builtin_type)

class AddError(Exception):
    def __init__(self):
        self.message = "Class has been added!"

# 登录注册的回复基本结构
class Status(object):

    def __init__(self):
        self.status = "00000"
        self.AccessToken = "null"
        self.RefreshToken = "null"

    def set_status(self, status):
        self.status = status

    def set_accesstoken(self, AccessToken):
        self.AccessToken = AccessToken

    def set_refreshtoken(self, RefreshToken):
        self.RefreshToken = RefreshToken

    def to_json(self):
        return json.dumps(self, default = convert_to_builtin_type)
