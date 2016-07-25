from __future__ import unicode_literals

from django.db import models
from callhubapp.utils import fib, matrix_pow, fib_matrix

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
		if int(self.inp) <= 10**6:
			return fib(int(self.inp))
		else:
			return matrix_pow(fib_matrix, int(self.inp), 1000000007)[0][1]
