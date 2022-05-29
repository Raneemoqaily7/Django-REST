from rest_framework import generics
from .serializers import BookSerializers
from bookss.models import Book


class BooksListAPIView(generics.ListAPIView):
    
        queryset = Book.objects.all()
        serializer_class =BookSerializers



class BookDetailAPIView(generics.RetrieveAPIView):
    
        queryset = Book.objects.all()
        serializer_class =BookSerializers

class BookDeleteAPIView(generics.RetrieveDestroyAPIView):
    
        queryset = Book.objects.all()
        serializer_class =BookSerializers


