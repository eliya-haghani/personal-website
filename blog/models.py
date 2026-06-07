from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User 
class Category(models.Model):
     name = models.CharField(max_length=255)

     def __str__(self):
        return self.name

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Content", config_name="default")
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publishd_date = models.DateTimeField(null=True)
    crated_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="متا تایتل")
    meta_description = models.TextField(blank=True, null=True, verbose_name="متا دیسکریپشن")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog/')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
