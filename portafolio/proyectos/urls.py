from django.urls import path
from .views import index,ProjectCreateView,ProjectListView

urlpatterns = [
    path("", index, name="index"),
    path("create",ProjectCreateView.as_view(),name="create_project"),
    path("portfolio", ProjectListView.as_view(), name="portfolio"),
    
]
