#coding: utf-8

from apptcc.forms.substancia import FormSubstancia
from apptcc.models import Substancia
from django.shortcuts import render, redirect


def listar(request):

	substancias = Substancia.objects.all()

	return render(request, 'substancia/index.html', {
		'dados': substancias
	})
