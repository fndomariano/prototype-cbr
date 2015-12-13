#coding: utf-8

from apptcc.models import Casos, Monitoramento, Entorno
from apptcc.forms.caso import FormCaso
from apptcc.forms.pesquisa import FormPesquisa
from django.shortcuts import render, redirect

def listar(request):
	casos = Casos.objects.order_by('classificacao_iap', 'classificacao_iva', 'entorno', 'risco').all()
	return render(request, 'caso/index.html', {'dados':casos})


def add(request):
	if request.method == 'POST':
		form = FormCaso(request.POST)
		if form.is_valid():
			caso = Casos()
			caso.classificacao_iap = request.POST['iap']
			caso.classificacao_iva = request.POST['iva']
			caso.entorno           = Entorno.objects.get(pk=request.POST['entorno'])
			caso.risco             = request.POST['risco']
			caso.solucao_sugerida  = request.POST['solucao_sugerida']
			caso.save()
			return redirect('/caso/')
	else:
		form = FormCaso()
	return render(request, 'caso/add.html', {'form': form})


def edit(request, caso_id):
	caso = Casos.objects.get(pk=caso_id)
	if request.method == 'POST':
		form = FormCaso(request.POST)
		if form.is_valid():
			caso.classificacao_iap = request.POST['iap']
			caso.classificacao_iva = request.POST['iva']
			caso.entorno           = Entorno.objects.get(pk=request.POST['entorno'])
			caso.risco             = request.POST['risco']
			caso.solucao_sugerida  = request.POST['solucao_sugerida']
			caso.save()
			return redirect('/caso/')
	else:
		data = {
			'iap': caso.classificacao_iap,
			'iva': caso.classificacao_iva,
			'risco': caso.risco,
			'entorno': caso.entorno,
			'solucao_sugerida': caso.solucao_sugerida
		}
		form = FormCaso(initial=data)

	return render(request, 'caso/edit.html', {
		'form': form,
		'caso_id': caso.id
	})

def delete(request, caso_id):
	caso = Casos.objects.get(pk=caso_id)
	if caso.id != None:
		caso.delete()
		return redirect('/caso/')


def pesquisar(request):

	resultado = {}
	montioramento = ''

	form = FormPesquisa()

	if request.method == 'GET':
		monitoramento = request.GET.get('monitoramento')
		entorno = request.GET.get('entorno')

		if monitoramento is not None and entorno is not None:
			
			sql = '''SELECT r.id, r.solucao_sugerida, r.risco FROM apptcc_casos r
				INNER JOIN apptcc_entorno e ON e.id = r.entorno_id WHERE e.id = %d 
				AND r.classificacao_iap = (SELECT classificacao_iap FROM apptcc_monitoramento WHERE id = %d)
	 			AND r.classificacao_iva = (SELECT classificacao_iva FROM apptcc_monitoramento WHERE id = %d)
	 			''' %(int(entorno), int(monitoramento), int(monitoramento))

			resultado['solucao'] = list(Casos.objects.raw(sql))
			resultado['monitoramento'] = monitoramento

			return render(request, 'caso/resultado.html', {'resultado': resultado})
	
	return render(request, 'caso/pesquisar.html', {'form': form})


def utilizar_solucao(request, caso_id, monitoramento_id):

	caso          = Casos.objects.get(pk=caso_id)
	monitoramento = Monitoramento.objects.get(pk=monitoramento_id)
	monitoramento.solucao_sugerida = caso.solucao_sugerida
	monitoramento.risco            = caso.risco
	monitoramento.save()

	return redirect('/caso/pesquisar/')


