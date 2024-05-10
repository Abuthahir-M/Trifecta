from django.shortcuts import render

# Create your views here.

def expenseHome(request):
    return render(request, 'expensemanager/expense-home.html')