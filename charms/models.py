from django.db import models


# Create your models here.
class Exalt(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Charm(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=100, blank=True, null=True)
    prerequisites = models.CharField(max_length=100, blank=True, null=True)
    section = models.CharField(max_length=100, blank=True, null=True)
    exalt_type = models.ForeignKey(Exalt, on_delete=models.PROTECT)
    charm_type = models.CharField(max_length=100, blank=True, null=True)
    keywords = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    whole_string = models.TextField()

    def __str__(self):
        return self.title
