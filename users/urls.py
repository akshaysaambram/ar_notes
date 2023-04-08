from . import views
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/', views.update_profile, name='profile-update'),

    path('password/', PasswordChangeView.as_view(template_name='users/password_change.html', success_url = reverse_lazy('password-success')), name='password-change'),
    path('password_success/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password-success'),
]