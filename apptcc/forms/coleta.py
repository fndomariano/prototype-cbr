#coding: utf-8

from apptcc.models import Ponto_Monitoramento, Substancia
from django import forms


class FormColeta(forms.Form):

	data_coleta = forms.DateField(
		widget = forms.DateInput(
			attrs={'type':'date'}		
		)
	)

	ponto = forms.ModelChoiceField(
		widget = forms.Select(), 
		queryset = Ponto_Monitoramento.objects.all(),
		empty_label = "Selecione o ponto"
	)

	substancia = forms.ModelChoiceField(
		widget = forms.Select(),
		queryset = Substancia.objects.all(),
		empty_label = "Selecione a substancia"
	)

	valor_coletado = forms.FloatField(
		widget = forms.TextInput(
			attrs = {'placeholder': 'Digite o valor coletado'}
		)
	)