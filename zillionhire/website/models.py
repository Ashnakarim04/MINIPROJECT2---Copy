from django.db import models
from django.contrib.auth.models import User
# from imagekit.processors import ResizeToFit
# from imagekit.models import ProcessedImageField

# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import AbstractUser, BaseUserManager

# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# from .manager import UserManager

 




# class UserManager(BaseUserManager):
#     # ... (existing methods)

#     def create_user(self, email, password=None, role=None, company_name=None, ceo=None, headquarters=None, contact=None):
#         if not email:
#             raise ValueError('User must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#             role=role,
#             company_name=company_name,
#             ceo=ceo,
#             headquarters=headquarters,
#             contact=contact,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password=None, company_name=None, ceo=None, headquarters=None, contact=None):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             company_name=company_name,
#             ceo=ceo,
#             headquarters=headquarters,
#             contact=contact, 
#         )
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superadmin = True
#         user.role=3
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractUser):
#     COMPANY = 1
#     STUDENT = 2
#     ADMIN = 3

#     ROLE_CHOICE = (
#         (COMPANY, 'COMPANY'),
#         (STUDENT, 'STUDENT'),
#         (ADMIN, 'ADMIN'),
#     )
 
#     username = None
#     first_name = None
#     last_name = None
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=128)
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True, default=STUDENT)

#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     ceo = models.CharField(max_length=100, blank=True, null=True)
#     headquarters = models.CharField(max_length=100, blank=True, null=True)
#     contact = models.CharField(max_length=15, blank=True, null=True)

#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superadmin = models.BooleanField(default=False)

#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True
class Jobs(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'
    
    APPROVAL_CHOICES = [
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    ]
    cname = models.CharField(max_length=100,default=" ")
    jname = models.CharField(max_length=100,default=" ")
    salary = models.IntegerField()
    email = models.EmailField(max_length=100)
    sdate = models.CharField(max_length=100)
    edate = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    job_descriptions = models.CharField(max_length=600,null=True, blank=True)
    responsibilities = models.CharField(max_length=600,null=True, blank=True)
    preferred_skills = models.CharField(max_length=600,null=True, blank=True)
    qualifications = models.CharField(max_length=600,null=True, blank=True)
    is_active=models.BooleanField(default=True)
    required_tenth_cgpa = models.FloatField(null=True, blank=True)
    required_twelfth_cgpa = models.FloatField(null=True, blank=True)
    required_current_cgpa = models.FloatField(null=True, blank=True)
    required_backlog = models.IntegerField(null=True, blank=True)

    # criteria= models.ImageField(upload_to='images/',blank= True,null=True)
    # is_approved = models.BooleanField(default=False)
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )
    def __str__(self):
        return self.email 





class CompanyProfile(models.Model): 
    
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'
    
    APPROVAL_CHOICES = [
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    companyname = models.CharField(max_length=100, default=" ")
    contact = models.CharField(max_length=15,blank=True)
    addressline1 = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100,blank=True)
    companydp=models.ImageField(upload_to='images/',blank= True,null=True)
    reset_password = models.CharField(max_length=128, null=True, blank=True)  # New field for reset password

    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )

    is_active= models.BooleanField(default=True)
    def __str__(self):
        return self.companyname
    
    # password = models.CharField(max_length=50)

    # def set_password(self, password):
    #      # Hash and set the password
    #      self.admin_set_password = make_password(password, default=make_password('default_password'))
class Students(models.Model): 
    
    sname = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    course = models.CharField(max_length=50, choices=[('B.Tech', 'B.Tech'), ('MCA', 'MCA')],null=True, blank=True)
    department = models.CharField(max_length=100, choices=[('ECE', 'ECE'), ('CSE', 'CSE'),('Integrated MCA', 'Integrated MCA'),('Regular MCA', 'Regular MCA')],null=True, blank=True)
    semester = models.CharField(max_length=100, choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8'), ('Semester 9', 'Semester 9'), ('Semester 10', 'Semester 10')],null=True, blank=True)
    # is_active=models.BooleanField(default=True)
    is_active: type[models.BooleanField] = models.BooleanField(default=True)

    def __str__(self):
        return self.email 
 
class StuProfile(models.Model): 
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    companyname = models.CharField(max_length=100, default="default")
    course = models.CharField(max_length=100, default="default")
    # ceo = models.CharField(max_length=100, default="default")
    contact = models.CharField(max_length=15,default="default")
    addressline1 = models.CharField(max_length=100, blank=True)
  
    website = models.CharField(max_length=100,default="www.example.com")
    city = models.CharField(max_length=100,default=" eg: Kochi")
    district= models.CharField(max_length=100,default=" eg:Ernakulam")
    state = models.CharField(max_length=100,default=" eg:Kerala ")
    country = models.CharField(max_length=100,default=" eg: India")
    pincode = models.CharField(max_length=15,default=" eg:686403")
    companydp=models.ImageField(upload_to='images/',blank= True,null=True)
    is_active= models.BooleanField(default=True)
    def __str__(self):
        return self.ceo
    
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'Student {self.username}'


from django.contrib.auth.models import User 
from django.db import models

class AdminStudent(models.Model):
    user = models.OneToOneField(User, related_name="student_profile", on_delete=models.CASCADE, null=True)
    admission_no = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)

    def get_full_name(self):
        if self.user:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return "Unknown"

    def __str__(self):
        return self.get_full_name()

