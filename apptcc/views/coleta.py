#coding: utf-8

from apptcc.models import Coleta, Substancia, Ponto_Monitoramento, Monitoramento
from apptcc.forms.coleta import FormColeta
from django.shortcuts import render, redirect

def listar(request):

	p = Ponto_Monitoramento()
	
	coletas = Coleta.objects.all()

	return render(request, 'coleta/index.html', {
		'dados': coletas
	})


def add(request):

	if request.method == 'POST':

		form = FormColeta(request.POST)

		if form.is_valid():
			
			substancias       = request.POST.getlist('substancia')
			valores_coletados = request.POST.getlist('valor_coletado')

			monitoramento = Monitoramento()
			monitoramento.data_monitoramento  = request.POST['data_coleta']
			monitoramento.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
			monitoramento.save()

			for i in range(len(substancias)):
				coleta                     = Coleta()
				coleta.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
				coleta.substancia          = Substancia.objects.get(pk=substancias[i])
				coleta.valor_coletado      = float(valores_coletados[i])
				coleta.save()

			calculo = Monitoramento.objects.get(pk=monitoramento.id)
			calculo.classificacao_iva   = calculo.get_classificacao_iva()
			calculo.classificacao_iap   = calculo.get_classificacao_iap()
			calculo.save()
			
			return redirect('/coleta/')

	else:
		form = FormColeta()

	return render(request, 'coleta/add.html', {
		'form': form
	})


def edit(request, coleta_id):

	coleta = Coleta.objects.get(pk=coleta_id)

	if request.method == 'POST':
		form = FormColeta(request.POST)

		if form.is_valid():
			pass
	else:
		data = {
			'valor_coletado': coleta.valor_coletado,
			'substancia': coleta.substancia.all(),
			'ponto': coleta.ponto
		}

		form = FormColeta(initial=data)

	return render(request, 'coleta/edit.html', {
		'form': form,
		'coleta_id': coleta.id
	})


def delete(request, coleta_id):

	coleta = Coleta.objects.get(pk=coleta_id)

	if coleta.id != None:
		coleta.delete()
		return redirect('/coleta/')