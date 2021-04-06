from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def welcome(request):
    print("进来了")
    # 调用的HttpResponse函数是用来返回一个字符串的，后续返回的json格式字符串也是用它，
    # HttpResponseRedirect 是用来重定向到其他url上的。
    # render是用来返回html页面和页面初始数据的。
    # return HttpResponse("欢迎来到主页");
    return render(request,"welcome.html")

def child(request,eid):
    print("request------------" + "child")
    print(eid)
    return render(request,eid)

def home(request):
    print("request---------------"+"home")
    return render(request,'welcome.html',{"whichHTML": "home.html","oid": ""})
    # return render(request,'home.html')
# 3. 把菜单作为后台唯一能返回的html，也就是唯一的render函数内的那个html参数。
# 然后在菜单welcome.html 中 把其他各个页面都当作一个子页面 一个来引入。

def login(request):
    return render(request,'login.html')