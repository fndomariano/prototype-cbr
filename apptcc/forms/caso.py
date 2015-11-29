#coding: utf-8

from apptcc.models import Entorno, Monitoramento
from django import forms

class FormCaso(forms.Form):
	
	classificacoes = (
		('otima', 'Ótima'), 
		('boa', 'Boa'), 
		('regular', 'Regular'),
		('ruim', 'Ruim'),
		('pessima', 'Péssima')
	)

	iap = forms.ChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		),
		choices = classificacoes
	)

	iva = forms.ChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		),
		choices = classificacoes
	)

	entorno = forms.ModelChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		), 
		queryset = Entorno.objects.all(),
		empty_label = "Selecione uma variável de entorno"
	)

	risco = forms.ChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		), 
		choices = (('B', 'Baixo'), ('M', 'Médio'), ('A', 'Alto'))
	)

	solucao_sugerida = forms.CharField(
		widget = forms.Textarea(
			attrs = {'class': 'form-control'}
		)
	)