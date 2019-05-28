from django import forms

from .models import *

class lecturerForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Lecturer
		fields = ('Name','password')