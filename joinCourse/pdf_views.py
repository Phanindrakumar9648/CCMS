from django.shortcuts import render,redirect
from .import pdf
from django.http import HttpResponse
def gen(request):
	html=""
	html+="<iframe src='../a.pdf'></iframe>"
	p=pdf.gens
	return HttpResponse(html,p) 