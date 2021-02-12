from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import PostRestFul

urlpatterns = [
    path('list/', views.select, name="list"),
    path('create/', views.create, name="create"),
    path('confirm/', views.confirm, name="confirm"),
]


post_list = PostRestFul.as_view({
    'post': 'create',
    'get': 'list',
})

post_detail = PostRestFul.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# urlpatterns = format_suffix_patterns([
#     path('auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('posts/', post_list, name='post_list'),
#     path('posts/<int:pk>/', post_detail, name='post_detail'),
# ])

# query parameter, path variable
