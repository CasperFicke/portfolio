# blog/views.py

from django.shortcuts import render
from django.views import generic

# home view
# classbased view 
class BlogIndexView(generic.TemplateView):
	"""
    Website home page.

    **Template:**

    :template:`blog/blog.html`
    """
	template_name = "blog/blog.html"


