# blog/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "blog"

urlpatterns = [
	path("", views.BlogIndexView.as_view(), name="blog-index"),
]