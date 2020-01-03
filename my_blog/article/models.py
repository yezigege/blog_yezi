from django.db import models
from django.contrib.auth.models import User  # 导入 django 自带的 User 模型
from django.utils import timezone  # timezone 用于处理时间相关的事务


# 博客文章数据模型
class ArticlePost(models.Model):
    """
    使用 ForeignKey定义一个关系。这将告诉 Django，每个（或多个） ArticlePost 对象都关联到一个 User 对象。
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者。 on_delete 用于指定数据删除方式
    title = models.CharField(max_length=100)  # 标题。models.CharField 为字符串字段，用于保存较短的字符串
    body = models.TextField()  # 正文。保存大量文本使用 TextField
    created = models.DateTimeField(default=timezone.now)  # 文章创建时间。timezone.now 指定其在创建时写入当前的时间
    updated = models.DateTimeField(auto_now=True)  # 文章更新时间。auto_now=True 指定每次数据更新时自动写入当前时间

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        db_table = "articles"  # 指定数据库表名
        verbose_name = '文章'  # 在后台 admin 站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
        ordering = ('-created',)  # ordering 指定模型返回数据的排列顺序。 '-created' 表名数据应该以创建时间 倒序 排列

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        """
        __str__方法定义了需要表示数据时应该显示的名称。
        给模型增加 __str__方法是很重要的，
        它最常见的就是在Django管理后台中做为对象的显示值。
        因此应该总是返回一个友好易读的字符串
        """
        return self.title   # return self.title 将文章的标题返回
