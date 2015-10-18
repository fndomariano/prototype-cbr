#coding: utf-8

from apptcc.forms.substancia import FormSubstancia
from apptcc.models import Substancia
from django.shortcuts import render, redirect


def listar(request):

	substancias = Substancia.objects.all()

	return render(request, 'substancia/index.html', {
		'dados': substancias
	})


def add(request):

	if request.method == 'POST':

		form = FormSubstancia(request.POST)

		if form.is_valid():
			substancia = Substancia()
			substancia.nome = request.POST['nome']
			substancia.save()

			return redirect('/substancia/')

	else:

		form = FormSubstancia()

	return render(request, 'substancia/add.html', {
		'form': form
	})


def edit(request, substancia_id):

	substancia = Substancia.objects.get(pk=substancia_id)

	if request.method == 'POST':

		form = FormSubstancia(request.POST)

		if form.is_valid():
			substancia.nome = request.POST['nome']
			substancia.save()

			return redirect('/substancia/')
	else:

		form = FormSubstancia(initial={'nome':substancia.nome})

	return render(request, 'substancia/edit.html', {
		'form': form,
		'substancia_id': substancia.id
	})


def delete(request, substancia_id):

	substancia = Substancia.objects.get(pk=substancia_id)
	if substancia.id != None:
		substancia.delete()
		return redirect('/substancia/')