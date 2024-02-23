
from django import forms
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib import admin

from duallang.models import FAQTopic
from duallang.models import HomeCarousel, HomeSlide


admin.site.register(FAQTopic)

class HomeSlideFormSet(BaseInlineFormSet):
    """
    Validate formset data here
    """
    def clean(self):
        super(HomeSlideFormSet, self).clean()

        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            data = form.cleaned_data


class HomeSlideAdmin(admin.TabularInline):
    model = HomeSlide
    formset = HomeSlideFormSet

class HomeCarouselAdmin(admin.ModelAdmin):
    inlines = (HomeSlideAdmin,)

admin.site.register(HomeCarousel, HomeCarouselAdmin)