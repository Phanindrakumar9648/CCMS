from django.urls import path
from .import pdf_views

urlpatterns=[
	path("",pdf_views.gen,name="gen")
]
