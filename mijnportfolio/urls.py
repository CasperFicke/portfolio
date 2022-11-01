# mijnportflio/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "mijnportfolio"

urlpatterns = [
	path("", views.PortfolioView.as_view(), name="portfolio"),
]