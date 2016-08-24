from django import forms
from django.core.exceptions import ValidationError


class FilmeForm(forms.ModelForm):
	def clean(self):
		cleaned_data = super(FilmeForm, self).clean()
		oscars = cleaned_data.get("numero_de_oscar")
		if (oscars > 10):
			raise ValidationError(u'Número inválido de premiações')