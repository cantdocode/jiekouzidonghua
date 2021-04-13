第一天
实现welcome页面和home页面进行整合，添加显示隐藏的标签，主页标签

第二天
功能实现
    注册
    登陆
总的实现路线  
---》login.html  
-->  js实现username和password的获取   
--->  实现jquery的方法，onclick() ---->  login_active
--->  login_active --url路由调用login_active的方法
--->  login_active 判断获取前端的username和password
--->  给出一个ret的判断接口，由前端页面判断ret的成功则跳转主页，否则抛出用户名错误
--->  注册功能  方式和上面一样，ret的放回结果由registe_active 给出

第三天
---- 退出功能实现  django.contrib import autho
由auth.logout 实现退出功能
---- 自带后台 admin
python3 manage.py createsuperuser

---- 基于生态考虑的菜单重构+意见反馈功能设计
1.首先改菜单  增加后台 添加超链接到/admin/
2.具体添加的是 target="_blank" 换页跳转
3.home.html 增加一个输入框，pei()  方法接口数据，想法存入数据库

---- 吐槽功能后台实现+orm初识
models层设计数据库字段
admins层，注册models数据
views层，进行写入数据，添加字段的信息
在home.html里面进行输入text吐槽内容，进行异步信息访问/pei/路径，由urls里面的路由，调用pei方法，存储数据库信息

第四天
代码实现17:帮助模块1
新增a标签，在通过help点击显示出来，并且嵌套到主页上面

在home主页，菜单不隐藏
if("{{whichHTML}}" != "home.html"){
            document.getElementById("menu_btn").click();
        }
在帮助页面，菜单自动隐藏


18.帮助页面2
实现script获取id，从div中来的，点击之后 --》可以发现我们点击不同左侧菜单，右侧就会迅速显示对应的解释文案～
a标签的设置方法，script设置的实现方法，有变量拼接，默认都不显示，只有点击固定，获取到固定的id，能够显示对应的说明
positon的固定位置，渐变颜色，竖线 /横线的设计。显示指定元素的js，鼠标放上元素的变化，元素id命名的小技巧

19.首页优化
本节课的内容主要是训练循环列表等显示效果，
目的是为了让我们接下来做项目列表/接口列表/用例列表 铺路。
那么就先要按照这个思路去思考：
-数据存在哪？我们存在数据库，那么就要去models.py中新建一个类作为数据库表
-前端的这堆数据展示在哪？我们是展示在home.html中c位
-增删改查这些数据去哪？我们去admin后台
-数据怎么传递给前端？我们后端进入home的哪个函数从数据库提取这些数据然后返回。

