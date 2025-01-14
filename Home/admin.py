from django.contrib import admin
from .models import Carousel,OurService,Achievement,Blog
# Register your models here.
admin.site.register(Carousel)
admin.site.register(OurService)
admin.site.register(Achievement)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'slug')
    prepopulated_fields = {'slug': ('title',)}  # Automatically fills the slug field based on the title
