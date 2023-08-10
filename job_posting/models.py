from django.db import models
from datetime import datetime, date


class Certification(models.Model):
    company_name = models.CharField(max_length=50)
    contents = models.CharField(max_length=50)
    exam_date = models.DateField()
    d_day = models.DateField()

    @property
    def d_day(self):
        delta = self.exam_date - date.today()
        return delta.days

    def __str__(self):
        return self.company_name

