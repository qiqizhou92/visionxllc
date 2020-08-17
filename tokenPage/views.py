from django.shortcuts import render

# Create your views here.

def token(response):
	return render(response, "token.html", {})