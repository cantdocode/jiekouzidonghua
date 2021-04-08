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

