
# user/views.
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import UserProfile, WorkerProfile,CustomUser
from .forms import SignUpForm, LogInForm, UpdateUserForm, UpdateProfileForm, UpdateWorkerForm
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
=======
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import UserProfile
>>>>>>> origin/tasks

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()   
    return render(request, 'user/signup.html', {'form': form})
  


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'user/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('user:login'))

from django.contrib.auth.decorators import login_required




# @login_required
# def profile(request) :
#     return render(request, 'user/profile.html')

@login_required
def profile(request):
<<<<<<< HEAD
    if request.user.is_authenticated:
        user=request.user.email
        c=CustomUser.objects.get(email=user)
        
        u=UserProfile.objects.get(user=c)
        
        w=WorkerProfile.objects.get(worker=u)
        
        #w = get_object_or_404(WorkerProfile, worker__user__username=user)
        #u=get_object_or_404(UserProfile, user__username=user)
    return render(request, 'user/profile.html', {'w':w,'u': u,'request.user':request.user})
    #return render(request, 'user/profile.html')
def editprofile(request):
=======
    if request.method == 'POST':
        u_form = AddDetails(request.POST, instance=request.user)
        p_form = AddWorkerDetails(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = AddDetails(instance=request.user)
        p_form = AddWorkerDetails(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def  edit_profile(request):
>>>>>>> origin/tasks
    if request.method == 'POST':
        
        #user_form = UpdateUserForm(request.POST, instance=request.user)
        #profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        worker_form=UpdateWorkerForm(request.POST,instance=request.user ) #check if .profile should be there
        
        
        # if user_form.is_valid():
            
        #   user_form.save()
        
        if worker_form.is_valid():
            user=request.user.email
            c=CustomUser.objects.get(email=user)
            u=UserProfile.objects.get(user=c)

            worker1=worker_form.save()
            worker1.worker=WorkerProfile.objects.get(worker=u)
            worker1.save()

            #return redirect('profile')

        
    else:
<<<<<<< HEAD
        #user_form = UpdateUserForm(instance=request.user)
        #profile_form = UpdateProfileForm(instance=request.user)
        worker_form=UpdateWorkerForm(instance=request.user)
    #return render(request, 'user/editprofile.html', {'user_form': user_form, 'profile_form': profile_form, 'worker_form' : worker_form})
    return render(request, 'user/editprofile.html', {'worker_form': worker_form})
=======
        form = AddDetails()
        form1=AddWorkerDetails()
    return render(request, 'user/edit_profile.html', {'form': form})


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
                        
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
>>>>>>> origin/tasks
