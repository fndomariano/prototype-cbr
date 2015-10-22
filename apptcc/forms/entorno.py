#codind: utf-8

from django import forms

class FormEntorno(forms.Form):

	variavel_entorno = forms.CharField(
		widget = forms.TextInput(
			attrs = {'class': 'form-control'}
		)
	)