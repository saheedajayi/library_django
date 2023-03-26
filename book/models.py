from uuid import uuid4

from django.db import models


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False, default="2000-01-01")
    date_of_death = models.DateField(blank=False, null=False, default="2000-01-01")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    description = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="author")
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, related_name="genre")
    language = models.ForeignKey("Language", on_delete=models.CASCADE, related_name="languages")

    def __str__(self):
        return self.title


class Genre(models.Model):
    GENRE_CHOICES = [
        ("FICTION", "FIC"),
        ("ROMANCE", "ROM"),
        ("COMEDY", "COM"),
        ("DRAMA", "DRA")
    ]

    name = models.CharField(max_length=8, choices=GENRE_CHOICES, default="FIC")

    def __str__(self):
        return self.name


class Language(models.Model):
    LANG_CHOICES = [
        ("ENGLISH", "ENG"),
        ("YORUBA", "Y0R"),
        ("IGBO", "IGB"),
        ("HAUSA", "HAU"),
        ("PIDGIN", "PID")
    ]
    name = models.CharField(max_length=7, choices=LANG_CHOICES, default="ENG")

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ("AVAILABLE", "A"),
        ("BORROWED", "B")
    ]
    unique_id = models.UUIDField(default=uuid4)
    due_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="A")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="book")
    imprint = models.CharField(max_length=55)

    def __str__(self):
        return self.imprint
