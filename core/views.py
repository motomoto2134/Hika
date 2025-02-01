from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        if password != repeat_password:
            return render(request, 'core/sign_up.html',{
                'error':'пароли не совпадают'
            })
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('sign_in')
    return render(request, 'core/sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')
        else:
            return render(request, 'core/sign_in.html',{
                'error':'нет пользователя'
            } )
    return render(request, 'core/sign_in.html' )