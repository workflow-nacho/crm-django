from django.contrib import admin
from django.urls import path
from apps.common.views import HomeView, SignUpView, DashboardView, ProfileView, ProfileUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),

    # Authentication 
    path('login/',
        auth_views.LoginView.as_view(template_name='common/login.html'), 
        name='login'
    ),
    path('logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
    path('change-password/', 
        auth_views.PasswordChangeView.as_view(template_name='common/change-password.html',
        success_url = '/'),
        name= 'change-password'
    ),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


    # ************ FORGET PASSWORD *************************
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

# Extending User Model Using a Proxy Model require to import the following:
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)