from django.shortcuts import render, render_to_response
from callhubapp.forms import CallHubForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from callhubapp.models import Fibonacci
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = CallHubForm(request.POST)
		if form.is_valid():
			inp = form.cleaned_data['inp']
			if cache.get(inp):
				data = cache.get(inp)
				return render_to_response(
						'home.html',
						{'form':form, 'out':data},
						context_instance=RequestContext(request)
					)
			try:
				obj = Fibonacci.objects.get(inp=inp)
			except ObjectDoesNotExist:
				obj = form.save(commit=True)
			cache.set(inp, obj.out)
			return render_to_response(
					'home.html',
					{'form':form, 'out':obj.out},
					context_instance=RequestContext(request)
				)
		else:
			return render_to_response(
					'home.html',
					{'form':form},
					context_instance=RequestContext(request)
				)
	else:
		return render_to_response(
			'home.html', 
			{'form':CallHubForm()},
			context_instance=RequestContext(request)
		)