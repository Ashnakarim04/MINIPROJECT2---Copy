import csv
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages, auth
from django.http import HttpResponse,HttpResponseRedirect
from .models import AdminStudent, Jobs, CompanyProfile
from .models import Students,StudentProfile,CompanyApprove,JobApplication
# from .forms import StudentForm
from django.shortcuts import render, get_object_or_404, redirect
# from .models import  CustomUser
# from django.contrib.auth import get_user_model 
# from django.contrib.auth import get_user_model
# Create your views here.
 
# def sample(request):
#     return render(request, 'sample.html')
# def loginn(request):
#     return render(request, 'login.html')
# def reg(request):
#     return render(request, 'registration.html')
# User=get_user_model()
def index(request):
    return render(request, 'index.html')
def jobs(request):
    return render(request, 'jobs.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def cjob(request):
    return render(request, 'cjob.html')
def blog(request):
    return render(request, 'blog.html')
def postjob(request):
    return render(request, 'postjob.html')
# def admin_index(request):
#     return render(request, 'admin/index.html')
def admin_index2(request):
    stu=Students.objects.filter(is_active = True)
    stu_count=stu.count()
    comp=CompanyProfile.objects.filter(is_approved = 'approved')
    comp_count=comp.count()
    com=CompanyProfile.objects.filter(is_approved = 'approved')
    com_count=comp.count()
    job=Jobs.objects.filter(is_active = True)
    job_count=job.count() 
    context={
        'stu':stu,
        'stu_count':stu_count,
        'comp':comp,
        'comp_count':comp_count,
        'com':com,
        'com_count':com_count,
        'job':job,
        'job_count':job_count,
        }
    return render(request, 'admin/index-2.html',context)
def admin_profile(request):
    return render(request, 'admin/profile.html')
def admin_editprofile(request):
    return render(request, 'admin/edit-profile.html')
# def admin_students(request):
#     return render(request, 'admin/students.html')
def admin_company(request):
    return render(request, 'admin/company.html')
# def admin_addstudent(request):
#     return render(request, 'admin/addstudent.html')
def admin_studentadd(request):
    return render(request,'admin/student_add.html')
def ad_cprofile(request):
    return render(request, 'admin/ad_cprofile.html')

# def sprofile(request):
#     return render(request, 'student/sprofile.html')
def srequest(request):
    admin_student = request.user.student_profile
    return render(request, 'student/srequest.html',{'admin_student':admin_student})
# def addjob(request):
#     return render(request, 'addjob.html')
def loginn(request):
    if request.method == "POST":
        username=request.POST['email']
        # email = request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_index2')
            elif user.is_staff:
                return redirect('sindex')
            else:
                return redirect('cindex')
        else:
            messages.info(request, "Invalid Login")
            return redirect('loginn')
    else:
        return render(request, 'login.html') 

def reg(request):
    if request.method == "POST":
        companyname = request.POST['companyname']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
       
        
        
        if password == confirmPassword:
            # if User.objects.filter(companyname=companyname).exists():
            #     return render(request, 'registration.html', {'companyname_exists': True})
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email already exists') 
                return redirect('reg')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                # company_approve = CompanyApprove(companyname=companyname, email=email, user=user)
                
                company = CompanyProfile(user=user, companyname=companyname) 

                
                user.save()
                # company_approve.save()
                company.save()

                messages.success(request, 'Registration successful! You can Login now..')
                return redirect('loginn')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('reg')
    else:
        return render(request, 'registration.html')
    

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .models import CompanyApprove

# def reg(request):
#     if request.method == "POST":
#         companyname = request.POST.get('companyname')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirmPassword = request.POST.get('confirmPassword')

#         if password == confirmPassword:
#             # Check if the email already exists
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already exists')
#                 return redirect('reg')
#             else:
#                 # Create the User instance
#                 user = User.objects.create_user(username=email, password=password, email=email)

#                 # Create the CompanyApprove instance
#                 company_approve = CompanyApprove(companyname=companyname, email=email, user=user)
#                 company_approve.save()

#                 messages.success(request, 'Registration successful! You can Login now..')
#                 return redirect('loginn')
#         else:
#             messages.error(request, 'Password confirmation does not match')
#             return redirect('reg')
#     else:
#         return render(request, 'registration.html')

def loggout(request):
    print('Logged Out')
    auth.logout(request)
    return redirect('/')

def sample2(request):
    return render(request, 'sample2.html')
# def cindex(request):
#     if request.user.is_authenticated:
#         companyprofile = request.user.companyprofile
#         return render(request, 'cindex.html', {'companyprofile': companyprofile})
#     else:
#         return redirect('loginn')

from django.shortcuts import get_object_or_404

def cindex(request):
    if request.user.is_authenticated:
        try:
            # Try to retrieve the company profile
            companyprofile = request.user.companyprofile
        except CompanyApprove.DoesNotExist:
            # If the user doesn't have a companyprofile, redirect to the profile creation page
            return redirect('loginn')

        return render(request, 'cindex.html', {'companyprofile': companyprofile})
    else:
        return redirect('loginn')


def aboutuser(request):
    return render(request, 'aboutuser.html') 
def contactuser(request):
    return render(request, 'contactuser.html')


# def postjob(request, companyprofile_id):
#     # Use get_object_or_404 to get the CompanyProfile instance or raise a 404 error if not found
#     companyprofile = get_object_or_404(CompanyProfile, id=companyprofile_id)

#     if request.method == "POST":
#         website = request.POST.get('website')
#         companyprofile.website = website
#         companyprofile.save()
#         return redirect('cindex')
#     else:
#         print("NO")
#     context={
#         'companyprofile': companyprofile
#     }
#     job = Jobs.objects.all()
#     return render(request, 'postjob.html', {'job': job, 'companyprofile': companyprofile}, context)

# def sindex(request):
#     if request.user.is_authenticated:
#         studentprofile= request.user.studentprofile
#         return render(request, 'sindex.html',{'studentprofile': studentprofile})
#     else:
#         return redirect()
    


def studentloginn(request):
    if request.method == "POST":
        username=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid Login")
            return redirect('studentloginn')
    else:
        return render(request, 'studentlogin.html') 

from django.core.files.images import get_image_dimensions
from django.http import HttpResponseBadRequest

def addjob(request):
        
        # obj=CompanyProfile.objects.get(id=obj_id)
        # cmp = get_object_or_404(CompanyProfile, user=request.user)
        # print(cmp)
    # except CompanyProfile.DoesNotExist:
            

            user = request.user
            

            if request.method == 'POST':
                cname = request.POST.get('cname')
                jname = request.POST.get('jname') 
                salary = request.POST.get('salary')
                email = request.POST.get('email')
                sdate = request.POST.get('sdate')
                edate = request.POST.get('edate')
                link = request.POST.get('link')
                job_descriptions = request.POST.get('job_descriptions')
                qualifications = request.POST.get('qualifications')
                preferred_skills = request.POST.get('preferred_skills')
                responsibilities = request.POST.get('responsibilities')
                required_current_cgpa = request.POST.get('required_current_cgpa')
                required_tenth_cgpa = request.POST.get('required_tenth_cgpa')
                required_twelfth_cgpa = request.POST.get('required_twelfth_cgpa')
                required_backlog = request.POST.get('required_backlog')
                # criteria=request.FILES['criteria'] if 'criteria' in request.FILES else None

                # if criteria and not criteria.name.endswith('.pdf'):
                #     messages.error(request, 'Please upload a PDF file for the criteria.')
                #     return redirect('postjob')


                obj = Jobs()
                obj.user = request.user
                obj.cname = cname
                obj.jname = jname
                obj.salary = salary
                obj.email = email
                obj.sdate = sdate
                obj.edate = edate
                obj.link = link
                obj.job_descriptions = job_descriptions
                obj.qualifications = qualifications
                obj.preferred_skills = preferred_skills
                obj.responsibilities = responsibilities
                obj.required_current_cgpa = required_current_cgpa
                obj.required_tenth_cgpa = required_tenth_cgpa
                obj.required_twelfth_cgpa = required_twelfth_cgpa
                obj.required_backlog = required_backlog
                
                # obj.criteria=criteria
                
                obj.save()
                messages.success(request, 'Job added successfully!')
                
            # Redirect to the doctors page
                return redirect('postjob')  # Redirect to the doctors page URL name
            
            return render(request, 'addjob.html',{'user':user})

def postjob(request):
    user = request.user
    job = Jobs.objects.filter(user=user)
    print(job)
    return render(request, 'postjob.html', {'job': job})
from django.shortcuts import render
from .models import Jobs









# edit_job

from django.shortcuts import render, get_object_or_404, redirect
from .models import Jobs

def edit_job(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    criteriafile = request.FILES.get('criteria')
    if request.method == 'POST':
        job.cname = request.POST.get('cname')
        job.jname = request.POST.get('jname')
        job.salary = request.POST.get('salary')
        job.email = request.POST.get('email')
        job.sdate = request.POST.get('sdate')
        job.edate = request.POST.get('edate')
        job.link = request.POST.get('link')
        job.job_descriptions = request.POST.get('job_descriptions')
        job.responsibilities = request.POST.get('responsibilities')
        job.preferred_skills = request.POST.get('preferred_skills')
        job.qualifications = request.POST.get('qualifications')
        # job.criteria = request.POST.FILES['criteria'] if 'criteria' in request.FILES else None
        # if criteriafile:
        #     job.criteria = criteriafile
        # job.criteria = request.POST.get('criteria')
        job.save()
        # Redirect to a success page or back to the job listing page
        return redirect('postjob')  # Change 'job_listing' to the appropriate URL name
        
    return render(request, 'editjob.html', {'job': job})

# deletejob
from django.shortcuts import render, redirect
from .models import Jobs

# def delete_job(request, job_id):
#     try:
#         job = Jobs.objects.get(id=job_id)
#         job.delete()
#         # Redirect to a different page (e.g., job list or any other appropriate page)
#         return redirect('postjob')  # Replace 'job_list' with the appropriate URL name
#     except Jobs.DoesNotExist:
#         # Handle the case where the job does not exist (you can show an error message or redirect to an error page)
#         return redirect('postjob')  # Redirect to the job list page or an error page as needed
from django.shortcuts import render, get_object_or_404, redirect
from .models import Jobs

def delete_job(request, job_id):
    # Get the job object by id
    job = get_object_or_404(Jobs, id=job_id)
    
    if request.method == 'POST':
        # Set the is_active field to False
        job.is_active = False
        job.save()  # Save the updated job object with is_active=False
        return redirect('postjob')  # Redirect to a suitable page after deletion

    return render(request, 'delete_job.html', {'job': job})

def CRegistration(request):
    return render(request, 'registration.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_index')  # Redirect to admin dashboard
        else:
            # Invalid credentials, handle error or show message
            pass
    
    return render(request, 'admin/admin_login.html')



#jobs_table_view 
from django.shortcuts import render
from .models import Jobs  # Import your Jobs model here


def jobslist(request):
    job_list = Jobs.objects.filter(is_active=True)
    context = {'job_list': job_list}
    return render(request, 'admin/admin_jobtable.html', context)

# def job_list(request):
#     # Retrieve data from the Jobs model
#     joblist = Jobs.objects.all()
    
#     # Pass the data to the template
#     return render(request, 'job_list.html', {'joblist': joblist})

from django.shortcuts import render
from .models import CompanyProfile

def companyprofilelist(request):
    company_profiles = CompanyProfile.objects.filter(is_approved='approved')
    return render(request, 'admin/companyprofilelist.html', {'company_profiles': company_profiles})


def addstudents(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        email = request.POST.get('email')
        # passw = request.POST.get('passw')
        # password=request.POST.get('password')
        course = request.POST.get('course')
        department = request.POST.get('department')
        semester = request.POST.get('semester')

        obj = Students()
        obj.sname = sname
        obj.email = email
        # obj.passw = passw
        # obj.password = password
        obj.course = course
        obj.department = department
        obj.semester = semester
        
        
        obj.save()
        messages.success(request, 'Student added successfully!')

       # Redirect to the doctors page
        return redirect('admin_poststudent')  # Redirect to the doctors page URL name
    
    return render(request, 'admin/student_add.html')











def profc(request):
    return render(request,'admin/profc.html')
def admin_poststudent(request):
    stus=Students.objects.all()
    return render(request,'admin/admin_poststudent.html',{'stus': stus})

def search_company(request):
    if 'companyname' in request.GET:
        companyname = request.GET['companyname']
        # Perform the company name search, for example:
        company_profiles = CompanyProfile.objects.filter(companyname__icontains=companyname)
    else:
        company_profiles = CompanyProfile.objects.all()  # Display all company profiles if no search query

    return render(request, 'admin/companyprofilelist.html', {'company_profiles': company_profiles})
def search_student(request):
    studentname = request.GET.get('studentname', '')
    
    # Filter students based on the search query
    students = Students.objects.filter(sname__icontains=studentname)
    
    return render(request, 'admin/admin_poststudent.html', {'stus': students})
def search_student2(request):
    admission_no = request.GET.get('admission_no', '')
    
    # Filter students based on the search query
    adstudents = StudentProfile.objects.filter(admission_no__icontains=admission_no)
    
    return render(request, 'admin/ad_studentlist.html', {'adstus': adstudents})
def search_course(request):
    semail= request.GET.get('semail', '')
    
    # Filter students based on the search query
    students = Students.objects.filter(email__icontains=semail)
    
    return render(request, 'admin/admin_poststudent.html', {'stus': students})
# def adsearch_company(request):
#     if 'companyname' in request.GET:
#         companyname = request.GET['companyname']
#         # Perform the company name search, for example:
#         job_list = CompanyProfile.objects.filter(companyname__icontains=companyname)
#     else:
#         job_list = CompanyProfile.objects.all()  # Display all company profiles if no search query

#     return render(request, 'admin/admin_jobtable.html', {'job_list': job_list})
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from .models import CompanyProfile

from django.shortcuts import render
from .models import CompanyProfile

def adsearch_company(request):
    companysname = request.GET.get('companysname', '')

    print("Search query:", companysname)

    # Search for the company
    job_list = CompanyProfile.objects.filter(companyname__icontains=companysname)

    print("Company list:", job_list)

    return render(request, 'admin/admin_jobtable.html', {'job_list': job_list})






def search_job(request):
    jobsname = request.GET.get('jobsname', '')
    print("Search query:", jobsname)  # Print the search query to console

    job_list = Jobs.objects.filter(jname__icontains=jobsname)
    print("Job list:", job_list)  # Print the job list to console

    return render(request, 'admin/admin_jobtable.html', {'job_list': job_list})


# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required  # Ensure the user is logged in to access this view
# def search_jobs(request):
#     company_name = request.GET.get('companyName', '')
#     job_name = request.GET.get('jobName', '')

#     # Filter jobs based on the search criteria
#     jobs = Jobs.objects.filter(
#         cname__icontains=company_name,
#         jname__icontains=job_name,
#         is_active=True
#     )

#     # Assuming you have a StudentProfile associated with the current user
#     student_profile = request.user.studentprofile

#     return render(request, 'adpostjob.html', {'jobs': jobs, 'studentprofile_id': student_profile.id})


def edit_student(request):
    return render(request, 'edit_student.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Students

def edit_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    
    if request.method == 'POST':
        # Update student data based on form input
        student.sname = request.POST.get('sname')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.course = request.POST.get('course')
        student.department = request.POST.get('department')
        student.semester = request.POST.get('semester')
        student.save()
        return redirect('admin_poststudent')
    return render(request, 'admin/edit_student.html', {'student': student})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Students

def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)

    # Mark the student as inactive
    student.is_active = False
    student.save()

    # Redirect to admin_poststudent view
    return redirect('admin_poststudent')
def delete_company(request):
    return render(request, 'admin/ad_deletecompany.html')


def ad_deletecompany(request, comp_id):
    company_profile = get_object_or_404(CompanyProfile, id=comp_id)

    if request.method == 'POST':
        company_profile.is_active= False
        company_profile.save()
        return redirect('companyprofilelist')  # Redirect to a relevant URL after deletion

    return render(request, 'admin/ad_deletecompany.html', {'company_profile': company_profile})


import os
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views import View
from django.utils.text import slugify
from .models import Jobs

class download_criteria(View):
    def get(self, request, job_id):
        # Get the job and retrieve the criteria file path
        job = get_object_or_404(Jobs, pk=job_id)
        criteria_path = job.criteria.path

        if os.path.exists(criteria_path):
            with open(criteria_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{slugify(os.path.basename(criteria_path))}"'
                return response
        else:
            raise Http404("File not found")

# def addelete_job(request, jobb_id):
#     # Get the job object by id
#     jobb = get_object_or_404(Jobs, id=jobb_id)
    
#     if request.method == 'POST':
#         # Set the is_active field to False
#         jobb.is_active = False
#         jobb.save()  # Save the updated job object with is_active=False
#         return redirect('jobslist')  # Redirect to a suitable page after deletion

#     return render(request, 'delete_job.html', {'jobb': jobb})





from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from pathlib import Path
from django.conf import settings
from website.models import Students  # Replace `your_app` with the actual app name

# def generate_pdf(request):
#     # Your existing code for template path, context, and response
#     template_path = 'admin/admin_poststudent.html'
#     students = Students.objects.values(id,email,course,department,semester,sname)  # Retrieve students data

#     # context = {'students': students}

#     # Construct the PDF file path
#     pdf_file_path = str(Path(settings.MEDIA_ROOT) / 'temp_students_list.pdf')

#     # Rest of your existing code for PDF generation
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="{pdf_file_path}"'

#     template = get_template(template_path)
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)

#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html.escape(str(pisa_status.err)) + '</pre>')

#     return response
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import Students  # Import your model

def generate_pdf(request):
    # Fetch department data from your model
    stu = Students.objects.values ('email','course','department','semester','sname')

    # Load the HTML template
    template = get_template('admin/admin_poststudent.html')

    # Render the template with department data
    html_content = template.render({'stu': stu})

    # Create a PDF file-like object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students_list.pdf"'

    # Generate PDF
    pdf = pisa.CreatePDF(BytesIO(html_content.encode('UTF-8')), response)

    if not pdf.err:
        return response

    return HttpResponse('Error generating PDF: %s' % pdf.err)


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Students  # Assuming your student model is named 'Students'

def stureg(request):
    if request.method == "POST":
        studentname = request.POST.get('studentname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        course = request.POST.get('course')
        phoneNumber = request.POST.get('phoneNumber')

        # Check if passwords match
        if password == confirmPassword:
            # Check if the email already exists
            if Students.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('stureg')
            else:
                # Create the student object
                student = Students(studentname=studentname, email=email, password=password, course=course, phoneNumber=phoneNumber)
                student.save()

                messages.success(request, 'Registration successful! You can log in now.')
                return redirect('loginn')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('stureg')
    else:
        return render(request, 'sregistration.html')

def sloginn(request):
    if request.method == "POST":
        username=request.POST['email']
        # email = request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_index2')
            elif user.is_staff:
                return redirect('sindex')
            else:
                return redirect('cindex')
        else:
            messages.info(request, "Invalid Login")
            return redirect('loginn')
    else:
        return render(request, 'login.html') 
from django.shortcuts import render
from website.models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'admin/student/student_list.html', {'students': students})
# import pandas as pd
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Student

# def student_list(request):
#     # Read data from Excel or database (replace with your logic)
#     students = Student.objects.values('id', 'username', 'password')

#     # Return data as JSON
#     return JsonResponse(list(students), safe=False)

# # def index(request):
# #     return render(request, 'index.html')

# import json
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views import View
# from .models import Student

# class StudentListView(View):
#     def get(self, request):
#         students = Student.objects.values('id', 'username', 'password')
#         return JsonResponse(list(students), safe=False)

# @method_decorator(csrf_exempt, name='dispatch')
# class AddStudentView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         username = data.get('username')
#         password = data.get('password')
#         student = Student.objects.create(username=username, password=password)
#         return JsonResponse({'id': student.id})

# def index(request):
#     return render(request, 'index.html')
from django.http import JsonResponse
from .models import Student

def get_student_data(request):
    students = Student.objects.all()
    student_data = [{'id':student.id,'username': student.username, 'password': student.password} for student in students]
    return JsonResponse(student_data, safe=False)
# Example structure in views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class StudentDataAPIView(APIView):
#     # Your implementation
#     pass 



# @ashaworker_required
# def asha_approved_appointments(request):
#     approved_appointments = Appointment.objects.filter(is_approved=True)
#     print(approved_appointments)
#     return render(request, 'asha_temp/asha_approved_appo.html', {'approved_appointments': approved_appointments})



# from django.shortcuts import get_object_or_404, redirect
# @login_required(login_url='login_page')
# def approve_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, pk=appointment_id)
#     appointment.is_approved = True
#     appointment.save()
    
#     # Redirect back to the list of approved appointments
#     return redirect("asha_approved_appo")
from django.shortcuts import render
from website.models import CompanyProfile

from django.shortcuts import render
from website.models import CompanyProfile

def companyapprove(request):
    # Retrieve a list of company profiles
    company_profiles = CompanyProfile.objects.all()

    context = {
        'company_profiles': company_profiles
    }

    return render(request, 'admin/companyapprove.html', context)


def approve_comp(request, company_id):
    certification = get_object_or_404(CompanyProfile, id=company_id)
    if request.method == 'POST':
        certification.is_approved = CompanyProfile.APPROVED  # Set it to 'approved'
        certification.save()
    return redirect('companyapprove')

def admin_addstudents(request):
    return render(request, 'admin/student/student.html')

def ad_studentlist(request):
    adstus=StudentProfile.objects.all()
    return render(request,'admin/student/ad_studentlist.html',{'adstus': adstus})
import csv
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminStudent
from django.core.mail import send_mail
from django.conf import settings
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        admission_no = request.POST.get('admission_no', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        # Path to your CSV file for validation
        csv_file_path = 'dataset/student.csv'
        match_found = False

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if (
                    row['first_name'] == first_name and
                    row['last_name'] == last_name and
                    row['admission_no'] == admission_no
                ):
                    match_found = True
                    break

        if match_found:
            # Check if a user with the same email already exists
            existing_user = User.objects.filter(username=email).first()

            if existing_user:
                messages.error(request, 'User with this email already exists')
            else:
                # Create a new user with is_staff=True
                user = User.objects.create_user(
                    username=email,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                user.is_staff = True  # Set as staff
                user.set_password("Student@Zillionhire1")
                user.save()

                # Create a new Student
                student = AdminStudent(
                    user=user,
                    admission_no=admission_no,
                    phone=phone,
                    email=email
                )
                student.save()

                subject = 'ZillionHire Student Login Details'
                message = f'Registered as Student. Your username: {email}, Password: Student@Zillionhire1'
                from_email = settings.EMAIL_HOST_USER # Your email address
                recipient_list = [user.email] # Employee's email address

                send_mail(subject, message, from_email, recipient_list)


                messages.success(request, 'Student added successfully')
        else:
            messages.error(request, 'No matching records found')

    return render(request, 'admin/student/student.html', context={'messages': messages.get_messages(request)})
def adpostjob(request):
    return render(request,'adpostjob.html')
# @ashaworker_required
# def job_approve(request):
#     approved_jobs = Jobs.objects.filter(is_approved=True)
#     print(approved_jobs)
#     return render(request, 'adpostjob.html', {'approved_jobs': approved_jobs})


    from django.shortcuts import get_object_or_404, redirectprimary
    # @login_required(login_url='login_page')
def approved_jobs(request, job_id):
    approvejob = get_object_or_404(Jobs, id=job_id)
    
    approvejob.is_approved = True
    approvejob.save()       
        # Redirect back to the list of approved appointments
    return redirect('jobslist')


def job_approve(request, studentprofile_id):
    admjob = Jobs.objects.filter(is_approved=True)
    studentprofile = StudentProfile.objects.filter(id=studentprofile_id).first()
    print(studentprofile)
    print(admjob) 
    return render(request, 'adpostjob.html', {'admjob': admjob, 'studentprofile_id': studentprofile_id,'studentprofile':studentprofile})


def eligibility(request):
    return render(request,'eligibility.html')

def cprofile(request, companyprofile_id):
    companyprofile=CompanyProfile.objects.get(id=companyprofile_id)
    
    if request.method == "POST":
         addressline1 = request.POST.get('addressline1')
         contact = request.POST.get('contact')
         website = request.POST.get('website')
         reset_password = request.POST.get('reset_password')
         old_password = request.POST.get('old_password')
    
         companydp=request.FILES['companydp'] if 'companydp' in request.FILES else None
 
         companyprofile.addressline1 = addressline1
         companyprofile.contact = contact
         companyprofile.website= website 
         companyprofile.companydp=companydp

         if request.user.check_password(old_password):
            #  the old password is correct, set the new password
                request.user.set_password(reset_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
         else:
            messages.error(request, "Incorrect old password. Password not updated.")
        
        
         companyprofile.reset_password = reset_password
         companyprofile.save()
         
         messages.success(request, 'Profile updated successfully.')
         return redirect('cindex')
    else:
         print("NO")
    context={
        'companyprofile': companyprofile
        
    }
    return render(request, 'cprofile.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from website.models import StudentProfile

# @login_required
# def sindex(request):
#     if request.user.is_authenticated:
#         studentprofile = request.user.studentprofile
#         return render(request, 'sindex.html', {'studentprofile': studentprofile})
#     else:
#         return redirect('loginn')

@login_required
def sindex(request):
    try:
        studentprofile = request.user.studentprofile
        return render(request, 'sindex.html', {'studentprofile': studentprofile})
    except StudentProfile.DoesNotExist:
        studentprofile = StudentProfile.objects.create(user=request.user)
        return redirect(reverse('sprofile', kwargs={'studentprofile_id': studentprofile.id}))
    # try:
    # studentprofile = request.user.studentprofile
    # return render(request, 'sindex.html',{'studentprofile': studentprofile})
        # Continue with the rest of your view logic using the student_profile
        # ...
    # except StudentProfile.DoesNotExist:
        # If the studentprofile does not exist for the user, redirect to a profile creation page
        # return redirect(reverse('index'))  # Adjust the URL name accordingly
from django.contrib.auth import update_session_auth_hash  # Add this import
@login_required
def sprofile(request, studentprofile_id):
    studentprofile = get_object_or_404(StudentProfile, id=studentprofile_id)
    admin_student = request.user.student_profile  # Accessing the related AdminStudent
    
    if request.method == "POST":
        admission_no = request.POST.get('admission_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        nationality = request.POST.get('nationality')
        religion = request.POST.get('religion')
        profile_photo = request.FILES.get('profile_photo')
        gender = request.POST.get('gender')

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        course = request.POST.get('course')
        department = request.POST.get('department')
        academic_year = request.POST.get('academic_year')
        current_semester = request.POST.get('current_semester')
        cgpa = request.POST.get('cgpa')
        c_backlog=request.POST.get('c_backlog')


        twelfth_institution = request.POST.get('twelfth_institution')
        twelfth_cgpa = request.POST.get('twelfth_cgpa')
        twelfth_course = request.POST.get('twelfth_course')
        # profile_photo = request.FILES.get('profile_photo')
        twelfth_certificate_upload = request.FILES.get('twelfth_certificate_upload')

        tenth_institution = request.POST.get('tenth_institution')
        tenth_cgpa = request.POST.get('tenth_cgpa')
        tenth_course = request.POST.get('tenth_course')
        tenth_certificate_upload = request.FILES.get('tenth_certificate_upload')

        ug_institution = request.POST.get('ug_institution')
        ug_cgpa = request.POST.get('ug_cgpa')
        ug_course = request.POST.get('ug_course')
        ug_certificate_upload = request.FILES.get('ug_certificate_upload')


        reset_password = request.POST.get('reset_password')
        old_password = request.POST.get('old_password')


        # Update the student profile
        if profile_photo:
            studentprofile.profile_photo = profile_photo

        studentprofile.admission_no = admission_no
        studentprofile.first_name = first_name
        studentprofile.last_name = last_name
        studentprofile.gender = gender
        studentprofile.dob = dob
        studentprofile.nationality = nationality
        studentprofile.religion = religion
    
        studentprofile.email = email
        studentprofile.phone = phone
        studentprofile.present_address = present_address
        studentprofile.permanent_address = permanent_address

        studentprofile.course = course
        studentprofile.department = department
        studentprofile.academic_year = academic_year
        studentprofile.current_semester = current_semester
        studentprofile.c_cgpa = cgpa
        studentprofile.c_backlog = c_backlog

        studentprofile.twelfth_institution = twelfth_institution
        studentprofile.twelfth_cgpa = twelfth_cgpa
        studentprofile.twelfth_course = twelfth_course
        if twelfth_certificate_upload:
            studentprofile.twelfth_certificate_upload = twelfth_certificate_upload
        # studentprofile.twelfth_certificate_upload = twelfth_certificate_upload

        studentprofile.tenth_institution = tenth_institution
        studentprofile.tenth_course = tenth_course
        studentprofile.tenth_cgpa = tenth_cgpa
        if tenth_certificate_upload:
            studentprofile.tenth_certificate_upload = tenth_certificate_upload
        # studentprofile.tenth_certificate_upload = tenth_certificate_upload

        studentprofile.ug_institution = ug_institution
        studentprofile.ug_course = ug_course
        studentprofile.ug_cgpa = ug_cgpa
        if ug_certificate_upload:
            studentprofile.ug_certificate_upload = ug_certificate_upload
        # studentprofile.ug_certificate_upload = ug_certificate_upload

        
        if request.user.check_password(old_password):
            #  the old password is correct, set the new password
                request.user.set_password(reset_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Update the session to prevent logging out
        else:
            messages.error(request, "Incorrect old password. Password not updated.")
        
        
        studentprofile.reset_password = reset_password
        studentprofile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('sprofile', studentprofile_id=studentprofile_id)
        

    context = {
        'studentprofile': studentprofile,
        'admin_student':admin_student,
    }
    return render(request, 'student/sprofile.html', context)

# def jobapply(request):
#     return render(request, 'student/jobapply.html')
def jobapply(request, jobapply_id):

    stuprof = get_object_or_404(StudentProfile, user=request.user)
    
    job = get_object_or_404(Jobs, id=jobapply_id)
    existing_certification = JobApplication.objects.filter(user=request.user,job=job).first()

    if existing_certification:
        certification_status = existing_certification.is_approved
    else:
        certification_status = 'pending'  # Set a default value if no certification exists
    print(existing_certification)

    if certification_status == 'pending':
        if request.method == "POST":
            
            # jobapply = JobApplication(stuprof=stuprof)

            cname=request.POST.get('cname')
            jname=request.POST.get('jname')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            dob = request.POST.get('dob')
            nationality = request.POST.get('nationality')
            profile_photo = request.FILES.get('profile_photo')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            present_address = request.POST.get('present_address')
            permanent_address = request.POST.get('permanent_address')
            area_code = request.POST.get('area_code')

            c_course = request.POST.get('c_course')
            c_institution = request.POST.get('c_institution')
            c_university = request.POST.get('c_university')
            academic_year = request.POST.get('academic_year')
            c_backlog = request.POST.get('c_backlog')
            c_cgpa = request.POST.get('c_cgpa')

            twelfth_institution = request.POST.get('twelfth_institution')
            twelfth_cgpa = request.POST.get('twelfth_cgpa')
            twelfth_board = request.POST.get('twelfth_board')
            twelfth_certificate_upload = request.FILES.get('twelfth_certificate_upload')

            tenth_institution = request.POST.get('tenth_institution')
            tenth_cgpa = request.POST.get('tenth_cgpa')
            tenth_board = request.POST.get('tenth_board')
            tenth_certificate_upload = request.FILES.get('tenth_certificate_upload')

            ug_course = request.POST.get('ug_course')
            ug_institution = request.POST.get('ug_institution')
            ug_cgpa = request.POST.get('ug_cgpa')
            ug_university = request.POST.get('ug_university')
            ug_certificate_upload = request.FILES.get('ug_certificate_upload')

            skills=request.POST.get('skills')
            newcourse=request.POST.get('newcourse')
            newcert=request.FILES.get('newcert')

            workexperience=request.POST.get('workexperience')
            jobresp=request.POST.get('jobresp')
            period=request.POST.get('period')
            companydetails=request.POST.get('companydetails')

            crime=request.POST.get('crime')
            dtoc=request.POST.get('dtoc')
            doc=request.POST.get('doc')
            nature=request.POST.get('nature')

            resume = request.FILES.get('resume')

            # jobapply = get_object_or_404(JobApplication, stuprof=stuprof)

            jobapply = JobApplication.objects.create(
                    user=request.user,
                    job=job,
                    stuprof=stuprof,
                    cname = cname,
                    jname = jname,
                    first_name = first_name,
                    last_name = last_name,
                    gender = gender,
                    dob = dob,
                    nationality = nationality,
                    area_code = area_code,
                    profile_photo=profile_photo,
        
                    email = email,
                    phone = phone,
                    present_address = present_address,
                    permanent_address = permanent_address,

                    c_course = c_course,
                    c_institution = c_institution,
                    c_university = c_university,
                    academic_year = academic_year,
                    c_backlog = c_backlog,
                    c_cgpa = c_cgpa,

                    twelfth_institution = twelfth_institution,
                    twelfth_cgpa = twelfth_cgpa,
                    twelfth_board = twelfth_board,
        
                    twelfth_certificate_upload = twelfth_certificate_upload,
            # studentprofile.twelfth_certificate_upload = twelfth_certificate_upload

                    tenth_institution = tenth_institution,
                    tenth_board = tenth_board,
                    tenth_cgpa = tenth_cgpa,
                    tenth_certificate_upload = tenth_certificate_upload,
            # studentprofile.tenth_certificate_upload = tenth_certificate_upload

                    ug_institution = ug_institution,
                    ug_university= ug_university,
                    ug_course = ug_course,
                    ug_cgpa = ug_cgpa,
                    ug_certificate_upload = ug_certificate_upload,
            # studentprofile.ug_certificate_upload = ug_certificate_upload

                    skills=skills,
                    newcourse=newcourse,
                    newcert=newcert,

                    workexperience=workexperience,
                    jobresp=jobresp,
                    period=period,
                    companydetails=companydetails,

                    crime=crime,
                    dtoc=dtoc,
                    doc=doc,
                    nature=nature,
                    resume = resume
                )

            jobapply.save()
            messages.success(request, 'Job submitted successfully.')
            print("Job Apply ID:", jobapply_id)

            return redirect('jobapply', jobapply_id=jobapply_id)  # Use job.id instead of jobapply.id



        context = {
            # 'jobapply': jobapply,
            # 'admin_student':admin_student,
            'sprof':stuprof,
            'jobapply_id': jobapply_id,
            'job':job,
            'certification_status': certification_status
        }
        return render(request, 'student/jobapply.html', context)
    
    else:
        return render(request, 'student/jobapply.html', {'certification_status': certification_status})

# def appliedstudents(request):
    

#     app_stu = JobApplication.objects.filter(job__company=request.user)
#     context = {'app_stu': app_stu}
#     return render(request,'company/appliedstudents.html', context)

 
def appliedstudents(request):
    # Retrieve all Jobs instances associated with the current user
    jobs_instances = Jobs.objects.filter(user=request.user)

    if jobs_instances.exists():
        # If Jobs instances are found, filter JobApplications based on them
        app_stu = JobApplication.objects.filter(job__in=jobs_instances)
    else:
        # If no Jobs instances are found, provide an empty queryset
        app_stu = JobApplication.objects.none()

    context = {'app_stu': app_stu}
    return render(request, 'company/appliedstudents.html', context)

def adminappstudents(request):
    
    app_stu = JobApplication.objects.all()
    context = {'app_stu': app_stu }
    return render(request, 'admin/adminappstudents.html',context)

def admin_shortlist(request):
    jobs_instances = Jobs.objects.all()

    if jobs_instances.exists():
        # If Jobs instances are found, filter JobApplications based on them
        app_stu = JobApplication.objects.all()
    else:
        # If no Jobs instances are found, provide an empty queryset
        app_stu = JobApplication.objects.none()

    context = {'app_stu': app_stu}
    return render(request,'admin/admin_shortlist.html', context)
 
def cfirstround(request):
    jobs_instances = Jobs.objects.filter(user=request.user)

    if jobs_instances.exists():
        # If Jobs instances are found, filter JobApplications based on them
        app_stu = JobApplication.objects.filter(job__in=jobs_instances)
    else:
        # If no Jobs instances are found, provide an empty queryset
        app_stu = JobApplication.objects.none()

    context = {'app_stu': app_stu}
    return render(request,'company/cfirstround.html', context)

@login_required
def sappliedjobs(request, studentprofile_id):
    user=request.user
    app_stu = JobApplication.objects.filter(user=user)
    context = {'app_stu': app_stu, 'studentprofile_id': studentprofile_id}

    return render(request,'sappliedjobs.html',context)




def s_shortlist(request, studentprofile_id):
    user=request.user
    app_stu = JobApplication.objects.filter(user=user)
    context = {'app_stu': app_stu, 'studentprofile_id': studentprofile_id}
    return render(request, 'sfirstround.html', context)



# def studentprofileapp(request, studentprofile_id):
#     app_stu = get_object_or_404(JobApplication, user=request.user)
#     context = {'app_stu': app_stu, 'studentprofile_id': studentprofile_id }
    
#     return render(request,'company/studentprofileapp.html',context)
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def studentprofileapp(request, studentprofile_id):
    print(f"Requested studentprofile_id: {studentprofile_id}")
    print(f"Authenticated user: {request.user}")
    # stuprof = get_object_or_404(StudentProfile, user=request.user)

    # Retrieve the JobApplication based on the user and studentprofile_id
    job_application = get_object_or_404(JobApplication, id=studentprofile_id)
    # job_application = JobApplication.objects.filter(stuprof__id=studentprofile_id)
    print('First Name:', job_application.first_name)
    print('Job' , job_application)
    # Pass the retrieved JobApplication to the template
    context = {'job_application': job_application, 'studentprofile_id': studentprofile_id}
    return render(request, 'company/studentprofileapp.html', context)

def approve_shortlist(request, application_id):
    shortlist = get_object_or_404(JobApplication, id=application_id)
    if request.method == 'POST':
        shortlist.is_approved = JobApplication.APPROVED  # Set it to 'approved'
        shortlist.save()
        
    return redirect('appliedstudents')


def reject_shortlist(request, application_id):
    shortlist = get_object_or_404(JobApplication, id=application_id)
    if request.method == 'POST':
        shortlist.is_approved = JobApplication.REJECTED  # Set it to 'approved'
        shortlist.save()
    return redirect('appliedstudents')