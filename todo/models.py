from tkinter import CASCADE
from django.db import models
from django.urls import reverse

class Todo(models.Model):
    text = models.CharField(max_length=40)
    amount = models.FloatField()
    complete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    whose_account_to_repay = models.CharField(max_length=40)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('todo-detail', args=[str(self.id)])

class Repay(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    repay = models.FloatField()
    date = models.DateField(auto_now=True)







