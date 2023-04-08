from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin


class UserNoteMixin(LoginRequiredMixin):
    """
    Mixin for views that require the user to be logged in and only allow them to
    access notes that they own.
    """
    model = Note
    queryset = Note.objects.all()

    def get_queryset(self):
        """
        Only return notes that belong to the current user.
        """
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)