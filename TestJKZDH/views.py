from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from TestJKZDH.models import *

@login_required
def welcome(request):
    print("进来了")
    # 调用的HttpResponse函数是用来返回一个字符串的，后续返回的json格式字符串也是用它，
    # HttpResponseRedirect 是用来重定向到其他url上的。
    # render是用来返回html页面和页面初始数据的。
    # return HttpResponse("欢迎来到主页");
    return render(request,"welcome.html")

def child(request,eid,oid):
    print("request------------" + "child")
    print(eid)
    print(oid)
    res = child_json(eid,oid)
    return render(request,eid,res)
def child_json(eid,oid=""):
    res = {}
    if eid == "home.html":
        # 数据格式其实是queryset
        data = DB_home_href.objects.all();
        res = {"hrefs":data}
    if eid == 'project_list.html':
        data = DB_project.objects.all();
        res = {"projects": data}
    if eid == 'P_apis.html':
        project_name = DB_project.objects.filter(id=oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res = {"project_name":project_name,"apis":apis}
    if eid == 'P_cases.html':
        project_name = DB_project.objects.filter(id=oid)[0]
        res = {"project_name":project_name}
    if eid == 'P_project_set.html':
        project_name = DB_project.objects.filter(id=oid)[0]
        res = {"project_name":project_name}
    return res



# 为了不放行在未进行登陆的状况下就进入主页  需要加上 @login_required

# @login_required
def home(request):
    print("request---------------"+"home")
    return render(request,'welcome.html',{"whichHTML": "home.html","oid":request.user.id})
    # return render(request,'home.html')
# 3. 把菜单作为后台唯一能返回的html，也就是唯一的render函数内的那个html参数。
# 然后在菜单welcome.html 中 把其他各个页面都当作一个子页面 一个来引入。

def login(request):
    print("request"+"----------login")
    return render(request,'login.html')

#开始登陆
# 然后让我们思考这个函数应该做些什么事？
# 获取前端给的 俩个字符串：用户名和密码
# 调用django自带的用户数据库，来验证这个用户是否存在并且密码正确
# 如果不正确，就随便给前端返回点什么，前端都会弹窗说报错文案
# 如果正确，就给用户进行重定向，定到首页：home.html

def login_action(request):
    print("request"+"------------------login_action")
    u_name = request.GET['username']
    p_word = request.GET['password']
    print(u_name,p_word)
    #  开始继续写验证用户名密码代码：
    from django.contrib import auth
    user = auth.authenticate(username=u_name,password=p_word)
    if user is not None:
        # 进行正确的动作
        return HttpResponse('成功')
    else:
        # 返回线圈告诉前端用户名密码不对
        return HttpResponse("失败")

def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name,password=p_word)
        user.save()
        return HttpResponse("注册成功")
    except:
        return HttpResponse("注册失败~用户名好像存在")

def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')

# 通过钉钉的机器人发消息 ，此方法比较实时。很快速。而且不用存放在我们平台的数据库，省空间。但是操作起来需要钉钉里面群里添加机器人-发送接口 ，初次使用会很蒙蔽。
# 发短信/邮件，此方法也可以，但是就是有点小题大做。而且调取短信接口花钱，发送邮件代码不是很好写。有兴趣的可以自己这么做
# 存放在django平台的数据库中，给创建个吐槽表，然后管理员可以去后台随时查看，以后我们还可以利用这些吐槽做个弹幕.....  而且这里我正好可以给大家讲一下，如何新建一个表 和 如何操作这个表 的技术。
def pei(request):
    print("request"+"-----------------------")
    print(request)
    print("request" + "-----------------------")
    tucao_text = request.GET['tucao_text']
    # 我们本来有4个字段：id user text ctime ,因为id为自动创建不用我们操心，ctime也是自动填入也不用我们操心，所以我们这里只写user 和 text即可
    DB_tucao.objects.create(user=request.user.username,text=tucao_text)
    return HttpResponse("")

def api_help(request,oid=""):
    return render(request,"welcome.html",{"whichHTML":"help.html","oid":request.user.id})

def project_list(request):
    return render(request,"welcome.html",{"whichHTML":"project_list.html","oid":request.user.id})

def delete_project(request):
    # .filter() 方法可以找出所有符合的数据记录，当然这里我们肯定只能找到一条。但是返回的仍然是一个类似列表的格式，虽然只有一个元素。
    # 后接.delete()方法 ，可以删除。然后直接返回给前端，证明事办完了。前端就会自动刷新，用户看到的就是 这个项目不见了。
    id = request.GET['id']
    DB_project.objects.filter(id=id).delete();
    return HttpResponse('')

def add_project(request):
    print("add_project")
    project_name = request.GET['project_name']
    DB_project.objects.create(name=project_name,remark='',user=request.user.username,other_user='')
    return HttpResponse('')


def open_apis(request,id):
    project_id = id
    return render(request,'welcome.html',{"whichHTML":"P_apis.html","oid":id})

def open_cases(request,id):
    return render(request,"welcome.html",{"whichHTML":"P_cases.html","oid":id})

def open_project_set(request,id):
    return render(request,"welcome.html",{"whichHTML":"P_project_set.html","oid":id})

def save_project_set(request,id):
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    DB_project.objects.filter(id=id).update(name=name,remark=remark,other_user=other_user)
    return HttpResponse('')

def save_bz(request):
    api_id = request.GET['api_id']
    bz_value = request.GET['bz_value']
    DB_apis.objects.filter(id=api_id).update(des=bz_value)
    return HttpResponse('')

def open_bz(request):
    api_id = request.GET['api_id']
    bz_value = DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_value)