from django.db import models
from accounts.models import User
from django.core.files.storage import default_storage


class CommonInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Hashtag(models.Model):
    tag = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.tag


class Product(CommonInfo):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    views = models.IntegerField(default=0)
    like_users = models.ManyToManyField(User, related_name="like_products")
    tags = models.ManyToManyField(Hashtag, blank=True, related_name="tags")

    def __str__(self):
        return self.title
    
    def delete(self):
        if self.image:
            default_storage.delete(self.image.path)
        super(Product, self).delete(using=None, keep_parents=False)


class Comment(CommonInfo):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


