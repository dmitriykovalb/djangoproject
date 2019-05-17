from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Posts(models.Model):
    """[Create fields of the table]

    Arguments:
        models {[text]} -- [title,text,date,author]
    """
    dt = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')[:-3]
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=dt)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    """[Returns a string representation of the title]

    Returns:
        [str] -- [article title]
    """

    def __str__(self):
        return self.title

    """[Tells Django how to calculate the URL for an object.]

    Returns:
        [str] -- [a string that can be used in an HTTP request]
    """

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"pk": self.pk})
