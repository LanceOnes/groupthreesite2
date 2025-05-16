from django.urls import path 
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('layout/login/', views.login_view, name="login"),
    path('gender/list', views.gender_list),
    path('gender/add', views.add_gender),
    path('gender/edit/<int:genderId>', views.edit_gender),
    path('gender/delete/<int:genderId>', views.delete_gender),
    path('user/list', views.user_list, name='user_list'),
    path('user/add', views.add_user),
    path('user/edit/<int:user_id>/', views.edit_user),  
    path('user/delete/<int:user_id>/', views.delete_user),
    path('logout/', views.logout_view, name="logout"),
    path('user/change_password/<int:user_id>/', views.change_password, name='change_password')
]
