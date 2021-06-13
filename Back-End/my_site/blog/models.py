from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Tag(models.Model):
    caption =models.CharField(max_length=20)
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique =True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True, related_name= "posts")
    tags =models.ManyToManyField(Tag)
