from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.CharField(max_length=300)
    tags = models.CharField(max_length=100)
    github_url = models.CharField(max_length=300)
