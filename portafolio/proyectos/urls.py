from django.urls import path
from .views import index,ProjectCreateView,ProjectListView,ProjectUpdateView,ProjectDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("create",ProjectCreateView.as_view(),name="create_project"),
    path("portfolio", ProjectListView.as_view(), name="portfolio"),
    path("<pk>/update", ProjectUpdateView.as_view(), name="update_project"),
    path("<pk>/delete", ProjectDeleteView.as_view(), name="delete_project"),
    
]
