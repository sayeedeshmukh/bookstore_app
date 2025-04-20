from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

class RegistrationView(View):
    def get(self, request):
        return render(request, 'store/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'store/register.html', {'error': 'All fields are required'})

        if User.objects.filter(username=username).exists():
            return render(request, 'store/register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')