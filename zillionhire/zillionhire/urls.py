"""
URL configuration for zillionhire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import loginn,reg, index, loggout,sample2, jobs, studentloginn, cindex, sindex, aboutuser, contactuser, cprofile, cjob, postjob, addjob,edit_job, admin_login, admin_index2,admin_profile,admin_editprofile,admin_company,addstudents,jobslist, admin_poststudent,companyprofilelist, search_company, search_student,edit_student, ad_cprofile, download_criteria, search_course, ad_deletecompany, search_job,adsearch_company
from website import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from website.views import StudentDataAPIView

 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('', sample, name=''),
    path('',views.index, name="index"),
    path('jobs',views.jobs, name="jobs"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    # path('blog',views.blog, name="blog"),
    path('sample2', sample2, name='sample2'),
    path('studentloginn', studentloginn, name='studentloginn'),
    path('loginn', loginn, name='loginn'),
    path('reg', reg, name='reg'), 
    path('loggout', loggout, name='loggout'),
    path('cindex', cindex, name='cindex'),
    path('aboutuser', aboutuser, name='aboutuser'),
    path('contactuser', contactuser, name='contactuser'),
    path('cprofile/<int:companyprofile_id>/', cprofile, name='cprofile'),
    path('cprofile/<int:user_id>/', views.approve_comp, name='approve_comp'),
    path('approve_comp/<int:company_id>/', views.approve_comp, name='approve_comp'),
    # path('postjob/<int:companyprofile_id>/', postjob, name='postjob'),
    path('cjob', cjob, name='cjob'),
    path('postjob/', views.postjob, name='postjob'),
    path('addjob', addjob, name='addjob'),
    # path('addjob/<int:obj_id>/', views.addjob, name='addjob'),
    path('sindex', sindex, name='sindex'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("",include("allauth.urls")),
    path('edit/job/<int:job_id>/', views.edit_job, name='edit_job'), 
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),  
    path('admin_login', admin_login, name='admin_login'),
    # path('admin_index', admin_index, name='admin_index'),
    path('admin_index2', admin_index2, name='admin_index2'),
    path('admin_profile', admin_profile, name='admin_profile'),
    path('ad_cprofile', ad_cprofile, name='ad_cprofile'),
    
    # path('admin_students', admin_students, name='admin_students'),
    path('admin_company', admin_company, name='admin_company'),
    path('admin_edit-profile', admin_editprofile, name='admin_editprofile'),
    path('addstudents', addstudents, name='addstudents'),
    path('jobslist',jobslist, name='jobslist'),
    # path('addelete_job',views.addelete_job, name='addelete_job'),
    # path('admin_studentadd',admin_studentadd,name='admin_studentadd'),
    path('admin_poststudent/', views.admin_poststudent, name='admin_poststudent'),
    path('companyprofilelist',companyprofilelist,name='companyprofilelist'),
    path('search_company', search_company, name='search_company'),
    path('search_job', search_job, name='search_job'),
    # path('search_jobs/', views.search_jobs, name='search_jobs'),
    path('adsearch_company', adsearch_company, name='adsearch_company'),
    path('delete_company', views.delete_company, name='delete_company'),
    path('ad_deletecompany/<int:comp_id>/', views.ad_deletecompany, name='ad_deletecompany'),

    path('search_student', search_student, name='search_student'),
    path('search_student2', views.search_student2, name='search_student2'),
    # path('edit_student',edit_student,name='edit_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('ad_studentlist', views.ad_studentlist, name='ad_studentlist'),
    # path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('download_criteria/<int:job_id>/', download_criteria.as_view(), name='download_criteria'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
     
    path('companyapprove',views.companyapprove, name='companyapprove'),
    path('search_course',search_course, name='search_course'),
    path('profc',views.profc, name='profc'),
    path('search_course',search_course, name='search_course'),
    path('stureg',views.stureg, name='stureg'),
    path('students/', views.student_list, name='student_list'),
    # path('api/get_student_data/', StudentDataAPIView.as_view(), name='get_student_data'),
    # path('asha_approved_appo', views.asha_approved_appointments, name='asha_approved_appo'),
    # path('approve-appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('add_student/', views.add_student, name='add_student'),
    path('admin_addstudents/', views.admin_addstudents, name='admin_addstudents'),
    # path('sdashboard/', views.sdashboard, name='sdashboard'),
    path('sprofile/<int:studentprofile_id>/', views.sprofile, name='sprofile'),
    path('jobapply/<int:jobapply_id>/', views.jobapply, name='jobapply'),

    # path('sprofile/', views.sprofile, name='sprofile'),
    # path('sprofile/<int:studentprofile_id>/', views.sprofile, name='sprofile'),
    path('cindex/', views.cindex, name='cindex'),
    path('srequest/', views.srequest, name='srequest'),
    path('adpostjob/', views.adpostjob, name='adpostjob'),
    path('job_approve/<int:studentprofile_id>/', views.job_approve, name='job_approve'),


    path('approved_jobs/<int:job_id>/', views.approved_jobs, name='approved_jobs'),
    path('eligibility', views.eligibility, name='eligibility'),

    path('appliedstudents', views.appliedstudents, name='appliedstudents'),
    path('adminappstudents', views.adminappstudents, name='adminappstudents'),
    path('sappliedjobs/<int:studentprofile_id>/', views.sappliedjobs, name='sappliedjobs'),
    path('s_shortlist/<int:studentprofile_id>/', views.s_shortlist, name='s_shortlist'),
    path('cfirstround', views.cfirstround, name='cfirstround'),
    path('admin_shortlist', views.admin_shortlist, name='admin_shortlist'),
    path('studentprofileapp/<int:studentprofile_id>/', views.studentprofileapp, name='studentprofileapp'), 
    path('reject_shortlist/<int:application_id>/', views.reject_shortlist, name='reject_shortlist'),
    path('approve_shortlist/<int:application_id>/', views.approve_shortlist, name='approve_shortlist'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

