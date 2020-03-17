from django.shortcuts import render,redirect
from joinCourse.models import Register,employee
from io import BytesIO
from django.views.generic import View

from django.template.loader import get_template
from django.template import loader
#from reportlab.pdfgen import canvas
from django.http import HttpResponse,Http404,HttpResponseRedirect

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,mm
from reportlab.lib.pagesizes import letter,landscape

from fpdf import FPDF

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

# from .utils import render_to_pdf
#return HttpResponseRedirect('/url-where-you-want-to-redirect/')
# from django.core.urlresolvers import reverse
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'critical',
}

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def subscribe(request):
	mail=request.POST['subscribe']
	# fromMail="bharathsiva519@gmail.com"
	fromMail="alex.apssdc@gmail.com"
	subject="Get Started Courses"
	body="Thank and Regards,We Will Get Back to You."
	send_mail(subject,body,fromMail,[mail],fail_silently=False)
	return render(request,"joinCourse/thankYou.html")

def home(request):
	return render(request,"joinCourse/home.html")

def about(request):
	return render(request,"joinCourse/about.html")

def events(request):
	return render(request,"joinCourse/events.html")	

def Success(request):
	return render(request,"joinCourse/Success.html")	

def feedback(request):
	return render(request,"joinCourse/feedback.html")	

def contact(request):
	return render(request,"joinCourse/contact.html")
	
def courseReg(request):
	return render(request,"joinCourse/register.html")

def RegisterHere(request):
	try:
		register=Register(name=request.POST['name'],gender=request.POST['gender'],designation=request.POST['design'],college=request.POST['college'],course=request.POST['courses'],mobile=request.POST['mobile'],email=request.POST['email'],joined_date=request.POST['date'])
		register.save()
		return render(request,"joinCourse/thankYou.html")
	except Exception as e:
		print(e)
		return render(request,"joinCourse/error.html")

def getDetails(request):
	course=request.POST['course']
	tech=Register.objects.filter(course=course)
	return render(request,"joinCourse/joinedCourse.html",{'tech':tech})

class GenerateOne(View):
	def get(self,request,stu_id):
		register=Register.objects.filter(id=stu_id)	
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="IndividualCourse.pdf"'

		html="<h1>Success</h1>"
		c = canvas.Canvas(response,pagesize=letter)
		width, height = letter

		for r in register:
			c.drawImage("icons/certificate.jpg", 0,0, 8.5*inch,10*inch)
			c.setFont('Helvetica', 12)
			course=r.course
			c.drawString(270, 450,course.upper())
			name=r.name
			c.drawString(270, 300, name.upper())
			date=r.joined_date
			c.drawString(150, 200, str(date))
			c.showPage()		
		c.save()
		return response

class GenerateAll(View):
	def get(self,request):
		register=Register.objects.all()
		#template =get_template("joinCourse/home.html")
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Course.pdf"'

		html="<h1>Success</h1>"
		c = canvas.Canvas(response,pagesize=letter)
		width, height = letter
		pdf=FPDF()

		for r in register:
			c.drawImage("icons/certificate.jpg", 0,0, 8.5*inch,10*inch)
			c.setFont('Helvetica', 12)
			course=r.course
			c.drawString(270, 450,course.upper())
			name=r.name
			c.drawString(270, 300, name.upper())
			date=r.joined_date
			c.drawString(150, 200, str(date))
			c.showPage()		
		c.save()
		return response



def login(request):
	return render(request,"joinCourse/login.html")

def logins(request):
	if request.user.is_authenticated:		
		return render(request,"dashBoard.html")

	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user is None:
			return render(request,"joinCourse/LoginError.html")
		else:
			dj_login(request,user)
			refurl=request.GET.get('next')
			if refurl is not None:
				return redirect(refurl)
		return render(request,"dashBoard.html")
	else:
		return render(request,"joinCourse/login.html")

def logouts(request):
	if request.user.is_authenticated:
		logout(request)
		return render(request,"joinCourse/login.html")
	else:
		return render(request,"joinCourse/login.html")
	return render(request,"joinCourse/login.html")

