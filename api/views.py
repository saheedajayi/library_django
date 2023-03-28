from django.shortcuts import render
from django.views.generic import DeleteView
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.models import Book, Author
from .pagination import DefaultPageNumberPagination
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, CreateAuthorSerializer, \
    CreateBookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view


# Create your views here.

# @api_view(["GET", "POST"])
# def book_list(request):
#     if request.method == "GET":
#         queryset = Book.objects.all()
#         serializers = BookSerializer(queryset, many=True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         book = BookCreateSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("book saved successfully")
#
#
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def book_detail(request, id):
#     if request.method == "GET":
#         book = get_object_or_404(Book, pk=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def authors(request):
#     if request.method == "GET":
#         queryset = Author.objects.all()
#         serializers = AuthorSerializer(queryset, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

class AuthorViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer


class GetAuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GetAnAuthorView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "id"


class BookView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


class CreateAuthorView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = CreateAuthorSerializer


class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer


class DeleteBookView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    # def delete(self, request, *args, **kwargs):
    #     book_id = kwargs['id']
    #     try:
    #         book = Book.objects.get(id=book_id)
    #     except Book.DoesNotExist:
    #         return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    #     book.delete()
    #     return Response({'detail': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)
