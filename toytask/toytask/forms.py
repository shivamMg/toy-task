from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import (
    Scale,
    Translation,
    Rotation,
    GaussianBlur,
    Average,
    MedianBlur,
)


class AverageForm(forms.ModelForm):
    class Meta:
        model = Average
        fields = ('width', 'height',)
        labels = {
            'width': 'Kernel Width',
            'height': 'Kernel Height',
        }


class MedianBlurForm(forms.ModelForm):
    class Meta:
        model = MedianBlur
        fields = ('coeff',)
        labels = {
            'coeff': 'Coefficient',
        }


class GaussianBlurForm(forms.ModelForm):
    class Meta:
        model = GaussianBlur
        fields = ('width', 'height',)
        labels = {
            'width': 'Kernel Width',
            'height': 'Kernel Height',
        }


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


class RotationForm(forms.ModelForm):
    class Meta:
        model = Rotation
        fields = ('angle',)
        labels = {
            'angle': _('Angle (θ):'),
        }


class UploadImageForm(forms.Form):
    image_file = forms.FileField(label='Select Image')
