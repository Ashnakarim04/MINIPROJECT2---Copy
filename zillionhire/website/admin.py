from django.contrib import admin
from . models import Jobs, CompanyProfile, Students,AdminStudent,StudentProfile,CompanyApprove,JobApplication



# Register your models here.
# from . import models
# # Register your models here.

admin.site.register(Jobs)
admin.site.register(CompanyProfile)
admin.site.register(Students)
admin.site.register(AdminStudent)
admin.site.register(StudentProfile)
admin.site.register(CompanyApprove)
admin.site.register(JobApplication)
# admin.site.register(CustomUser)