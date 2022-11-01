# mijnportfolio/admin.py

# django
from django.contrib import admin

# local
from .models import (
  Skill,
  UserProfile,
  ContactProfile,
  Testimonial,
  Media,
  Portfolio,
  Certificate
  )

class SkillAdmin(admin.ModelAdmin):
  list_display = ('name', 'score',)
  ordering     = ('name',)
  list_filter  = ('name',)

admin.site.register(Skill, SkillAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
  list_display = ('id','name','is_active')
  readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
  list_display = ('id','name')
