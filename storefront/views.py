from django.views import generic

class HomepageTemplateView(generic.TemplateView):
    template_name = 'pages/home.html'