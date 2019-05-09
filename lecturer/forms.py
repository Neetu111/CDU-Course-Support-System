from django import forms

from .models import Lecturer

class lecturerForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Lecturer
		fields = ('LecturerID','password')