from django.urls import path  # 引入 path
from . import views

app_name = 'article'  # 正在部署的应用的名称


# 此 app 对应的 url 路径
urlpatterns = [
    # path 函数将 url 映射到视图
    path('article_list/', views.article_list, name='article_list'),
    # 文章详情
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
]
