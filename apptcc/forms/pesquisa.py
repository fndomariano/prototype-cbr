#coding: utf-8

from apptcc.models import Entorno
from django import forms

class FormPesquisa(forms.Form):

	classificacoes = (
		('otima', 'Ótima'), 
		('boa', 'Boa'), 
		('regular', 'Regular'),
		('ruim', 'Ruim'),
		('pessima', 'Péssima')
	)

	iap = forms.ChoiceField(
		widget = forms.Select(),
		choices = classificacoes
	)

	iva = forms.ChoiceField(
		widget = forms.Select(),
		choices = classificacoes
	)

	entorno = forms.ModelChoiceField(
		widget = forms.Select(), 
		queryset = Entorno.objects.all(),
		empty_label = "Selecione uma variável de entorno"
	)

	risco = forms.ChoiceField(
		widget = forms.Select(), 
		choices = (('B', 'Baixo'), ('M', 'Médio'), ('A', 'Alto'))
	)