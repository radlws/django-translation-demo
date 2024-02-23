from django.views.generic import ListView

from duallang.models import FAQTopic


# landing = ListView.as_view(template_name='dual_lang/landing.html',
#                            model=FAQTopic,
#                            context_object_name='topic_list')

class FAQTopicListView(ListView):
    model = FAQTopic
    template_name = 'dual_lang/landing.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

landing = FAQTopicListView.as_view()