import inspect

from django.forms.models import ModelFormMetaclass as ModelFormType
from django.db import models

from . import forms as custom_forms
from . import models as custom_models


def form_dict():
    """
    Returns a dictionary with Module Handle and Form as key-value pairs
    """
    form_dict = {}

    for name, obj in inspect.getmembers(custom_forms):
        if inspect.isclass(obj) and type(obj) == ModelFormType:
            model = obj.Meta.model
            handle = model.module_info()['Handle']
            form_dict[handle] = obj

    return form_dict


def info_list():
    """
    Returns a list of dictionaries, each containing Module Handle, Name and
    its Description
    """
    info_list = []

    for name, obj in inspect.getmembers(custom_models):
        if inspect.isclass(obj):
            info = obj.module_info()
            info_list.append(info)

    return info_list


def info_dict():
    """
    Returns a dictionary with Module Handles as keys and Name and Description
    as their values
    """
    info_dict = {}

    for name, obj in inspect.getmembers(custom_models):
        if inspect.isclass(obj):
            info = obj.module_info()
            info_dict[info['Handle']] = {
                'Name': info['Name'],
                'Description': info['Description'],
            }

    return info_dict


class UploadImageModel(models.Model):
    image_file = models.FileField(upload_to='images/')
