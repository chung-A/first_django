from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.select, name="list"),
    path('create/', views.create, name="create"),
    path('update/', views.update, name="update"),
    path('detail/', views.detail, name="detail"),
    path('delete/', views.delete, name="delete"),
]
