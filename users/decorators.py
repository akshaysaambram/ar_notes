from django.urls import reverse
from django.shortcuts import redirect

class UnauthenticatedUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('note-list')
        return super().dispatch(request, *args, **kwargs)
