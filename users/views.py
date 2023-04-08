from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import UnauthenticatedUserMixin


# Create your views here.
class UserRegisterView(UnauthenticatedUserMixin, FormView):

    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Your account has been created! You can now log in.")
        return super(UserRegisterView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'users/profile.html'    
    

@login_required
def update_profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/edit_profile.html', context)
