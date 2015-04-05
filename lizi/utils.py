# -*- coding: utf-8 -*-
from lizi.schema import *
import jwt

secret = 'ThisIsAWeakBird'

def init():
    return Status()

def getResponse():
	return Response()

def checkToken(token, user_type):
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

def refreshToken(token):
	if token['token_type'] != 'r':
		# token 不为 RefreshToken
		raise Exception('10006')
	ReToken = AccessToken(token['user_id'], token['aud'], 30, 'r')
	AcToken = AccessToken(token['user_id'], token['aud'], 1, 'a')
	ReToken = jwt.encode(ReToken, secret, algorithm = 'HS256')
	AcToken = jwt.encode(AcToken, secret, algorithm = 'HS256')
	return ReToken, AcToken

def makeTokens(response, User, user_type):
	response.setRefreshToken(jwt.encode(
		AccessToken(User.user_id, user_type, 30, 'r'), secret,
		algorithm = 'HS256'))
	response.setAccessToken(jwt.encode(
		AccessToken(User.user_id, user_type, 1, 'a'), secret,
		algorithm = 'HS256'))
