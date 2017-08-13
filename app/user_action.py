from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def checkUser(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

@csrf_exempt
def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password',None)

    s_username = request.session.get('s_username', None)
    if s_username is not None: # 第一次使用session 时候初始化数据库 python manage.py migrate
        return render_to_response('main.html', {'s_username': s_username})
    else:
        flag = checkUser(username,password)
        if flag:
            request.session['s_username'] = username
            return render_to_response('main.html', {'s_username': username})
        else:
            return render_to_response("login.html")

def loginUI(request):
    return render_to_response("login.html")

@csrf_exempt
def logout(request):
    try:
        del request.session['s_username']
    except KeyError:
        pass
    return HttpResponseRedirect("/loginUI/")