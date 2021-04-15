from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=260)
    display_name = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name
