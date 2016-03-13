from django.db import models

# module_info()
#  Handle: Unique module handle in lowercase
#  Name: Name to be displayed to the user
#  Description: Description about what the module does


class Scale(models.Model):
    width = models.FloatField()
    height = models.FloatField()

    def module_info():
        return {
            'Handle': 'scale',
            'Name': 'Scale',
            'Description': 'Resize image to new width and height',
        }


class Translation(models.Model):
    xoffset = models.FloatField()
    yoffset = models.FloatField()

    def module_info():
        return {
            'Handle': 'translation',
            'Name': 'Translation',
            'Description': 'Shift object location',
        }
