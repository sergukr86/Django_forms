from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fathers_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
