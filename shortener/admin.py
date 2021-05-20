from django.contrib import admin

from shortener.models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_url']