@login_required()
def showData(request):	
	register=Register.objects.all().order_by('id').reverse()
	context={'register':register}
	return render(request,"joinCourse/joinedCourse.html",context)


# def uploadData(request):
# 	data = {}

# 	if request.method=="GET":
# 		return render(request, "joinCourse/uploadForm.html", data)
#     	# if not GET, then proceed
# 	try:
# 		csv_file = request.FILES["csv_file"]
# 		print(csv_file)
# 	except Exception as e:
# 		print(e)


# 			# if not csv_file.name.endswith('.csv'):
# 			# messages.error(request,'File is not CSV type')
# 			# return HttpResponseRedirect(reverse("myapp:upload_csv"))
# 			# #if file is too large, return
# 			# if csv_file.multiple_chunks():
# 			# messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
# 			# return HttpResponseRedirect(reverse("myapp:upload_csv"))

# 			# file_data = csv_file.read().decode("utf-8")        

# 			# lines = file_data.split("\n")
# 			# #loop over the lines and save them in db. If error , store as string and then display
# 			# for line in lines:                        
# 			# fields = line.split(",")
# 			# data_dict = {}
# 			# data_dict["name"] = fields[0]
# 			# data_dict["start_date_time"] = fields[1]
# 			# data_dict["end_date_time"] = fields[2]
# 			# data_dict["notes"] = fields[3]
# 			# try:
# 			# 	form = EventsForm(data_dict)
# 			# 	if form.is_valid():
# 			# 		form.save()                    
# 			#     else:
# 			#         logging.getLogger("error_logger").error(form.errors.as_json())                                                
# 			# except Exception as e:
# 			#     logging.getLogger("error_logger").error(repr(e))                    
# 			#     pass

# 			# except Exception as e:
# 			# logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
# 			# messages.error(request,"Unable to upload file. "+repr(e))

# 			# return HttpResponseRedirect(reverse("myapp:upload_csv"))
# 	return render(request,"joinCourse/uploadForm.html")


def uploadData(request):
	data = {}
	if "GET" == request.method:
		return render(request, "joinCourse/uploadForm.html", data)
	# if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("courses:uploadData"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("courses:uploadData"))

		file_data = csv_file.read().decode("utf-8")        

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:
			fields = line.split(",")
			data_dict = {}
			data_dict["name"] = fields[0]
			data_dict["start_date"] = fields[1]
			data_dict["end_date"] = fields[2]
			data_dict["notes"] = fields[3]
			try:
				form = employee(data_dict)
				if form.is_valid():
					form.save()                    
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())                                                
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))                    
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		#messages.error(request,"Unable to upload file. "+repr(e))
	return HttpResponse("Success")











# def login1(request):
# 	next=request.GET.get('next','/')
# 	if request.method=="POST":
# 		username=request.POST['username']
# 		password=request.POST['password']
# 		user=authenticate(username=username,password=password)
# 		if user is not None:
# 			if user.is_active:
# 				login(request,user)
# 				return HttpResponseRedirect('/')
# 		else:
# 			HttpResponse("Inactive user!")
# 	else:
# 		return HttpResponseRedirect('/login/')
# 	return render(request,"joinCourse/login.html",{'redirect_to':next})




		# p.showPage()
		# p.save()		
		# pdf = buffer.getvalue()
		# buffer.close()
		# response.write(pdf)
		#canvas.Canvas(buffer)		
		#return response #HttpResponse(pdf.output("PDF/a.pdf","F"),open("PDF/a.pdf"))




# def ShowOne(request,stu_id):
# 	register=Register.objects.filter(id=stu_id)
# 	context={'registerOne':register}
# 	return render(request,"joinCourse/joinedCourse.html",context)





# def ge(request):
#     return pdf.gens()
# def genPDF(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(1, 1, "Hello world.")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response




#from django.core.files.storage import FileSystemStorage
#from fpdf import FPDF
#from django.template.loader import render_to_string
#from weasyprint import HTML, CSS

# Create your views here.

