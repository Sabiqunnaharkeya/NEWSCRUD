from django.db import models

# Create your models here.

class newsinfo(models.Model):
    title = models.CharField(max_length=288)
    news_details = models.TextField()
    cover_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title
    

    


