from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,UserProfile,WorkerProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
=======
from .models import UserProfile, WorkerProfile
# Register your models here.
>>>>>>> origin/tasks
admin.site.register(UserProfile)
admin.site.register(WorkerProfile)