from django import forms
from .models import Topic,Post,Board

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'What is on your mind?'}), max_length=4000)
    class Meta:
        model= Topic
        fields=['subject', 'message']
