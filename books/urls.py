from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('contact-us/', views.ContactView.as_view(), name='contact-us'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
]
