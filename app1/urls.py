from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.Register, name='Register'),
    path('login/', views.login, name="login"),
    path('admin_index/', views.admin_index, name="admin_index"),
    path('admindetail/', views.admindetail, name="admindetail"),
    path('userdetail/', views.userdetail, name="userdetail"),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
]
