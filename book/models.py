from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = '')
    def __str__(self):
        return self.name