# def genPDF(request):
# 	register=Register.objects.all()
# 	pname='newBatch'
# 	if register!=None:
# 		pdf=FPDF()
# 		for register in register:
# 			print(register.name)
# 			pdf.add_page("a4")
# 			pdf.set_font('Arial', 'B', 16)
# 			pdf.cell(90, 10, register.name,1,0,"C")
# 			pdf.cell(90, 10, register.course,1,0,"C")
			
# 			#return render(request,"retrive.html",context)
# 			return pdf.output("static/PDFs/"+pname+".pdf","F")
# 	else:
# 		return HttpResponse("Something Went Wrong...!")
# 	return render(request,"retrive.html",{'register':register})

# 0
# def genPDF(request):
# 	try:		
# 	    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
# 	    html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})

# 	    html = HTML(string=html_string)

# 	    fs = FileSystemStorage('/PDFs')
# 	    with fs.open('mypdf.pdf') as pdf:
# 	        response = HttpResponse(pdf, content_type='application/pdf')
# 	        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
# 	        return response
# 	    return html.write_pdf(target='/PDFs/mypdf.pdf')
# 	except Exception as e:
# 		print(e)


# class GenerateOne(View):
# 	def get(self,request,stu_id):
# 		register=Register.objects.filter(id=stu_id)		
# 		pdf=FPDF()
		
# 		for register in register:
# 			att=register.name+'_'+str(register.joined_date)+'_'+register.course
# 			pdf.add_page("a4")		
# 			pdf.image('icons/certificate.jpg', 10, 8, 280)	
# 			pdf.set_font('Arial', 'B', 16)

# 			pdf.ln(70)
# 			pdf.cell(90, 10, '',0,0,"C")
# 			course=register.course
# 			pdf.cell(100, 10,course.upper(),0,0,"C")

# 			pdf.ln(40)
# 			pdf.cell(90, 10, '',0,0,"C")
# 			name=register.name
# 			pdf.cell(100,10,name.upper(),0,0,"C")

# 			pdf.ln(20)
# 			pdf.cell(60, 10, '',0,0,"C")
# 			date=register.joined_date
# 			pdf.cell(40, 10,str(date),0,0,"C")
# 		my_data=pdf.output("PDF/"+att+".pdf","F")
# 		response = HttpResponse(my_data, content_type='application/pdf')
# 		response['Content-Disposition'] = 'attachment; filename="foo.pdf"'
# 		return HttpResponse(response)



# class GenerateAll(View):
# 	def get(self,request):
# 		register=Register.objects.all()
# 		#template =get_template("joinCourse/home.html")
# 		response = HttpResponse(content_type='application/pdf')
# 		response['Content-Disposition'] = 'attachment; filename="Course.pdf"'

# 		html="<h1>Success</h1>"
# 		c = canvas.Canvas(response)
# 		pdf=FPDF()

# 		for r in register:
# 			# print(r.name)
# 			# pdf.add_page("a4")		
# 			# pdf.image('icons/certificate.jpg', 10, 8, 280)	
# 			# pdf.set_font('Arial', 'B', 16)

# 			# pdf.ln(70)
# 			# pdf.cell(90, 10, '',0,0,"C")
# 			# course=r.course
# 			# pdf.cell(100, 10,course.upper(),0,0,"C")

# 			# pdf.ln(40)
# 			# pdf.cell(90, 10, '',0,0,"C")
# 			# name=r.name
# 			# pdf.cell(100,10,name.upper(),0,0,"C")

# 			# pdf.ln(20)
# 			# pdf.cell(60, 10, '',0,0,"C")
# 			# date=r.joined_date
# 			# pdf.cell(40, 10,str(date),0,0,"C")
# 			c.setFont('Helvetica', 12)
# 			c.drawString(40, 10, str(date))
# 			c.showPage()

		
# 		c.save()
		
# 		#my_data=pdf.output(dest='S')
# 		#stream=BytesIO(my_data)
# 		#response = HttpResponse(my_data, content_type='application/pdf')
# 		#response['Content-Disposition'] = 'attachment; filename="Course.pdf"'
# 		#return HttpResponse(open('my_data', 'rb').read(), content_type='application/zip')
# 		return response
