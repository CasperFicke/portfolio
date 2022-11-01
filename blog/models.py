# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Blog model
class Blog(models.Model):
  class Meta:
    verbose_name        = 'Blog'
    verbose_name_plural = 'Blog Profiles'
    ordering            = ["timestamp"]

  name        = models.CharField(max_length=200, blank=True, null=True)
  description = models.CharField(max_length=500, blank=True, null=True)
  body        = RichTextField(blank=True, null=True)
  image       = models.ImageField(blank=True, null=True, upload_to="blog")
  author      = models.CharField(max_length=200, blank=True, null=True)
  timestamp   = models.DateTimeField(auto_now_add=True)
  slug        = models.SlugField(null=True, blank=True)
  is_active   = models.BooleanField(default=True)

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.name)
    super(Blog, self).save(*args, **kwargs)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f"/blog/{self.slug}"