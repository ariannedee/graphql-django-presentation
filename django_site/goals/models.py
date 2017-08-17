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
        return round(progress_avg, 2)


class KeyResult(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='key_results')
    name = models.CharField(max_length=500)
    starting_value = models.FloatField(default=0)
    target_value = models.FloatField(default=100)
    current_value = models.FloatField(default=0)
    progress = models.DecimalField(default=0, decimal_places=2, max_digits=5)

    def save(self, **kwargs):
        print('got here')
        self.progress = abs(self.current_value - self.starting_value) / max(abs(self.target_value - self.starting_value), 1)
        print(self.progress)
        super(KeyResult, self).save(**kwargs)
