from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView,DeleteView
from django.views import View
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, template_name="index.html")


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = "./create.html"
    fields = ["title", "tags", "photo_url", "github_url", "description"]

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect("portfolio")
        else:
            print("EROOR FORM")
            return self.form_invalid(form)


class ProjectListView(ListView):
    model = Project
    template_name = "./portfolio.html"

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = "update_project.html"
    fields = ["title", "tags", "photo_url", "github_url", "description"]
    success_url = reverse_lazy('portfolio')

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = "delete_project.html"
    success_url = reverse_lazy('portfolio')



