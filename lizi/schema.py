# Create for lizi-backend
import json
import datetime

def convert_to_builtin_type(obj):
    builtin_type = {}
    builtin_type.update(obj.__dict__)
    return builtin_type

def AccessToken(user_id, user_type, time):
	return {
		'user_id' : user_id,
		'aud' : user_type
		'iss' : 'SundayDX'
		'exp' : datetime.datetime.utcnow() \
				+ datetime.timedelta(days = time)
			}

class Status(object):

    def __init__(self):
        self.status = "00000"
        self.AccessToken = "null"
        self.RefreshToken = "null"

    def setStatus(self, status):
        self.status = status

    def setAccessToken(self, AccessToken):
        self.AccessToken = AccessToken

    def setRefreshToken(self, RefreshToken):
        self.RefreshToken = RefreshToken

    def toJSON(self):
        return json.dumps(self, default = convert_to_builtin_type)
