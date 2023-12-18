from django.contrib import admin
from .models import UserProfile
from django.contrib import admin
from .models import Department, Course, Information, Material
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Information)
admin.site.register(Material)