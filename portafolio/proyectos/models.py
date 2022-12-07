from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    photo_url= models.CharField(max_length=300)
    tags = models.CharField(max_length=20)
    github_url = models.CharField(max_length=300)



