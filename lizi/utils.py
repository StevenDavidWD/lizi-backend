# -*- coding: utf-8 -*-
from lizi.schema import *
import jwt

# jwt加密的密钥
secret = 'ThisIsAWeakBird'

# 返回登录, 注册的基本信息
def init():
    return Status()

# 返回获取信息的基本信息
def get_response():
	return Response()

# 验证token是否有效, user_type 用于检查为学生还是老师, 防止使用
# 学生的token, 获得教师的权限
def check_token(token, user_type):
	try:
		return jwt.decode(token, secret,
				issuer = 'SundayDX', audience = user_type,
				algorithms = ['HS256'])
	except jwt.ExpiredSignatureError:
		# token 授权超时
		raise Exception("10002")
	except jwt.InvalidAudience:
		# token 类型错误
		raise Exception("10003")
	except jwt.InvalidIssuer:
		# token 发布认证被篡改
		raise Exception("10004")
	except Exception as e:
		# token 未知错误
		raise Exception("10005")

# 更新AccessToken, token_type用于区分AccessToken和RefreshToken
# 防止使用AccessToken进行更新
def refresh_token(token):
	if token['token_type'] != 'r':
		# token 不为 RefreshToken
		raise Exception('10006')
	ReToken = access_token(token['user_id'], token['aud'], 30, 'r')
	AcToken = access_token(token['user_id'], token['aud'], 1, 'a')
	ReToken = jwt.encode(ReToken, secret, algorithm = 'HS256')
	AcToken = jwt.encode(AcToken, secret, algorithm = 'HS256')
	return ReToken, AcToken

# 在返回信息中加入AccessToken和RefreshToken, 仅适用登录注册
def make_tokens(response, User, user_type):
	response.set_refreshtoken(jwt.encode(
		access_token(User.user_id, user_type, 30, 'r'), secret,
		algorithm = 'HS256'))
	response.set_accesstoken(jwt.encode(
		access_token(User.user_id, user_type, 1, 'a'), secret,
		algorithm = 'HS256'))
