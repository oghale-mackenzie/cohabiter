from django import forms
from django.contrib.auth.models import User
from .models import Profile

CHOICES=[('Male','M'),('Female','F')]

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
	gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('phone_number','gender','date_of_birth', 'photo')