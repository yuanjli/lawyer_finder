from django import forms
from .models import Lawyer

class LawyerForm(forms.ModelForm):
	class Meta:
		model = Lawyer
		fields = ('name', 'specialties', 'ratings', 'experience', 'stories', 'photo_url', 'numbers',)