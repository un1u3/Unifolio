from django.contrib import admin
from .models import Author, Skills, Experience, Education, Technology, Project, Link, Crausel

# Register your models here.
admin.site.register(Author)
admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Link)
admin.site.register(Crausel)
