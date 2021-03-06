import os

from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from embed_video.fields import EmbedVideoField

import saiba.image_utils
from feedback.models import Action
from home.models import SaibaSettings


class State(models.Model):
    label = models.CharField(max_length=250)
    code_name = models.CharField(max_length=250, default="")
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.label

class Image(models.Model):
    author          = models.ForeignKey(User, blank=True)
    title           = models.CharField(max_length=250)
    date            = models.DateTimeField(default=timezone.now, blank=True)
    date_origin     = models.CharField(max_length=100, blank=True)
    source          = models.CharField(max_length=250)
    tags            = models.ManyToManyField('home.Tag', blank=True)
    entry           = models.ForeignKey('entry.Entry', on_delete=models.CASCADE, related_name="images")
    hidden          = models.BooleanField(default=False)
    file            = models.ImageField(upload_to='icon/', blank=True)
    file_url        = models.URLField(blank=True)
    description     = models.TextField(max_length=250, blank=True)
    state           = models.ForeignKey(State, on_delete=models.CASCADE, default=1)
    trending_points = models.IntegerField(default=0)
    views           = GenericRelation('feedback.View')
    comments_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.entry.title + ' - ' + self.title

    def create_action(self, action_type_number = "0"):
        new_action = Action.objects.create(author=self.author, target=self, target_id=self.id, action_type=action_type_number)
        new_action.save()

    def save(self, *args, **kwargs):
        if self.file_url and not self.file:
            image_name, image_content = saiba.image_utils.download_external_image(self.file_url)

            if image_name and image_content != None:
                self.file.save(image_name, ContentFile(image_content), save=False)

        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery:image_detail', kwargs={'image_id': self.id, 'slug': '-'+self.entry.slug})

class Video(models.Model):
    author          = models.ForeignKey(User, blank=True)
    title           = models.CharField(max_length=250)
    date            = models.DateTimeField(default=timezone.now, blank=True)
    date_origin     = models.CharField(max_length=100, blank=True)
    tags            = models.ManyToManyField('home.Tag', blank=True)
    entry           = models.ForeignKey('entry.Entry', on_delete=models.CASCADE)
    hidden          = models.BooleanField(default=False)
    media           = EmbedVideoField(max_length=250)
    description     = models.TextField(max_length=250, blank=True)
    state           = models.ForeignKey(State, on_delete=models.CASCADE, default=1)
    trending_points = models.IntegerField(default=0)
    views           = GenericRelation('feedback.View')
    comments_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.entry.title + ' - ' + self.title

    def create_action(self, action_type_number = "0"):
        new_action = Action.objects.create(author=self.author, target=self, target_id=self.id, action_type=action_type_number)
        new_action.save()

    def get_absolute_url(self):
        return reverse('gallery:video_detail', kwargs={'video_id': self.id})
