from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import UserBean

@csrf_exempt
def insert(request):
    user = UserBean.objects.create(name='xiaoming',age=20)
    print("insert " + user.name + "ok")
    return HttpResponse("nothing to do")

@csrf_exempt
def delete(request):
    UserBean.objects.filter(name__contains="xiaoming").delete()  # 删除 名称中包含 "abc"的人
    print("delete success")

@csrf_exempt
def update(request):
    user = UserBean.objects.get(name="xiaoming")
    user.name = "Jack"
    user.age = 30
    user.save()

@csrf_exempt
def find(request):
    name = request.GET.get("name")
    print("name is " + name)
    print("findAll")
    list = UserBean.objects.all()
    for user in list:
        print(user.name)
    return HttpResponse("nothing to do")
