# mijnportfolio/views.py

from django.shortcuts import render
from django.views import generic

# portfolio view
# classbased view 
class PortfolioView(generic.TemplateView):
	"""
    Website portfolio page.

    **Template:**

    :template:`mijnportfolio/portfolio.html`
    """
	template_name = "mijnportfolio/portfolio.html"
