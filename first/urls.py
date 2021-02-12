from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('select/', views.select, name="select"),
    path('view/<int:id>', views.select, name="view"),
    path('result/', views.result, name="result"),

    # 정규식 사용하여 url 을 만들수 있음
    # re_path('')
]

# query parameter, path variable
