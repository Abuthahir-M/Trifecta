from django.urls import path
from . import views

app_name = 'expensemanager'
urlpatterns = [
    path('expense-home/', views.expenseHome, name='expense-home')
]