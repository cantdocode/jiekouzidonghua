from django.contrib import admin

# Register your models here.
# 类下面我们要写什么呢？我们要写类变量 。类变量会被orm当作是表内的字段。那么吐槽内容都有些什么字段呢？
#     1.id 任何表的id都不需要我们亲自写，都是自动生成并且自增 主键不唯一
#     2.user 吐槽人的名字
#     3.吐槽内容
#     4.吐槽时间

from TestJKZDH.models import *
# 然后我们进行注册
# 刚刚的吐槽表：
admin.site.register(DB_tucao)
# admin.site.register() 是注册用的函数，里面写类名，注意是类名，并不是类本身，所以不要加()
# 注册后同步 makemigrations migrate
admin.site.register(DB_home_href)
admin.site.register(DB_project)
admin.site.register(DB_apis)