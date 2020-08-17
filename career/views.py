from django.shortcuts import render
from . import forms
# Create your views here.

def career(response):
	return render(response, "career/careerPage.html", {})

def regform(request):
	form = forms.SignUp()
	if request.method == 'POST' :
		form = forms.SignUp(request.POST)
		html = 'we have recieved this form again'
	else:
		html = 'Thank you for your applcation!'
	return render(request, 'careerPage.html', {'html': html, 'form': form})