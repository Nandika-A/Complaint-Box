from user import views as user_views
from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #To direct user to register page
<<<<<<< HEAD
    path('user_register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name = 'logout'),
    path('profile/', user_views.profile, name= 'profile'),
    path("password_reset", auth_views.password_reset_request, name="password_reset"),#**check if it is user or auth
    path('edit_profile/', user_views.edit_profile, name= 'edit-profile'),
=======
    path('/user_register/', user_views.register, name = 'register'),
    path('/login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('/logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name = 'logout'),
    path('/profile/', user_views.profile, name= 'profile'),
    path('/password_reset', auth_views.password_reset_request, name="password_reset"),#**check if it is user or auth
    #path('edit_profile/', user_views.edit_profile, name= 'edit_profile'),
>>>>>>> 8feba73d58496b1b42cf29e6ebc60bf4d1d27a02
    path ('',include('home.urls')),
]
#image
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
