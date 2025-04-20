from django.views import View
from django.shortcuts import render, redirect
from books.models import Book

class CartAddView(View):
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        cart = request.session.get('cart', {})
        
        if str(book_id) in cart:
            cart[str(book_id)] += 1
        else:
            cart[str(book_id)] = 1
        
        request.session['cart'] = cart
        return redirect('book-list')

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = []
        total = 0
        
        for book_id, quantity in cart.items():
            book = Book.objects.get(id=book_id)
            books.append({
                'book': book,
                'quantity': quantity,
                'subtotal': book.price * quantity
            })
            total += book.price * quantity
        
        return render(request, 'cart/cart.html', {'books': books, 'total': total})