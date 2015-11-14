#coding: utf-8

from apptcc.models import Regras, Monitoramento, Entorno
from apptcc.forms.regra import FormRegra
from apptcc.forms.pesquisa import FormPesquisa
from django.shortcuts import render, redirect

def listar(request):
	regras = Regras.objects.all()
	return render(request, 'regra/index.html', {'dados':regras})


def add(request):
	if request.method == 'POST':
		form = FormRegra(request.POST)
		if form.is_valid():
			regra = Regras()
			regra.classificacao_iap = request.POST['iap']
			regra.classificacao_iva = request.POST['iva']
			regra.entorno           = Entorno.objects.get(pk=request.POST['entorno'])
			regra.risco             = request.POST['risco']
			regra.solucao_sugerida  = request.POST['solucao_sugerida']
			regra.save()
			return redirect('/regra/')
	else:
		form = FormRegra()
	return render(request, 'regra/add.html', {'form': form})


def edit(request, regra_id):
	regra = Regras.objects.get(pk=regra_id)
	if request.method == 'POST':
		form = FormRegra(request.POST)
		if form.is_valid():
			regra.classificacao_iap = request.POST['iap']
			regra.classificacao_iva = request.POST['iva']
			regra.entorno           = Entorno.objects.get(pk=request.POST['entorno'])
			regra.risco             = request.POST['risco']
			regra.solucao_sugerida  = request.POST['solucao_sugerida']
			regra.save()
			return redirect('/regra/')
	else:
		data = {
			'iap': regra.classificacao_iap,
			'iva': regra.classificacao_iva,
			'risco': regra.risco,
			'entorno': regra.entorno,
			'solucao_sugerida': regra.solucao_sugerida
		}
		form = FormRegra(initial=data)

	return render(request, 'regra/edit.html', {
		'form': form,
		'regra_id': regra.id
	})

def delete(request, regra_id):
	regra = Regras.objects.get(pk=regra_id)
	if regra.id != None:
		regra.delete()
		return redirect('/regra/')


def pesquisar(request):

	resultado = []
	montioramento = ''

	if request.method == 'GET':
		monitoramento = request.GET.get('monitoramento')
		entorno = request.GET.get('entorno')

		form = FormPesquisa()

		if monitoramento is not None and entorno is not None:
			
			sql = '''SELECT r.id, r.solucao_sugerida, r.risco FROM apptcc_regras r
				INNER JOIN apptcc_entorno e on e.id = r.entorno_id WHERE e.id = %d 
				AND r.classificacao_iap = (SELECT classificacao_iap FROM apptcc_monitoramento WHERE id = %d)
	 			AND r.classificacao_iva = (SELECT classificacao_iva FROM apptcc_monitoramento WHERE id = %d)
	 			''' %(int(entorno), int(monitoramento), int(monitoramento))

			resultado = list(Regras.objects.raw(sql))
			resultado.append(monitoramento)
		
	return render(request, 'regra/pesquisar.html', {
		'form': form,
		'resultado': resultado
	})


def utilizar_solucao(request, regra_id, monitoramento_id):

	regra         = Regras.objects.get(pk=regra_id)
	monitoramento = Monitoramento.objects.get(pk=monitoramento_id)

	monitoramento.solucao_sugerida = regra.solucao_sugerida
	monitoramento.save()

	return redirect('/regra/pesquisar/')


