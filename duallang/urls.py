from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from views import landing

urlpatterns = [
    # 'faq.views',
    url(_(r'^dual_language/$'), landing, name='duallang_landing'),
]
