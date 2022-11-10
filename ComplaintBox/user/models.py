<<<<<<< HEAD
=======

from email.policy import default
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.postgres.fields import JSONField
from unittest.util import _MAX_LENGTH
>>>>>>> origin/tasks
from django.db import models
from django.core.validators import MaxValueValidator
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from PIL import Image 
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()
class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')  #images will get saved in directory called profile_pics
    
<<<<<<< HEAD
    # Star= models.JSONField(
    #     models.DecimalField(blank=True, validators=[
    #         MaxValueValidator(5)], decimal_places = 2, max_digits = 3),
    #     default = []
    # )
    phone_no= models.CharField(default=None,max_length=50)
    address = models.TextField(default = None)
    star=models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    # preference= JSONField(
    #     models.DecimalField(blank=True, validators=[
    #         MaxValueValidator(5)], decimal_places = 2, max_digits = 3),
    #     size=2,default = None
    # )
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

=======
    Star= models.JSONField(
        models.DecimalField(blank=True, validators=[
            MaxValueValidator(5)], decimal_places = 2, max_digits = 3),
        default = [], blank = True
    )
    
    phone_no= models.CharField(default=None,max_length=50)
    
    preference= models.JSONField(default=dict, blank=True)

    
    
    
    phone_no= models.CharField(default=None,max_length=50)

    address = models.TextField(default = None)
    '''
    Star= ArrayField(
        models.DecimalField(blank=True, validators=[
            MaxValueValidator(5)], decimal_places = 2, max_digits = 3),
        size=2,default = None
    )
    '''
    REQUIRED_FIELDS=['user']
    USERNAME_FIELD = 'user'
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.user.username} Profile'  #will dispaly in a nice way otherwise will return object name

    def save(self):
        super().save()
>>>>>>> origin/tasks
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
<<<<<<< HEAD

=======
>>>>>>> origin/tasks
class WorkerProfile(models.Model):
    worker =models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100, default=None)
    biodata = models.TextField(default = None)
<<<<<<< HEAD
    star=models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    #UPI = models.CharField(max_length=100, default=None)
=======
    no_of_jobs = models.IntegerField(default = 0)
    Star= models.JSONField(default=list, blank=True)
    
'''    
class Usermanager(models.Manager): #to separate user and worker data.
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = UserProfile.Role.USER) 
    
class UserData(UserProfile):
    objects = Usermanager()
    base_role = UserProfile.Role.USER
    class Meta:
        proxy = True #won't create a new table for user
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = UserProfile.Role.USER
        return super().save(*args, **kwargs)
    @property #to access additional fields in user model
    def more(self):
        return Usermore.objects.filter(user_id=self.id)
    
class Usermore(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,null=True)
    address = models.TextField(default = None)
    preference= models.JSONField(null=True, default=dict)
    USERNAME_FIELD = 'user'
     
class Workermanager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = UserProfile.Role.WORKER) 
    
class WorkerData(UserProfile):
    objects = Workermanager()
    base_role = UserProfile.Role.WORKER
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = UserProfile.Role.USER
        return super().save(*args, **kwargs)
    @property
    def more(self):
        return Workermore.objects.filter(user_id=self.id)
    
class Workermore(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,null=True)
    biodata = models.TextField(default = None)
    profession = models.CharField(max_length=100, default=None)
'''
>>>>>>> origin/tasks
