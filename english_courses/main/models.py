from django.db import models


class StudentGroup(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField()

    class Meta:
        unique_together = ('name', 'year',)

    def __str__(self):
        return '%s%s' % (self.year, self.name)