通过主页，显示，超链接的功能，将数据库中的信息展示到网页上，实现网页快速收藏的页面跳转
models层添加字段，admin注册字段，home.html嵌入到welocome页面中，(需要在对应的方法上，添加上字段，
对应的whichHTML这种字段只是用来匹配，提供下面使用的变量，不用管请求路径)
通过child--》load('/child/'  获取具体的页面信息，将从数据库中获取的数据，展示到这个页面上，
data = DB_home_href.objects.all();
因为 从数据库查出的数据默认是queryset格式，前端接受的是字典类型，所以res = {}自行写一个字典，处理后，在传入到
child方法中，统一返回



实现20: 首页完善和项目模块1
一个项目模块我们要考虑 都有哪些组成部分？
    1: 项目列表
    2：接口库
    3:  用例库
    4：项目设置

首先我们要先做一个 可以增删改查的 项目列表。所有用户的项目都展示。
我们再考虑项目列表的数据放在哪？当然是数据库。
    那么里面都应该有些什么字段呢？
    项目id,orm会自动加入，无需我们操心
    项目名称
    项目备注
    项目创建者
    项目其他管理员

实现21:项目列表
首先models.py 创建项目表
迁移完成，注册两个项目列表在后台

实现22： 项目列表前后端

// 问题   child_json  出现了问题，res需要初始，要不然下面的没有访问路径没有定义，则不能狗返回数据
先将数据都取出来，新建一个project_list.html  负责展示， url路由注册上
后端views写上，因为所有的展示都嵌套在welcome上面，所以return render(request,welcome.html,{whichHTML,oid参数传递})

通过使用bootstrap工具，加入table元素，使得project_list  被插件加载好，总插件放置的位置是welocome因为要控制全局
项目列表的展示，也需要能够进入项目或者删除项目

代码实现23:项目列表收尾
使用bootstrp在项目列表上增加btn的属性，添加颜色，并且增加一个新增项目的按钮


代码实现24:项目列表的删除功能实现
首先思路是，点击按钮，能够实现后台逻辑进行删除信息，页面刷新，项目删除
点击按钮，btn实现 ，但是具体要删除的信息，需要从有一个定位的信息，就是从fori里面取到id值，onclik方法，传入一个id的值
script中实现一个异步的链接，能够得到这个id值，驱动后台的delete_project路由，实现删除的方法，通过获取所有的数据库信息，并且过滤掉查询到
的信息，通过delete()方法将其删除， 
script脚本中，会自动判断，confim的结果是true还是false， 如果是false则忽略，true则向下执行，删除操作
ret  接受的是httpresponse，成功，就在前端，script中reload实现刷新


平台代码实现25:项目列表页的新增功能
这个弹层默认是隐藏的一个div，当点击新增按钮后，修改该弹层的隐藏属性为显示。当点击确定/取消按钮后，再把弹层的隐藏属性变为隐藏。
点确定的时候，会发送给后台一个异步请求，带着用户写的新项目名字。让后端新建一个项目。等返回成功后，项目列表页面刷新，用户即可看到新增的那个项目了。
<div id="add_project_div" style="width: 50%;backgrround-color:white;border:1px solid black;position: absolute;left:25%;top:30px;padding-left:10px;box-shadow;4px 4px 8px grey;border-radius:5px">
        <h3>项目名称:(最多100字)</h3>
        <input type="text" placeholder="请输入项目名字" style="width: 95%">
        <br><br>
        <button class="btn btn-danger" onclick="javascript:document.getElementById('add_project_div').style.display='none'">取消</button>
        <button class="btn btn-success">确定</button>
        <br><br>
    </div>

接下来就是要让这个新增项目功能真实生效。
我们先在底部加一个script标签，里面新建一个function函数，取名add_project()
新建了这个 add_project函数：
它要做三件事：
接收project_name
去项目表新建项目
返回给前端一个空证明已经成功完成
document.getElementById('project_name').value;  value 没有括号


代码实现26:项目详情页设计
本节我们要设计项目详情页。按照我们之前的设计，项目详情页至少要包括3个部分：
    接口库 ：难度 ***  （接口导入/调试）
    用例设置 ：难度 ***** （用接口库的接口组成各种用例/执行/报告/监控）
    项目设置 ：难度 * （项目名称/备注/其他管理者 等后续新增的属性修改）

  需求来了:
        通过项目列表页，点击按钮，进入接口库页面，接口库页面，展示的是 接口库--{{ 项目的名字 }}
    首先找到项目列表页面，的进入按钮，增加onclick进行跳转页面的编写，
    1----onclick="javascript:document.location.href='/apis/{{ i.id }}/'
    2----强制跳转的页面是/apis/{{ i.id }}  首先明确这是根据项目的id进行跳转，有条件的筛选
    3---对apis进行urls设置  url(r'^apis/(?P<id>.*)/$',open_apis)
    4---进行view方法，去把数据返回到前端 open_apis方法，想要得到这个id，需要在参数中，增加id
    5---定位页面，将数据返回到welocome中，render(request,"welcome.html",{"whichHTML":"P_apis.html","oid":从前端传回来的id值，}))
    6---因为通过child方法，去进行页面的总体设置，会调用child_json（没有进行对oid的处理），将oid加入两个方法中
    7---child_json得到oid，将project_name = Db_project.objects.filter(id=oid)[0].name
    8---返回res，将前端页面上的变量project_name 从 res中设置返回


代码实现27: 项目详情页的导航功能
    需求来了，想要在项目列表进入接口库，用例库，项目设置模块，将三个模块显示成，一个导航栏
