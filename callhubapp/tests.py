from django.test import TestCase
from callhubapp.models import Fibonacci
from callhubapp.forms import CallHubForm
from django.core.cache import cache
# Create your tests here.
class HomeViewTestCase(TestCase):
	def test_index(self):
		# Testing GET request
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_context(self):
		# Testing form in homepage
		resp = self.client.get('/')
		self.assertTrue('form' in resp.context)

	def test_post(self):
		# Testing POST request
		resp = self.client.post('/', {'inp':5})
		self.assertEqual(resp.status_code, 200)

class FibonacciFormTestCase(TestCase):
	def test_form_validity(self):
		obj = Fibonacci(inp=5)
		form = CallHubForm({'inp': 5}, instance=obj)
		self.assertEqual(form.is_valid(), True)

	def test_form_fields(self):
		obj = CallHubForm()
		self.assertTrue('inp' in obj.fields)
		self.assertFalse('out' in obj.fields)

class FibonacciModelTestCase(TestCase):
	def setUp(self):
		super(FibonacciModelTestCase, self).setUp()
		self.obj1, status = Fibonacci.objects.get_or_create(inp=6)
		self.obj2, status = Fibonacci.objects.get_or_create(inp=9)

	def test_model_func(self):
		# Check Model Function
		self.assertEqual(self.obj1._get_fibonacci(), self.obj1.out)
		self.assertEqual(self.obj2._get_fibonacci(), self.obj2.out)

class CacheTestCase(TestCase):
	def setUp(self):
		super(CacheTestCase, self).setUp()
		cache.set(5, 5)
		
	def test_cache(self):
		self.assertEqual(cache.get(5), 5)
