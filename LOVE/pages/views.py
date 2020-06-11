from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "this is about us",
		"my_number": 20200316,
		"list": [456,789, 000, 'abc'],
		"html": "<h1>hello motor</h1>",
	}
	return render(request, "about.html", my_context)
