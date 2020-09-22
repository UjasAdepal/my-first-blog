from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # link to another model (ForeignKey)
    title = models.CharField(max_length=200) # we can type text upto limit of 200 char (CharField)
    text = models.TextField() # limit less text we can type (TextField)
    created_date = models.DateTimeField(default=timezone.now) # this is date and time (DateTimeField)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title