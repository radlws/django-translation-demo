from django.db import models
from django.utils.translation import gettext_lazy as _


from django.db import models


class HomeCarousel(models.Model):


    def __unicode__(self):
        return 'Home Carousel'


class HomeSlide(models.Model):

    carousel = models.ForeignKey(HomeCarousel, on_delete=models.CASCADE)
    label = models.CharField(max_length=255, unique=True)
    text = models.TextField()


class FAQTopic(models.Model):

    name = models.CharField(_('name'), max_length=255, unique=True, help_text=_("Name of the FAQ Topic"))
    slug = models.SlugField(_('slug'))
    text = models.TextField(_('text field test'), help_text=_("This is a help text"))


    class Meta:
        verbose_name = _('faq topic')
        verbose_name_plural = _('faq topics')

    def __unicode__(self):
        return self.name