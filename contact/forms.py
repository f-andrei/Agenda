
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class': 'classe-a',
            'placeholder': 'Escreva aqui'
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajdua para o usuário'
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
        
        if first_name == last_name:
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        
        return first_name