导航栏的设计 bootstrrap
[comment]: <> (    <nav class="navbar navbar-default" role="navigation" style="position: absolute;top: 0px;left: 80px;width:-webkit-calc&#40;100% - 200px&#41;;z-index: 1">)
[comment]: <> (    <div class="container-fluid">)
[comment]: <> (    <div class="navbar-header">)
[comment]: <> (        <span style="font-size: xx-small" class="navbar-brand" >项目名称：{{ project_name.name }}</span>)
[comment]: <> (        <a class="navbar-brand" href="/project_list/">返回项目列表</a>)
[comment]: <> (    </div>)
[comment]: <> (    <div>)
[comment]: <> (        <ul class="nav navbar-nav">)
[comment]: <> (            <li class="active"><a href="/apis/{{ project_name.id }}/">接口库</a></li>)
[comment]: <> (            <li><a href="/cases/{{ project_name.id }}/">用例库</a></li>)
[comment]: <> (            <li><a href="/project_set/{{ project_name.id }}/">项目设置</a></li>)
[comment]: <> (        </ul>)
[comment]: <> (    </div>)
[comment]: <> (    </div>)
[comment]: <> (</nav>)
url路由，获取到id的值，然后通过open_apis,open_cases,open_project_set /id/
将页面，id值传入到welcome页面中，通过child方法，child_json方法，将从数据库得到的project整体返回，在
前端页面，使用project.name  和  project.id  做返回操作，（Db_project.objects.filter(id=oid)[0]--这里不在处理，）直接返回project.name 会导致前端无法得到project.id的值
如果出现1前端页面上，点击，不能置灰的标签，修改li标签下的active，顺势调整

代码实现28:子页面-项目设置
打开P_project_set.html：
这里我们准备先放三个设置点：
项目名称
项目备注
项目其他管理者
实现思路，通过点击保存按钮，将所有添加的信息，传入到路由，通过save_project_set方法，将字段信息保存到Db_project 的数据库中
在显示在前端页面上，
<button type="button" onclick="save()" style="margin-left: 15%;width: 70%" class="btn btn-primary btn-lg btn-block">保存</button>
    <script>
        function save() {
        var name = document.getElementById('name').value;
        var remark = document.getElementById('remark').value;
        var other_user = document.getElementById('other_user').value;
        $.get('/save_project_set/'+'{{ project_name.id }}',{
            'name':name,
            'remark':remark,
            'other_user':other_user,
        },function (ret) {
            alert('保存成功')
        })
    }
    </script>
-----------------------------------------------------------
def save_project_set(request,id):
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    DB_project.objects.filter(id=id).update(name=name,remark=remark,other_user=other_user)
    return HttpResponse('')

代码实现29:真正的三大核心模块概述
  只有三个功能 可以让这个django项目叫做接口测试平台：
接口调试 ------对标postman
自动化执行/监控 ---------对标jmeter或其他基础接口自动化项目
自动录入/自动生成用例 --------对标fiddler/charles
接口调试：
接口列表的增删改查
接口的调试弹层界面
接口调试界面对应的接口各个属性的输入和显示
接口调试界面真正发送请求
各种请求体编码格式的底层请求技术
公共变量-请求头header
公共变量-域名host
登陆态接口设置弹层
接口调试功能添加自动登陆态
接口的复制/备注
diy加密/解密算法功能开发
2.自动化监控/执行
测试用例列表的增删改查
测试用例具体步骤开发
测试用例步骤列表的增删改查
具体步骤的执行顺序设置
具体步骤的请求设置
具体步骤的重试次数设置
具体步骤的实际发出连续请求
具体步骤提取返回值
具体步骤断言返回值
具体步骤mock返回值
在线测试报告生成
word文档标准报告生成
监控模块的核心技术开发
监控技术融合进用例执行业务中
监控的分级报警措施
监控的历史报告功能开发
3.自动录入/自动生成用例 
解析接口文档技术
在线抓包技术
在线抓包模仿charles/fiddler界面
在线抓包接口导入接口库
在线抓包接口导入用例库
解析postman自动导入
接口异常值测试用例自动生成技术
异常值测试用例自动执行
异常值测试用例测试报告


代码实现30:接口库-接口列表