from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views import View
from .models import Project

def index(request):
    return render(request,template_name="index.html")

class ProjectCreateView(CreateView):
    model = Project
    template_name = "./create.html"
    fields= ["title","tags","photo_url","github_url"]
