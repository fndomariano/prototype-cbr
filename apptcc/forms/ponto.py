#coding: utf-8

from apptcc.models import Rio
from django import forms

class FormPonto(forms.Form):

	latitude = forms.CharField(
		widget = forms.TextInput()
	)

	longitude = forms.CharField(
		widget = forms.TextInput()
	)

	rio = forms.ModelChoiceField(
		widget = forms.Select(),
		queryset=Rio.objects.all(),
        empty_label='Selecione um Rio...'
	)