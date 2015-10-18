#coding: utf-8

from apptcc.forms.entorno import FormEntorno
from apptcc.models import Entorno
from django.shortcuts import render, redirect

def listar(request):
	entornos = Entorno.objects.all()
	return render(request, 'entorno/index.html', {
		'dados':entornos
	})

def add(request):
	if request.method == 'POST':
		form = FormEntorno(request.POST)
		if form.is_valid():
			entorno = Entorno()
			entorno.variavel_entorno = request.POST['variavel_entorno']
			entorno.save()
			return redirect('/entorno/')
	else:
		form = FormEntorno()
	return render(request, 'entorno/add.html', {
		'form':form
	})


def edit(request, entorno_id):
	entorno = Entorno.objects.get(pk=entorno_id)
	if request.method == 'POST':
		form = FormEntorno(request.POST)
		if form.is_valid():
			entorno.variavel_entorno = request.POST['variavel_entorno']
			entorno.save()
			return redirect('/entorno/')
	else:
		form = FormEntorno(initial={'variavel_entorno':entorno.variavel_entorno})
	return render(request, 'entorno/edit.html', {
		'form':form,
		'entorno_id':entorno.id
	})

def delete(request, entorno_id):
	entorno = Entorno.objects.get(pk=entorno_id)
	if entorno.id != None:
		entorno.delete()
		return redirect('/entorno/')
