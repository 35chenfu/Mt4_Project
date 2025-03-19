
from django.urls import re_path, include
from .views import *


urlpatterns = [
    re_path(r'^add_book$', add_book, name='add_book'),
    re_path(r'^show_books$', show_books, name='show_books')
]