from .views import RegistrationView
from .views import BookListView
from .views import LoginView, LogoutView

urlpatterns += [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', BookListView.as_view(), name='home'),
]