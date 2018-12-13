from rest_framework import serializers
#from rest_framework import Book
from .models import Book
class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'