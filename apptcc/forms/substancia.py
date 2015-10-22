#coding: utf-8

from django import forms

class FormSubstancia(forms.Form):

	nome = forms.CharField(
		widget = forms.TextInput(
			attrs = {'class':'form-control'}
		)
	)