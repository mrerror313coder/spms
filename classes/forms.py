from django import forms
from .models import Class
from users.models import CustomUser

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class AddStudentsForm(forms.Form):
    students = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter(user_type='student'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
