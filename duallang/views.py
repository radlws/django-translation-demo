
from django.views.generic import ListView

from models import FAQTopic


landing = ListView.as_view(template_name='dual_lang/landing.html',
    model=FAQTopic, context_object_name='topic_list')


# if request.LANGUAGE_CODE == 'de-at':
#    return HttpResponse("You prefer to read Austrian German.")
# else:
#    return HttpResponse("You prefer to read another language.")
