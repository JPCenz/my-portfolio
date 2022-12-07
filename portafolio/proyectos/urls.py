from django.urls import path
from .views import index,ProjectCreateView

urlpatterns = [
    path("", index, name="index"),
    path("create",ProjectCreateView.as_view(),name="create_project")
    
]
