from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Scale, Translation


class ScaleForm(forms.ModelForm):
    class Meta:
        model = Scale
        fields = ('width', 'height',)
        labels = {
            'width': _('Width'),
            'height': _('Height'),
        }


class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ('xoffset', 'yoffset',)
        labels = {
            'xoffset': _('X Offset'),
            'yoffset': _('Y Offset'),
        }
