from django.urls import path, re_path
from django.utils.translation import gettext_lazy as _
from duallang.views import landing

urlpatterns = [
    re_path(_(r'^dual_language/$'), landing, name='duallang_landing'),
]
