from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListCreateAPIView.as_view()),
    path('<str:name>', views.BookDetailedAPIView.as_view()),
    path('', views.BookEditAPIView.as_view())
]