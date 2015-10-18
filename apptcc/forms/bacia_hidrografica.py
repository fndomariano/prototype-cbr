#coding: utf-8

from django import forms

class FormBaciaHidrografica(forms.Form):

	nome = forms.CharField(
		widget = forms.TextInput()
	)
