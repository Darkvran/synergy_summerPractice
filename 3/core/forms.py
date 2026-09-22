from django import forms
from .models import UserProfile

class NameForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя...'
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError("Поле имени не может быть пустым.")
        return name.strip()