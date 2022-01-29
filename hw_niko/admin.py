from django.contrib import admin

from .models import Author, Quote


class QuoteInlineModelAdmin(admin.TabularInline):
    model = Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth']
    fields = ['name', 'date_of_birth', 'biography']
    inlines = [QuoteInlineModelAdmin]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text_quota', 'author']
    fields = ['text_quota', 'author']
