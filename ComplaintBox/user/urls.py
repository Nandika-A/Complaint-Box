# user/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import activate

from .views import signup, log_in, log_out,profile,editprofile
app_name = "user"
urlpatterns = [
<<<<<<< HEAD
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('editprofile/', editprofile, name='editprofile'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'), 
    #path('accounts/', include('allauth.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    #To direct user to register page
    path('user_register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name = 'logout'),
    path('profile/', user_views.profile, name= 'profile'),
    path("password_reset", auth_views.password_reset_request, name="password_reset"),#**check if it is user or auth
    path('edit_profile/', user_views.edit_profile, name= 'edit_profile'),
    path ('',include('home.urls')),
]
#image
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> origin/tasks
