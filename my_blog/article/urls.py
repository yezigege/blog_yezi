from django.urls import path  # 引入 path
from . import views


app_name = 'article'  # 正在部署的应用的名称


# 此 app 对应的 url 路径
urlpatterns = [
    # path 函数将 url 映射到视图
    path('article-list/', views.article_list, name='article-list'),
]
