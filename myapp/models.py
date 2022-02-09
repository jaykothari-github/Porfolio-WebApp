from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/',null=True,blank=True)
    des = models.TextField()
    tech = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title