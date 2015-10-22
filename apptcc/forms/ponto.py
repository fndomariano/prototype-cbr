#coding: utf-8

from apptcc.models import Rio
from django import forms

class FormPonto(forms.Form):

	latitude = forms.CharField(
		widget = forms.TextInput(
			attrs = {'class': 'form-control'}
		)
	)

	longitude = forms.CharField(
		widget = forms.TextInput(
			attrs = {'class': 'form-control'}
		)
	)

	rio = forms.ModelChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		),
		queryset=Rio.objects.all(),
        empty_label='Selecione um Rio...'
	)