from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured_pic = models.ImageField(upload_to='featured_pics/', blank=True, null=True)

    def __str__(self):
        return self.title



class Contact(models.Model):
    subject =models.CharField(max_length=100)
    email =models.EmailField()
    sender =models.CharField(max_length=80)
    detail =models.TextField()


