from django.forms import ModelForm
from callhubapp.models import Fibonacci

class CallHubForm(ModelForm):
	class Meta:
		model = Fibonacci
		exclude = ['out']