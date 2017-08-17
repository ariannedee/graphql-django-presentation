from __future__ import division
from django.contrib.auth.models import User
from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    @property
    def progress(self):
        task_progresses = [kr.current_value / kr.target_value for kr in self.tasks.all()]
        progress_avg = sum(task_progresses) / self.tasks.count()
        return round(progress_avg, 2)


class Task(models.Model):
    objective = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=500)
    starting_value = models.FloatField(default=0)
    target_value = models.FloatField(default=100)
    current_value = models.FloatField(default=0)
    progress = models.DecimalField(default=0, decimal_places=2, max_digits=5)

    def save(self, **kwargs):
        self.progress = abs(self.current_value - self.starting_value) / max(abs(self.target_value - self.starting_value), 1)
        super(Task, self).save(**kwargs)
