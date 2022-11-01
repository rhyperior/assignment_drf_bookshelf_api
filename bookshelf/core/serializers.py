from rest_framework import serializers

from .models import Bookshelf

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookshelf
        fields = [
            'name',
            'author',
            'isbn_number',
            'publication',
            'genre',
        ]