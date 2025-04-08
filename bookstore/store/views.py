from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    cart.append(book_id)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def cart(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    request.session['prev_page'] = request.META.get('HTTP_REFERER')
    return render(request, 'store/cart.html', {'books': books})

@login_required
def go_back(request):
    return redirect(request.session.get('prev_page', '/'))
