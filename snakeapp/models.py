from django.db import models
from django.utils import timezone

class Snake(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    notes = models.TextField()
    date_added = models.DateField(
            default=timezone.now)
    hatch_date = models.DateField(
            blank=True, null=True)

    def add_snake(self):
        self.date_added = timezone.now()
        self.save()

    def __str__(self):
        return self.name
