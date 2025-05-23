from django.contrib import admin
from .models import Carousel,OurService,Achievement,Blog,Team,MisconductReport,Achievement
# Register your models here.
# admin.site.register(Carousel)
admin.site.register(OurService)
# admin.site.register(Achievement)
# admin.site.register(Team)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'slug')
    prepopulated_fields = {'slug': ('title',)}  
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display=('title','category')
    list_filter=('title','category')
@admin.register(MisconductReport)
class MisconductReportAdmin(admin.ModelAdmin):
    list_display = ('anonymous', 'names', 'email', 'phone_number', 'country', 'city', 'submitted_at')
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'created_at')
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'board_member', 'management_team')
