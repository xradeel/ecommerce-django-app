from django.shortcuts import render

def account(request):
    return render(request, 'user/account.html')

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')
