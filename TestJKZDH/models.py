from django.db import models

# Create your models here.

class DB_tucao(models.Model):
    user = models.CharField(max_length=30,null=True) # 吐槽人名字
    text = models.CharField(max_length=1000,null=True) #内容
    ctime = models.DateTimeField(auto_now=True) #时间

    def __str__(self):
        return self.text+str(self.ctime)
    # 类下面我们要写什么呢？我们要写类变量 。类变量会被orm当作是表内的字段。那么吐槽内容都有些什么字段呢？
    # 1.id任何表的id都不需要我们亲自写，都是自动生成并且自增主键不唯一
    # 2.user吐槽人的名字
    # 3.吐槽内容
    # 4.吐槽时间

class DB_home_href(models.Model):
    name = models.CharField(max_length=300,null=True) # 超链接的名字
    href = models.CharField(max_length=2000,null=True) # 超链接

    def __str__(self):
            return self.name



