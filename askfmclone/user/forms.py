from django import forms
from django.core import validators
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
                   max_length=20,
                   label='Username')
    password = forms.CharField(
                   widget=forms.PasswordInput,
                   max_length=25,
                   min_length=6)


class RegistrationForm(forms.Form):
    username = forms.CharField(
                   max_length=20,
                   label='Username',
                   required=True,
                   validators=[
                       validators.MinLengthValidator(
                            4,
                            message='Username must be at least 4 characters.'),
                       validators.RegexValidator(
                            regex=r'^([\._\-a-zA-Z0-9])+$',
                            message='Username can only contain: alphabets, numbers and (. , -, _).'),
                       validators.RegexValidator(
                            regex=r'^[a-zA-Z]+',
                            message='Username must begin with a letter.'),
                       ]
               )
    email = forms.CharField(max_length=256,
                            label='Email Address',
                            required=True,
                            validators=[validators.EmailValidator()])
    password = forms.CharField(
                   widget=forms.PasswordInput,
                   label='Password',
                   max_length=25,
                   required=True,
                   validators=[
                       validators.RegexValidator(
                        r'\d+',
                        message='Password must contain a digit'),
                       validators.RegexValidator(
                        r'[a-zA-Z]+',
                        message='Password must contain an alphabet'),
                       validators.MinLengthValidator(
                        6, 'Password must contain at least 6 characters.'),
                       validators.MaxLengthValidator(
                        25, 'Password must contain less than 25 characters.'),
                   ]
               )
    password_confirm = forms.CharField(
                           widget=forms.PasswordInput,
                           max_length=25,
                           required=True,
                           label='Confirm Password'
                       )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {
                'required': '{} can not be empty.'.format(field.label)
            }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            username = username.lower()
            users = User.objects.filter(username=username)
            if len(users):
                raise forms.ValidationError(
                        '{} is not available. Choose something else.'.format(
                                                                    username))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
            users = User.objects.filter(email=email)
            if len(users):
                raise forms.ValidationError(
                        '{} is already associated to another account.'.format(
                                                                        email))
        return email

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Passwords do not match.')

        return cleaned_data
