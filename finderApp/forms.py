from django import forms
from .models import Lawyer, UserAnswer

class LawyerForm(forms.ModelForm):
	class Meta:
		model = Lawyer
		fields = ('name', 'specialties', 'ratings', 'experience', 'stories', 'photo_url', 'numbers',)



class UserAnswerForm(forms.ModelForm):
	"""docstring for UserAnswerForm"""
	class Meta:
		model = UserAnswer
		fields = ('question',)
		