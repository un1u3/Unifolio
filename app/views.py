# views.py
from django.views.generic import TemplateView
from .models import Author, Skills, Experience, Education, Technology, Project, Link

class HomePageView(TemplateView):
    template_name = 'app/home.html'  
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['skills'] = Skills.objects.all()
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['technologies'] = Technology.objects.all()
        context['projects'] = Project.objects.all()
        context['links'] = Link.objects.all()
        return context
