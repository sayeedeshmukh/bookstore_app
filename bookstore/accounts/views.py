from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, "Passwords don't match!")
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('book-list')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('book-list')
        else:
            messages.error(request, "Wrong username or password!")
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')