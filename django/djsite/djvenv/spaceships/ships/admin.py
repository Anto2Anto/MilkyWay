from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ShipsAdmin(admin.ModelAdmin):
        list_display = ('id', 'title', 'get_html_photo', 'time_create', 'time_update', 'is_published')
        list_display_links = ('id', 'title')
        search_fields = ('title', 'content')
        list_editable = ('is_published',)
        list_filter = ('is_published', 'photo', 'time_create')
        prepopulated_fields = {'slug': ('title',)}
        fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published')
        readonly_fields = ('time_create', 'time_update', 'get_html_photo')
        save_on_top = False

        def get_html_photo(self, object):
                if object.photo:
                        return mark_safe(f"<img src='{object.photo.url}' width=50>")

        get_html_photo.short_description = 'Picture'


class CategoryAdmin(admin.ModelAdmin):
        list_display = ('id', 'name')
        list_display_links = ('id', 'name')
        search_fields = ('name',)
        prepopulated_fields = {'slug': ('name',)}


admin.site.register(ships, ShipsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'MilkyWay administration'
admin.site.site_header = 'MilkyWay administration'
