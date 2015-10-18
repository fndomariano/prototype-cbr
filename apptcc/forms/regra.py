#coding: utf-8

from apptcc.models import Entorno, Monitoramento
from django import forms

class FormRegra(forms.Form):

	monitoramento = forms.ModelChoiceField(
		widget = forms.Select(), 
		queryset = Monitoramento.objects.all(),
		empty_label = "Selecione uma data de monitoramento"
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

	solucao_sugerida = forms.CharField(
		widget = forms.Textarea()
	)