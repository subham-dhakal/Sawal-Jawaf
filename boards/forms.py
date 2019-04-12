from django import forms
from .models import Topic,Post,Board

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'What is on your mind?'}), 
    max_length=4000, help_text='The max length of the text is 4000. ')
    class Meta:
        model= Topic
        fields=['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
