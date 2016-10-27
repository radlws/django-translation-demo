from django.conf.urls import url

from views import landing

urlpatterns = [
    # 'home.views',
    url(r'^$', landing, name='home'),
]
