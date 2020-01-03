"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 引入 include


"""
存放映射关系的列表

path为Django的路由语法：

参数article/分配了app的访问路径；
include将路径分发给下一步处理；
namespace可以保证反查到唯一的url，即使不同的app使用了相同的url（后面会用到）。
"""
urlpatterns = [
    path('admin/', admin.site.urls),

    # 自定义的路径
    path('article/', include('article.urls', namespace='article'))
]
