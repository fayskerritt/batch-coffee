from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder and classes and remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment': 'Your Comment',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'comment-input'
            self.fields[field].label = False
