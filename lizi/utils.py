# -*- coding: utf-8 -*-
import jwt
from lizi.schema import *

secret = 'ThisIsAWeakBird'

def init():
    return Status()

def checkToken(token, user_type):
	try:
		return jwt.decode(token, secret,
				issuer = 'SundayDX', aud = user_type,
				algorithms = ['HS256'])
	except jwt.ExpiredSignatureError:
		raise "TokenExpired"
	except jwt.InvalidAudience:
		raise "TypeError"
	except jwt.InvalidIssuer:
		raise "FakeToken"
	except:
		raise "TokenError"

def makeTokens(response, User, user_type):
	response.setRefreshToken(jwt.encode(
		AccessToken(User.user_id, user_type, 30), secret,
		algorithm = 'HS256'))
	response.setAccessToken(jwt.encode(
		AccessToken(User.user_id, user_type, 1), secret,
		algorithm = 'HS256'))
