from rest_framework import serializers
from book.models import Book, Author
from djoser.serializers import UserCreateSerializer


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

    date_of_birth = serializers.DateTimeField(read_only=True)
    date_of_death = serializers.DateTimeField(read_only=True)


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ["id", "title", "description", "author", "price", "discount_price", "date_added"]

        author = serializers.HyperlinkedRelatedField(
            queryset=Author.objects.all(),
            view_name="author-detail",
        )
    date_added = serializers.DateTimeField(read_only=True)
    discount_price = serializers.SerializerMethodField(method_name="discount")

    def discount(self, book: Book):
        return book.price * 25 / 100


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "isbn", "description", "author", "genre", "price", "discount_price", "language"]


class CreateLibraryUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id", "username", "email", "password", "first_name", "last_name"]

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
