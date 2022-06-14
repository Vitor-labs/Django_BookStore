# Django Libs:
from django.contrib import admin
# Local Libs:
from .models import Book


class CustomBook(admin.ModelAdmin):
	"""Allow to edit Book informations"""
	# list_display = ('', )
	fieldsets = [
		('title', {'fields': ['title']}),
		('author', {'fields': ['author']}),
		('summary', {'fields': ['summary']}),
		('pages', {'fields': ['pages']}),
		('rating', {'fields': ['rating']}),
		('price', {'fields': ['price']}),
		('isbn', {'fields': ['isbn']}),
		('publisher', {'fields': ['publisher']}),
		('pub_date', {'fields': ['pub_date']}),
		('cover', {'fields': ['cover']}),
		('genre', {'fields': ['genre']}),
	]


admin.site.register(Book, CustomBook)
