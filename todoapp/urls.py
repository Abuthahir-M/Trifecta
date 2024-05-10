from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register' ),
    path('login/', views.loginPage, name='login-page'),
    path('logout/', views.logoutUser, name='logout'),
    path('delete-task/<str:name>/', views.deleteTask, name='delete-task'),
    path('update-status/<str:name>/', views.updateStatus, name='update-status'),
]