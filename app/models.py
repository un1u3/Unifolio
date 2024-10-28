from django.db import models

# Create your models here.
class Crausel(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='profile_pictures/')
    typewritter = models.ManyToManyField(Crausel)
    about_author = models.TextField()
    
    def __str__(self):
        return self.name
    

    

class Skills(models.Model):
    skill = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)
        
    def __str__(self):
        return self.skill
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4, blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_year', '-end_year']  

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4, blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_year', '-end_year']  

    def __str__(self):
        return f"{self.position} at {self.company}"


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    techstack = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=50,blank='True')
    class_field = models.CharField(max_length=60,blank='True')
    link = models.URLField(max_length=200,blank='True')
    
    def __str__(self):
        return self.title
    