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
			regra.monitoramento = Monitoramento.objects.get(pk=request.POST['monitoramento'])
			regra.entorno = Entorno.objects.get(pk=request.POST['entorno'])
			regra.risco = request.POST['risco']
			regra.solucao_sugerida = request.POST['solucao_sugerida']
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
			regra.monitoramento = Monitoramento.objects.get(pk=request.POST['monitoramento'])
			regra.entorno = Entorno.objects.get(pk=request.POST['entorno'])
			regra.risco = request.POST['risco']
			regra.solucao_sugerida = request.POST['solucao_sugerida']
			regra.save()
			return redirect('/regra/')
	else:
		data = {
			'monitoramento': regra.monitoramento,
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

	iap     = request.GET.get('iap')
	iva     = request.GET.get('iva')
	risco   = request.GET.get('risco')
	entorno = request.GET.get('entorno')

	form = FormPesquisa()

	resultado = []

	if iap is not None and iva is not None and entorno is not None and risco is not None:
		resultado = Regras.objects.raw(
			''' SELECT r.id, r.solucao_sugerida FROM apptcc_regras r
				INNER JOIN apptcc_monitoramento m ON m.id = r.monitoramento_id
				INNER JOIN apptcc_entorno e ON e.id = r.entorno_id
				WHERE m.classificacao_iap = '%s' AND m.classificacao_iva = '%s'
				AND r.risco = '%s' AND e.id = %d ''' %(iap, iva, risco, int(entorno))
		)

	return render(request, 'regra/pesquisar.html', {
		'form': form,
		'resultado': list(resultado)
	})




