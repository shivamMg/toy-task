import cv2
import numpy as np

from django.db import models

# module_info()
#  Handle: Unique module handle in lowercase
#  Name: Name to be displayed to the user
#  Description: Description about what the module does

class Average(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()

    def module_func(self, img):
        blur = cv2.blur(img,(self.width, self.height))
        return blur

    def module_info():
        return {
            'Handle': 'average',
            'Name': 'Average',
            'Description': 'Performs average',
        }


class MedianBlur(models.Model):
    coeff = models.IntegerField()

    def module_func(self, img):
        blur = cv2.medianBlur(img,(self.coeff),0)
        return blur

    def module_info():
        return {
            'Handle': 'medianblur',
            'Name': 'Median Blur',
            'Description': 'Produce median blur',
        }


class GaussianBlur(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()

    def module_func(self, img):
        blur = cv2.GaussianBlur(img,(self.width,self.height),0)
        return blur

    def module_info():
        return {
            'Handle': 'gaussianblur',
            'Name': 'Gaussian Blur',
            'Description': 'Produce Gaussian blur',
        }


class Scale(models.Model):
    width = models.FloatField()
    height = models.FloatField()

    def module_func(self, img):
        res = cv2.resize(img, None, fx=self.width, fy=self.height,
                         interpolation = cv2.INTER_CUBIC)
        return res

    def module_info():
        return {
            'Handle': 'scale',
            'Name': 'Scale',
            'Description': 'Resize image to new width and height',
        }


class Translation(models.Model):
    xoffset = models.FloatField()
    yoffset = models.FloatField()

    def module_func(self, img):
        rows, cols, _ = img.shape
        M = np.float32([[1, 0, self.xoffset], [0, 1, self.yoffset]])

        dst = cv2.warpAffine(img, M, (cols,rows))
        return dst

    def module_info():
        return {
            'Handle': 'translation',
            'Name': 'Translation',
            'Description': 'Shift object location',
        }


class Rotation(models.Model):
    angle = models.FloatField()

    def module_func(self, img):
        rows, cols, _ = img.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        dst = cv2.warpAffine(img,M,(cols,rows))
        return dst

    def module_info():
        return {
            'Handle': 'rotation',
            'Name': 'Rotation',
            'Description': 'Rotate image for an angle',
        }
