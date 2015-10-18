#coding: utf-8

from apptcc.models import Ponto_Monitoramento, Rio
from apptcc.forms.ponto import FormPonto
from django.shortcuts import render, redirect

def listar(request):
	
	pontos = Ponto_Monitoramento.objects.all()
	return render(request, 'ponto/index.html', {
		'dados':pontos
	})

def add(request):

	if request.method == 'POST':
		form = FormPonto(request.POST)
		if form.is_valid():
			ponto = Ponto_Monitoramento()
			ponto.latitude = request.POST['latitude']
			ponto.longitude = request.POST['longitude']
			ponto.rio = Rio.objects.get(pk=request.POST['rio'])
			ponto.save()

			return redirect('/ponto/')
	else:
		form = FormPonto()

	return render(request, 'ponto/add.html', {
		'form':form
	})


def edit(request, ponto_id):

	ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)

	if request.method == 'POST':
		form = FormPonto(request.POST)

		if form.is_valid():
			ponto.latitude = request.POST['latitude']
			ponto.longitude = request.POST['longitude']
			ponto.rio = Rio.objects.get(pk=request.POST['rio'])
			ponto.save()

			return redirect('/ponto/')
	else:
		data = {
			'latitude': ponto.latitude,
			'longitude': ponto.longitude,
			'rio': ponto.rio
		}
		form = FormPonto(initial=data)

	return render(request, 'ponto/edit.html', {
		'form': form,
		'ponto_id': ponto.id
	})


def delete(request, ponto_id):

	ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)

	if ponto.id != None:
		ponto.delete()
		return redirect('/ponto/')