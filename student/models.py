from django.db import models
from base.models import ClassProfile

class Student(models.Model):
    name = models.CharField(max_length=20)
    now_in_class = models.ForeignKey(ClassProfile,related_name='nowinschool',on_delete=False)
    once_in_class = models.ManyToManyField(ClassProfile,related_name='onceinclass',)
    starttime = models.DateField(null=True)

    def __str__(self):
        return self.name

#
# class ExamProfile(models.Model):
#
#
# class score(models.Model):
#



class Score(models.Model):
    name = models.CharField(max_length=20)
    classname = models.ForeignKey(ClassProfile,related_name='class_score',on_delete=False)
    chinese = models.FloatField(default=0)
    math = models.FloatField(default=0)
    english = models.FloatField(default=0)
    sum = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.name
