#coding: utf-8

from apptcc.models import Entorno, Monitoramento
from django import forms

class FormPesquisa(forms.Form):

	monitoramento = forms.ModelChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		), 
		queryset = Monitoramento.objects.all(),
		empty_label = "Selecione uma data de monitoramento"
	)

	entorno = forms.ModelChoiceField(
		widget = forms.Select(
			attrs = {'class': 'form-control'}
		), 
		queryset = Entorno.objects.all(),
		empty_label = "Selecione uma variável de entorno"
	)