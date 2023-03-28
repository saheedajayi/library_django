from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from api import views

# router = SimpleRouter()
router = DefaultRouter()
router.register("authors", views.AuthorViewSet)
router.register("books", views.BookViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("books/", views.BookCreateApiView.as_view()),
    path("authors/", views.GetAuthorView.as_view()),
    path("author/<int:id>/", views.GetAnAuthorView.as_view()),
    path("book/<int:id>/", views.BookView.as_view()),
    path('new_author/', views.CreateAuthorView.as_view()),
    path("new_book/", views.CreateBookView.as_view()),
    path("delete_book/<int:id>", views.DeleteBookView.as_view()),
    path("authors/<int:id>/", views.author_detail, name="author-detail")
    # path("book/<int:id>/", views.book_detail),
    # path("author/", views.authors)
    # path('books/', views.BookListView.as_view())
]
