from django.db import models
import uuid
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
# Create your models here.
class Carousel(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    image=models.ImageField(upload_to='Homecarousel/')
    video = CloudinaryField(
    'media',
    resource_type='auto',  # This is key: it auto-detects image or video
    blank=True,
    null=True
)
    title=models.TextField(blank=True,null=True)
    subtitle=models.TextField(blank=True,null=True)
    order=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.id)
    class Meta:
        ordering = ['order','created_at']
class OurService(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    image=models.ImageField(upload_to='Service/')
    title=models.CharField(max_length=200)
    subtitle=models.TextField() 
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
         return self.title  
class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="achievements/")
    category = models.CharField(max_length=100, choices=[
        ("recognition", "Recognition"),
        ("project", "Project"),
        ("material_supply", "Material Supply"),
    ])

    def __str__(self):
        return self.title   
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description =  RichTextUploadingField()
    image = models.ImageField(upload_to='blog_images/')
    tags = models.JSONField(default=list)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title        
class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')
    position = models.CharField(max_length=200)
    other_position=models.CharField(max_length=200,null=True,blank=True)
    board_member=models.BooleanField(default=False)
    management_team=models.BooleanField(default=False)
    linkedin=models.URLField(null=True,blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    def save(self, *args, **kwargs):
        if not self.order:  # Only assign if `order` is not set
            last_order = Team.objects.aggregate(max_order=models.Max('order'))['max_order']
            self.order = (last_order + 1) if last_order is not None else 1
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
class MisconductReport(models.Model):
    anonymous = models.BooleanField(default=False)
    names=models.CharField(null=True,blank=True,max_length=255)
    email = models.EmailField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    case_details = models.TextField()
    evidence = models.FileField(upload_to="evidence/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report from {self.city}, {self.country} (Anonymous: {self.anonymous})"
    