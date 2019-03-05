from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','fullname']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '.co.ke' in email:
            raise forms.ValidationError("Use a company Email.")
        return email


class ContactForm(forms.Form):
    email = forms.CharField(max_length=255)
    fullname = forms.CharField(max_length=255)
    message = forms.CharField(max_length=400)

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not '.co.ke' in email:
    #         raise forms.ValidationError("Use Company Email")
    #     return self.email



