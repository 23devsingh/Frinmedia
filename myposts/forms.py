from django import forms
from .models import PostImage


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', 'description', 'privacy']  # Include fields you want to display
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Write a description...',
                'rows': 4,
                'class': 'form-control',
            }),
            'privacy': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })
