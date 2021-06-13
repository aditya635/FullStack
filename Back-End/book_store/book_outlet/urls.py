from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:booki>", views.book_detail, name = "book-detail")
]