from django.db import models

class StudentProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    adminstu = models.OneToOneField(AdminStudent, on_delete=models.CASCADE, null=True)
    admission_no = models.CharField(max_length=20,blank= True,null=True)
    first_name = models.CharField(max_length=50,blank= True,null=True)
    last_name = models.CharField(max_length=50,blank= True,null=True)
    dob = models.DateField(blank=True, null=True, default=None)
    # gender = models.CharField(max_length=10)
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female'),('Others', 'Others')],null=True, blank=True)
    reset_password = models.CharField(max_length=128, null=True, blank=True)  # New field for reset password
    nationality = models.CharField(max_length=50,blank= True,null=True)
    religion = models.CharField(max_length=50,blank= True,null=True)
    profile_photo = models.ImageField(upload_to='images/',blank= True,null=True)

    reset_password = models.CharField(max_length=128, null=True, blank=True)  # New field for reset password


    email = models.EmailField(default=" ")
    phone = models.CharField(max_length=15,blank= True,null=True)
    present_address = models.TextField(blank= True,null=True)
    permanent_address = models.TextField(blank= True,null=True)

    course = models.CharField(max_length=50, choices=[('B.Tech', 'B.Tech'), ('MCA', 'MCA')],null=True, blank=True)
    # department = models.CharField(max_length=700, choices=[('Electronics and Communication engineering', 'Electronics and Communication engineering'), ('Computer Science Engineering', 'Computer Science Engineering'),('Information Technology','Information Technology')('Integrated MCA', 'Integrated MCA'),('Regular MCA', 'Regular MCA')],null=True, blank=True)
    department = models.CharField(
    max_length=700,
    choices=[
        ('Electronics and Communication engineering', 'Electronics and Communication engineering'),
        ('Computer Science Engineering', 'Computer Science Engineering'),
        ('Information Technology', 'Information Technology'),  # Added comma after the previous choice
        ('Integrated MCA', 'Integrated MCA'),  # Added comma after the previous choice
        ('Regular MCA', 'Regular MCA')
    ],
    null=True,
    blank=True
)
   
   
   
   
    academic_year = models.CharField(max_length=10,blank= True,null=True)
    current_semester = models.CharField(max_length=10,blank= True,null=True)
    c_cgpa = models.FloatField(max_length=10,blank= True,null=True)
    c_backlog=models.CharField(max_length=100,blank= True,null=True)
    # c_backlog=models.FloatField(blank= True,null=True)

    twelfth_institution = models.CharField(max_length=100,blank= True,null=True)
    twelfth_cgpa = models.FloatField(blank= True,null=True)
    twelfth_course = models.CharField(max_length=100,blank= True,null=True)
    twelfth_certificate_upload = models.FileField(upload_to='images/',blank= True,null=True)

    tenth_institution = models.CharField(max_length=100,blank= True,null=True)
    tenth_cgpa = models.FloatField(blank= True,null=True)
    tenth_course = models.CharField(max_length=100,blank= True,null=True)
    tenth_certificate_upload = models.FileField(upload_to='images/',blank= True,null=True)
    
    ug_institution = models.CharField(max_length=100,blank= True,null=True)
    ug_cgpa = models.CharField(max_length=100,blank= True,null=True)
    ug_course = models.CharField(max_length=100,blank= True,null=True)
    ug_certificate_upload = models.FileField(upload_to='images/',blank= True,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.admission_no}'

class EditRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  
    admission_no = models.CharField(max_length=20,blank= True,null=True)
    email = models.EmailField(default=" ")
    reason = models.CharField(max_length=20, blank=True,default=" ",null=True)
    proof = models.FileField(upload_to='images/',blank= True,null=True)
    
    def __str__(self):
        return f'{self.email} {self.admission_no}'

class CompanyApprove(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  
    companyname = models.CharField(max_length=20,blank= True,null=True)
    email = models.EmailField(default=" ")
    
    
    def __str__(self):
        return self.companyname


class JobApplication(models.Model):
    
    APPROVED = 'approved'
    PENDING = 'pending'
    REJECTED ='rejected'
    
    APPROVAL_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
        (REJECTED,'rejected')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True)
    stuprof = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True)
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )

    cname=models.CharField(max_length=100,blank= True,null=True)
    jname=models.CharField(max_length=100,blank= True,null=True)
    first_name = models.CharField(max_length=50,blank= True,null=True)
    last_name = models.CharField(max_length=50,blank= True,null=True)
    dob = models.CharField(max_length=10,blank= True,null=True)
    # gender = models.CharField(max_length=10)
    gender = models.CharField(max_length=50,blank= True,null=True )
    nationality = models.CharField(max_length=50,blank= True,null=True)
    # religion = models.CharField(max_length=50,blank= True,null=True)
    profile_photo = models.ImageField(upload_to='images/',blank= True,null=True)

    

    email = models.EmailField(max_length=50,blank= True,null=True)
    phone = models.CharField(max_length=15,blank= True,null=True)
    area_code = models.CharField(max_length=300, choices=[('+1 (United States)', '+1 (United States)'), ('+44 (United Kingdom)', '+44 (United Kingdom)'), ('+91 (India)', '+91 (India)'), ('+61 (Australia)', '+61 (Australia)')], null=True, blank=True)
    present_address = models.TextField(blank= True,null=True)
    permanent_address = models.TextField(blank= True,null=True)

    
    # current_semester = models.CharField(max_length=10,blank= True,null=True)
    # cgpa = models.FloatField(blank= True,null=True)

    twelfth_institution = models.CharField(max_length=100,blank= True,null=True)
    twelfth_cgpa = models.FloatField(blank= True,null=True)
    twelfth_board = models.CharField(max_length=100,blank= True,null=True)
    twelfth_certificate_upload = models.FileField(upload_to='images/',blank= True,null=True)

    tenth_institution = models.CharField(max_length=100,blank= True,null=True)
    tenth_cgpa = models.FloatField(blank= True,null=True)
    tenth_board = models.CharField(max_length=100,blank= True,null=True)
    tenth_certificate_upload = models.FileField(upload_to='images/',blank= True,null=True)
    
    ug_course = models.CharField(max_length=100,blank= True,null=True)
    ug_institution = models.CharField(max_length=100,blank= True,null=True)
    ug_cgpa = models.CharField(max_length=100,blank= True,null=True)
    ug_university = models.CharField(max_length=100,blank= True,null=True)
    ug_certificate_upload = models.FileField(upload_to='images/',blank= True,null=True)

    c_course=models.CharField(max_length=100,blank= True,null=True)
    c_institution=models.CharField(max_length=100,blank= True,null=True)
    c_university=models.CharField(max_length=100,blank= True,null=True)
    c_cgpa = models.FloatField(blank= True,null=True)
    c_backlog=models.CharField(max_length=100,blank= True,null=True)
    academic_year = models.CharField(max_length=10,blank= True,null=True)

    skills=models.CharField(max_length=700,blank= True,null=True)
    newcourse=models.CharField(max_length=100,blank= True,null=True)
    newcert=models.FileField(upload_to='images/',blank= True,null=True)

    workexperience = models.CharField(max_length=70, choices=[('No', 'No'), ('Yes', 'Yes'),], null=True, blank=True)
    # jobname=models.CharField(max_length=100,blank= True,null=True)
    period=models.CharField(max_length=100,blank= True,null=True)
    jobresp=models.CharField(max_length=100,blank= True,null=True)
    companydetails=models.CharField(max_length=400,blank= True,null=True)

    crime = models.CharField(max_length=70, choices=[('No', 'No'), ('Yes', 'Yes'),], null=True, blank=True)
    dtoc=models.CharField(max_length=100,blank= True,null=True)
    doc=models.CharField(max_length=100,blank= True,null=True)
    nature=models.CharField(max_length=100,blank= True,null=True)

    resume=models.FileField(upload_to='images/',blank= True,null=True)


