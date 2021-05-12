from django.db import models


class StudentGroup(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField()

    class Meta:
        unique_together = ('name', 'year',)

    def __str__(self):
        return '%s%s' % (self.year, self.name)


class Application(models.Model):
    created_at = models.DateField(auto_now_add=True)
    f_name = models.CharField(max_length=20, verbose_name="Student's first name")
    l_name = models.CharField(max_length=30, verbose_name="Student's last name")
    age = models.IntegerField(verbose_name="Student's age")
    parent_tel_numb = models.CharField(max_length=13, verbose_name="Parent's telephone number")
    parent_email = models.EmailField(max_length=254, verbose_name="Parent's email")
    parent_f_name = models.CharField(max_length=20, verbose_name="Parent's first name")
    parent_patronimic = models.CharField(max_length=30, verbose_name="Parent's patronimic")
    parent_l_name = models.CharField(max_length=30, verbose_name="Parent's last name")

    def __str__(self):
        return '%s : %s %s' % (self.created_at, self.f_name, self.l_name)