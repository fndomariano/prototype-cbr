#coding: utf-8

from apptcc.models import Rio, Bacia_Hidrografica
from apptcc.forms.rio import FormRio
from django.shortcuts import render, redirect

def listar(request):
	rios = Rio.objects.all()

	return render(request, 'rio/index.html', {'dados': rios})

def add(request):

	if request.method == 'POST':
		form = FormRio(request.POST)

		if form.is_valid():
			rio = Rio()
			rio.nome = request.POST['nome']
			rio.dimensao = request.POST['dimensao']
			rio.bacia_hidrografica = Bacia_Hidrografica.objects.get(pk=request.POST['bacia_hidrografica'])
			rio.save()

			return redirect('/rio/')
	else:
		form = FormRio()

	return render(request, 'rio/add.html', {
		'form': form
	})


def edit(request, rio_id):

	rio = Rio.objects.get(pk=rio_id)

	if request.method == 'POST':
		form = FormRio(request.POST)

		if form.is_valid():
			rio.nome = request.POST['nome']
			rio.dimensao = request.POST['dimensao']
			rio.bacia_hidrografica = Bacia_Hidrografica.objects.get(pk=request.POST['bacia_hidrografica'])
			rio.save()

			return redirect('/rio/')

	else:
		data = {
			'nome': rio.nome,
			'dimensao': rio.dimensao,
			'bacia_hidrografica': rio.bacia_hidrografica
		}

		form = FormRio(initial=data)

	return render(request, 'rio/edit.html', {
		'form':form,
		'rio_id':rio.id
	})

def delete(request, rio_id):

	rio = Rio.objects.get(pk=rio_id)

	if rio.id != None:
		rio.delete()
		return redirect('/rio/')