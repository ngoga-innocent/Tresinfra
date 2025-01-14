from django.db import models
import uuid
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Carousel(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    image=models.ImageField(upload_to='Homecarousel/')
    title=models.TextField(blank=True,null=True)
    subtitle=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.id)
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
     