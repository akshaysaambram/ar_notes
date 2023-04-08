from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .decorators import UserNoteMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import NoteForm, FeedbackForm


# Create your views here.
def home(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                form.instance.owner = request.user
            form.save()
            messages.success(request, "The feedback has been successfully submitted. Thanks for your submission.")
            return redirect('home')
    else:
        form = FeedbackForm()

    context = {
        'request': request,
        'form': form,
    }

    return render(request, 'notes/home.html', context)


class NoteListView(UserNoteMixin, ListView):

    paginate_by = 6
    ordering = ['-created_at']
    context_object_name = 'notes'
    template_name = 'notes/note_list.html'


class NoteCreateView(UserNoteMixin, CreateView):

    form_class = NoteForm
    template_name = 'notes/note_create.html'
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NoteCreateView, self).form_valid(form)


class NoteUpdateView(UserNoteMixin, UpdateView):

    form_class = NoteForm
    template_name = 'notes/note_update.html'
    success_url = reverse_lazy('note-list')


class NoteDeleteView(UserNoteMixin, DeleteView):

    context_object_name = 'note'
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')


class FeedbackView(CreateView):

    form_class = FeedbackForm
    template_name = 'notes/home.html'    
    success_url = reverse_lazy('home')

