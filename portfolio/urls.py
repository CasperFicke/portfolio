# portfolio/urls.py

# django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('site_basis.urls', namespace="site-basis")),
  path('', include('mijnportfolio.urls', namespace="mijnportfolio")),
  path('', include('blog.urls', namespace="blog")),
  # debug urls
  #path("__debug__", include('debug_toolbar.urls')),
]
