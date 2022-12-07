from statistics import mode
from django.db import models


class Document(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)

class Report(models.Model):
    text = models.TextField(max_length=1500)

    def __str__(self):
        return self.text[:50]

class HistoryObject(models.Model):
    to_language = models.CharField(max_length=100)
    from_language = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    translate = models.CharField(max_length=1000)

    def __str__(self):
        return self.text[:30]

class SelectObject(models.Model):
    to_language = models.CharField(max_length=100)
    from_language = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    translate = models.CharField(max_length=1000)

    def __str__(self):
        return self.text[:30]