from django.db import models 
class Post(models.model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title