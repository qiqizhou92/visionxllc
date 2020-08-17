from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
	return render(response, "main/index.html", {})

def home(response):
	return render(response, "main/home.html", {})

def contact(response):
	return render(response, "main/contact.html", {})

def industry(response):
	return render(response, "main/industry.html", {})

def teams(response):
	return render(response, "main/teams.html", {})

#def token(response):
#	return render(response, "main/token.html", {})

