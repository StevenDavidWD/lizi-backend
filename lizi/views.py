from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lizi.models import user

# Create your views here.

@csrf_exempt
def login(request):
    status = 'init'
    token = 'init'
    try:
        User = user.objects.get(phone_number = request.POST['phone_number'])
        if check_password(request.POST['password'], User.password):
            status = 'ok'
            token = 'fuck!'
        else:
            status = 'no'
            token = User.password
    except user.DoesNotExist:
        status = 'fail'
        token = 'null'
    return HttpResponse('''{"status" : "%s" , "token" : "%s"}''' % (status, token))

@csrf_exempt
def reg(request):
    status = 'init'
    token = 'init'
    salt = '81124'
    try:
        #status = make_password(request.POST['password'])
        #status = make_password(request.POST['password'], None, 'bcrypt')[15:40]
        token = request.POST['phone_number']
        User = user(phone_number = request.POST['phone_number'], password = make_password(request.POST['password']))
        User.save()
        status = User.user_id
    except:
        status = 'fail'
        token = 'null'
    return HttpResponse('''{"status" : "%s" , "token" : "%s"}''' % (status, token))
