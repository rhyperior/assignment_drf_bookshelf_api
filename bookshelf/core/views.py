from rest_framework import generics

from .models import Bookshelf
from .serializers import BookSerializer

# Create your views here.
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookSerializer

class BookDetailedAPIView(generics.RetrieveAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'name'
    
class BookEditAPIView(generics.UpdateAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookSerializer
    

