"""my_server URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from restApi.views import UserViewSet, PostViewSet, CommentViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)

schema_view = get_swagger_view(title="게시판 API")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url('swagger/', schema_view)
]