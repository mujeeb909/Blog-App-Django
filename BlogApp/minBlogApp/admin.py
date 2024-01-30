from django.contrib import admin
from django.utils.html import format_html
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'category', 'featured', 'thumbnail_preview',)
  prepopulated_fields = {'slug': ('title', )}

  def thumbnail_preview(self, obj):
    if obj.thumbnail:
      return format_html('<img src="{}" width="70" height="70" />', obj.thumbnail.url)
    else:
      return 'No Image'
  thumbnail_preview.short_description = 'Thumbnail Preview'

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

