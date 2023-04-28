from django.views.generic import TemplateView
from articles.models import Article


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data()
        home_news = Article.objects.all()[0:8]
        context["object_list"] = home_news
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'
