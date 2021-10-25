from django.db import models


class DeadlineError(Exception):
    pass


class Human(models.Model):
    last_name = models.CharField(max_length=50, db_index=True)
    first_name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Homework(models.Model):
    text = models.CharField(max_length=100, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DurationField()


class Teacher(Human):
    homework_done = models.ManyToManyField(Homework)


class Student(Human):
    pass


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=200, db_index=True)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
