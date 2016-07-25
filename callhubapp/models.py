from __future__ import unicode_literals

from django.db import models
from callhubapp.utils import fib

# Create your models here.
class Fibonacci(models.Model):
	inp = models.CharField(max_length=400)
	out = models.TextField()

	def save(self, *args, **kwargs):
		if not self.out:
			self.out = self._get_fibonacci()
		super(Fibonacci, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.inp

	def _get_fibonacci(self):
		return fib(int(self.inp))
