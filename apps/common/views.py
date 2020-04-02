from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm, UserForm, ProfileForm 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from apps.userprofile.models import Profile

class HomeView(TemplateView):
    template_name = 'common/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm # Loading UserForm
    profile_form = ProfileForm # Loading ProfileForm
    template_name = 'common/profile-update.html'

    # POST METHOD
    def post(self, request):
        post_data = request.POST or None # Load data submitted
        file_data = request.FILES or None # Load data image submitted

        # First param is the request POST or FILE and secondone is the instances of the data which we want
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        # If the form is valid we save it, sent a successfully message and redirect it to the profile view
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was succssesfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))
        
        # Otherwise return the context
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    # GET METHOD is get this code is not be running
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

