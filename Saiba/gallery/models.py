from django.contrib.auth.models import Permission, User
from django.db import models
from entry.models import Entry
from django.utils import timezone

class State(models.Model):
    label       = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __unicode__(self):
        return self.label

class Image(models.Model):
    author      = models.ForeignKey(User, blank=True)
    title       = models.CharField(max_length=250)
    date        = models.DateTimeField(default=timezone.now, blank=True)
    date_origin = models.CharField(max_length=100, blank=True)
    source      = models.CharField(max_length=250)
    tags        = models.ManyToManyField('home.Tag', blank=True)
    entry       = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="images")
    hidden      = models.BooleanField(default=False)
    file        = models.ImageField(blank=True, upload_to='icon/')
    description = models.TextField(max_length=250, blank=True)
    state       = models.ForeignKey(State, on_delete=models.CASCADE, default=1)
    trending_points = models.IntegerField(default=0)

    def __unicode__(self):
        return self.entry.title + ' - ' + self.title

class Video(models.Model):
    author      = models.ForeignKey(User, blank=True)
    title       = models.CharField(max_length=250)
    date        = models.DateTimeField(default=timezone.now, blank=True)
    date_origin = models.CharField(max_length=100, blank=True)
    tags        = models.ManyToManyField('home.Tag', blank=True)
    entry       = models.ForeignKey(Entry, on_delete=models.CASCADE)
    hidden      = models.BooleanField(default=False)
    link        = models.CharField(max_length=250)
    description = models.TextField(max_length=250, blank=True)
    state       = models.ForeignKey(State, on_delete=models.CASCADE, default=1)

    def __unicode__(self):
        return self.entry.title + ' - ' + self.title