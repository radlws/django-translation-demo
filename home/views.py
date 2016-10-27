from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/landing.html'

landing = HomeView.as_view()
