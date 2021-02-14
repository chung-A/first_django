from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.select, name="list"),
    path('create/', views.create, name="create"),
    path('update/', views.update, name="update"),
    path('delete/', views.delete, name="delete"),

    # path('detail/', views.detail, name="detail"),
    path('restaurant/<int:id>', views.detail, name="detail"),
    path('restaurant/<int:restaurant_id>/review/create', views.review_create, name="review-create"),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name="review-delete"),
    path('review/list/', views.review_list, name="review-list")
]
