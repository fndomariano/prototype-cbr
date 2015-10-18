#coding: utf-8

from apptcc.models import Bacia_Hidrografica
from apptcc.forms.bacia_hidrografica import FormBaciaHidrografica
from django.shortcuts import render, redirect

def listar(request):
	bh = Bacia_Hidrografica.objects.all()
	
	return render(request, 'bacia-hidrografica/index.html', {
		'dados': bh
	})

def add(request):

	if request.method == 'POST':
		form = FormBaciaHidrografica(request.POST)
		if form.is_valid():
			bh = Bacia_Hidrografica()
			bh.nome = request.POST['nome']
			bh.save()

			return redirect('/bacia-hidrografica/')
	else:
		form = FormBaciaHidrografica()

	return render(request, 'bacia-hidrografica/add.html', {
		'form': form
	})

def edit(request, bh_id):

	bh = Bacia_Hidrografica.objects.get(pk=bh_id)

	if request.method == 'POST':
		form = FormBaciaHidrografica(request.POST)

		if form.is_valid():
			bh.nome = request.POST['nome']
			bh.save()

			return redirect('/bacia-hidrografica/')
	else:

		form = FormBaciaHidrografica(initial={'nome':bh.nome})

	return render(request, 'bacia-hidrografica/edit.html',{
		'form':form,
		'bh_id': bh.id
	})

def delete(request, bh_id):

	bh = Bacia_Hidrografica.objects.get(pk=bh_id)

	if bh.id != None:
		bh.delete()
		return redirect('/bacia-hidrografica/')