from django.db import models
from accounts.models import User
from django.core.files.storage import default_storage

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)

    like_users = models.ManyToManyField(User, related_name="like_articles")

    def __str__(self):
        return self.title
    
    def delete(self):
        if self.image:
            default_storage.delete(self.image.path)
        super(Product, self).delete(using=None, keep_parents=False)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
