from django.urls import path
from .views import RegistrationView
from .views import BookListView
from .views import LoginView, LogoutView
from .views import AddToCartView, CartView,HomeView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('book_list/', BookListView.as_view(), name='bookList'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('', HomeView.as_view(), name='home'),
]