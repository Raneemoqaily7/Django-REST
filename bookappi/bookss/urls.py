from django.urls import path
from bookss.api.viewset import BooksListAPIView ,BookDetailAPIView

urlpatterns=[
    path('api/v1/books-list' ,BooksListAPIView.as_view(), name = 'books_list'),
    path('api/v1/<int:pk>' ,BookDetailAPIView.as_view(), name = 'book_detail')
]