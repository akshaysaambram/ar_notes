from django import forms
from .models import Note, Feedback


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 40}))

    class Meta:

        model = Note
        fields = ['title', 'content']

class FeedbackForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}))

    class Meta:

        model = Feedback
        fields = ['subject', 'body']

