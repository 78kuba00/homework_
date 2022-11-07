from django.db import models
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процесее'), ('done', 'Сделано')]

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="Статус")
    details = models.TextField(max_length=3000, null=False, blank=False, default="-", verbose_name="Содержание")
    deadline = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f'{self.id}. {self.title}'