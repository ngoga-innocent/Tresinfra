from django.contrib import admin
from .models import Carousel,OurService,Achievement,Blog,Team,MisconductReport
# Register your models here.
admin.site.register(Carousel)
admin.site.register(OurService)
admin.site.register(Achievement)
admin.site.register(Team)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'slug')
    prepopulated_fields = {'slug': ('title',)}  
@admin.register(MisconductReport)
class MisconductReportAdmin(admin.ModelAdmin):
    list_display = ('anonymous', 'names', 'email', 'phone_number', 'country', 'city', 'submitted_at')
