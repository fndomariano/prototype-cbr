#coding: utf-8

from apptcc.models import Bacia_Hidrografica
from django import forms

class FormRio(forms.Form):

	nome = forms.CharField(
		widget=forms.TextInput()
	)

	dimensao = forms.FloatField(
		widget = forms.TextInput()
	)

	bacia_hidrografica = forms.ModelChoiceField(
		widget = forms.Select(),
		queryset=Bacia_Hidrografica.objects.all(),
        empty_label='Selecione a Bacia Hidrográfica...'
	)


