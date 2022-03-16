from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, mobile_no, username, first_name, last_name, password=None):
        if not email:
            raise ValueError ('email is required')
        if not username:
            raise ValueError ('username can not empty it is required')
        if not first_name:
            raise ValueError ('mandatory field')
        if not last_name:
            raise ValueError ('mandatory field')
        if not mobile_no:
            raise ValueError ('Please provide an active phone no.')

        user =  self.model(
            first_name = first_name,
            last_name = last_name,
            username = username, 
            email = self.normalize_email(email),
            mobile_no = mobile_no
        )
        user.set_password(password)
        user.save(using=self._db)
    
    def create_superuser(self,first_name,last_name, username, email, mobile_no, password=None):
        user = self.create_user(
            first_name= first_name,
            last_name= last_name,
            username=username,
            mobile_no= mobile_no,
            email = email,
            password = password
        )
        user.is_admin = True
        user.is_superuser= True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    first_name  = models.CharField(max_length=12)
    last_name =  models.CharField(max_length=12)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    mobile_no = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    joined_date  = models.DateTimeField(auto_now_add=True)  
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'mobile_no', 'first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    
    def has_module_perms(self, app_lebel):
        return True