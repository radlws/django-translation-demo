from django.urls import path, re_path
from home.views import landing

urlpatterns = [
    re_path(r'^$', landing, name='home'),
]
