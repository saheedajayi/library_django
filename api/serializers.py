from rest_framework import serializers
from book.models import Book, Author


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "isbn", "description"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name"]


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "date_of_birth", "date_of_death"]


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        # fields = ["id", "title", "isbn", "description"]
        fields = ["id", "title", "description", "author"]


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "isbn", "description", "author"]

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#
#     class Meta:
#         model = Book
#         fields = ["id", "title", "description", "author"]


# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
# discount_price = serializers.SerializerMethodField(method_name="")
#
# def get_discount(self):
#     return self.price - 20
