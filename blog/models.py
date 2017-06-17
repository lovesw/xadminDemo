from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2, choices=(("1", "男"), ("2", "女")))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name
