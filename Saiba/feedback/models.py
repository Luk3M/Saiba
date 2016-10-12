from django.contrib.auth.models import Permission, User
from django.db import models
from entry.models import Entry
from gallery.models import Image, Video

class Comment(models.Model):
    author          = models.ForeignKey(User, default=1)
    content         = models.CharField(max_length=250)
    creation_date   = models.DateTimeField(auto_now_add=True, blank=True)
    update_date     = models.DateTimeField(auto_now=True, blank=True)
    parent_comment  = models.ForeignKey('self', default=None, blank=True, null=True)
    hidden          = models.BooleanField(default=False)

    class Meta:
        abstract = True

class EntryComment(Comment):
    entry = models.ForeignKey(Entry, default=1)

    def __unicode__(self):
        text = '#' + str(self.id) + ' - ' + str(self.author.username) + ' (' + str(self.entry.title) + ')'
        return text

class ImageComment(Comment):
    image = models.ForeignKey(Image, default=1)

    def __unicode__(self):
        text = '#' + str(self.id) + ' - ' + str(self.author.username) + ' (' + str(self.image.title) + ')'
        return text

class Vote(models.Model):
    author      = models.ForeignKey(User, default=1)
    date        = models.DateTimeField(auto_now=True, blank=True)
    type        = models.CharField(max_length=250)
    is_positive = models.BooleanField(default=True)

    def __unicode__(self):
        text = '#' + str(self.id) + ' - ' + str(self.author.username)
        return text
    
    class Meta:
        abstract = True

class ImageVote(Vote):
    media = models.ForeignKey(Image, default=1)

class VideoVote(Vote):
    media = models.ForeignKey(Video, default=1)

class CommentVote(Vote):
    comment = models.ForeignKey(EntryComment, default=1)   