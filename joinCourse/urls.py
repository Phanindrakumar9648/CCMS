from django.urls import path,re_path
from .import views
app_name="joinCourse"
urlpatterns=[
	#path("",views.genPDF,name='pdf'),
	path("",views.home,name='home'),
	path("about",views.about,name='about'),
	path("events",views.events,name='events'),
	path("Success",views.Success,name="Success"),
	path("feedback",views.feedback,name='feedback'),
	path("contact",views.contact,name='contact'),
	path("subscribe",views.subscribe,name='subscribe'),
	path("register",views.courseReg,name="courseReg"),
	path("registerHere",views.RegisterHere,name="RegisterHere"),
	path("showData",views.showData,name='showData'),
	path("getDetails",views.getDetails,name='getDetails'),
	# path("some_view",views.some_view,name='some_view'),
	path("uploadData",views.uploadData,name='uploadData'),
	# path("ShowOnes",GeneratePDF.as_view(),name="ShowOne"),
	path("ShowOnes/<int:stu_id>/",views.GenerateOne.as_view(),name="ShowOne"),
	path("GenAll",views.GenerateAll.as_view(),name="GenAll"),
	path("login",views.login,name="login"),
	path("logins",views.logins,name="logins"),
	path("logouts",views.logouts,name="logouts"),
]