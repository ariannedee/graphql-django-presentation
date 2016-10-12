from __future__ import division
from django.contrib.auth.models import User
from django.db import models


class Objective(models.Model):
    name = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='objectives')

    @property
    def progress(self):
        kr_progresses = [kr.current_value / kr.target_value for kr in self.key_results.all()]
        progress_avg = sum(kr_progresses) / self.key_results.count()
        return int(progress_avg * 100)


class KeyResult(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='key_results')
    name = models.CharField(max_length=500)
    starting_value = models.IntegerField(default=0)
    target_value = models.IntegerField(default=100)
    current_value = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
