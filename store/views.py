from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Book

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

class LoginView(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'}) 


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        books = Book.objects.all()
        cart = request.session.get('cart', [])
        return render(request, 'store/home.html', {
            'books': books,
            'cart_count': len(cart)
        })

class BookListView(ListView):
    model = Book
    template_name = 'store/book_list.html'
    context_object_name = 'books'

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', [])
        books_in_cart = Book.objects.filter(id__in=cart)
        return render(request, 'store/cart.html', {'books': books_in_cart})

class AddToCartView(View):
    def get(self, request, book_id):
        cart = request.session.get('cart', [])
        cart.append(book_id)
        request.session['cart'] = cart
        return redirect('cart')
