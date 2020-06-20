from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = True
        ordering = ["pk"]

    def __str__(self):
        return self.user


class MembersProfile(models.Model):
    """
    purpose: Creating Member Profile with extending User Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    tz = models.CharField(max_length=50,null=False, blank=False)
    activity_periods = models.ManyToManyField(Activity)

    class Meta:
        managed = True
        ordering = ["pk"]

    def __str__(self):
        return self.user