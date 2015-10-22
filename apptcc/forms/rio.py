#coding: utf-8

from apptcc.models import Bacia_Hidrografica
from django import forms

class FormRio(forms.Form):

	nome = forms.CharField(
		widget=forms.TextInput(
			attrs = {'class': 'form-control'}
		)
	)

	dimensao = forms.FloatField(
		widget = forms.TextInput(
			attrs = {'class': 'form-control'}
		)
	)

	bacia_hidrografica = forms.ModelChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		),
		queryset=Bacia_Hidrografica.objects.all(),
        empty_label='Selecione a Bacia Hidrográfica...'
	)


