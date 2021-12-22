from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start = models.DateTimeField()
    end_time = models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    # TODO: link group to api key
    group = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    url = models.URLField()
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.title + " " + str(self.start)
