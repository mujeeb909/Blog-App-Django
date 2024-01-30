from django.db import models


  
class Category(models.Model):
  title = models.CharField(max_length=25)
  

  def __str__(self):
    return self.title

class Blog(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField()
  body = models.TextField()
  thumbnail = models.ImageField(upload_to="img")
  created = models.DateField(auto_now_add = True)
  updated = models.DateField(auto_now = True)
  featured = models.BooleanField(default=False)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True ,default=None)

  def __str__(self):
    return self.title


