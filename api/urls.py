from django.urls import path

from api import views

urlpatterns = [
    path("books/", views.BookCreateApiView.as_view()),
    path("authors/", views.GetAuthorView.as_view()),
    path("author/<int:id>/", views.GetAnAuthorView.as_view()),
    path("book/<int:id>/", views.BookView.as_view()),
    path('new_author/', views.CreateAuthorView.as_view()),
    path("new_book/", views.CreateBookView.as_view())
    # path("book/<int:id>/", views.book_detail),
    # path("author/", views.authors)
    # path('books/', views.BookListView.as_view())
]
