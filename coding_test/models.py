from django.db import models


class Codingsite(models.Model):
    coding_site = models.CharField(max_length=50)

    def __str__(self):
        return  self.coding_site


