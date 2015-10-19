#coding: utf-8


from django.db import models
import math

class Bacia_Hidrografica(models.Model):

	nome = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nome


class Rio(models.Model):

	nome               = models.CharField(max_length=150)
	dimensao           = models.FloatField()
	bacia_hidrografica = models.ForeignKey(Bacia_Hidrografica)

	def __unicode__(self):
		return self.nome

class Ponto_Monitoramento(models.Model):

	latitude  = models.FloatField()
	longitude = models.FloatField()
	rio       = models.ForeignKey(Rio)

	def __unicode__(self):
		return str(self.id) + ' - (' + str(self.latitude) + ', ' + str(self.longitude) + ')'


class Substancia(models.Model):

	nome  = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome


class Coleta(models.Model):
	id                  = models.AutoField(verbose_name='id', serialize=False, auto_created=True, primary_key=True)
	ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
	substancia          = models.ForeignKey(Substancia)
	valor_coletado      = models.FloatField()
	
	def __unicode__(self):
		return unicode(self.data_coleta)


class Entorno(models.Model):

	variavel_entorno = models.CharField(max_length=45)

	def __unicode__(self):
		return self.variavel_entorno


class Monitoramento(models.Model):

	data_monitoramento  = models.DateField('Data do Monitoramento')
	ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
	classificacao_iap   = models.CharField(max_length=45)
	classificacao_iva   = models.CharField(max_length=45)

	def _get_valor_coletado_substancia(self, nome_substancia):
		sql = ''' SELECT m.id, s.nome, c.valor_coletado FROM apptcc_monitoramento m
			INNER JOIN apptcc_ponto_monitoramento p ON p.id = m.ponto_monitoramento_id
			INNER JOIN apptcc_coleta c ON p.id = c.ponto_monitoramento_id
			INNER JOIN apptcc_substancia s ON s.id = c.substancia_id
			WHERE s.nome = '%s' AND m.data_monitoramento = '%s' 
			AND c.ponto_monitoramento_id = %d ''' %(nome_substancia, self.data_monitoramento, int(self.ponto_monitoramento.id))

		substancia = Monitoramento.objects.raw(sql)
		substancia = list(substancia)
		valor_coletado_da_substancia = substancia[0].valor_coletado
		return valor_coletado_da_substancia

	def _get_valores_iqa(self):
		return {
			'oxigenio_dissolvido': self._get_od(self._get_valor_coletado_substancia('Oxigênio Dissolvido')),
			'coliformes_termotolerantes': self._get_cf(self._get_valor_coletado_substancia('Coliformes Termotolerantes')),
			'ph': self._get_ph(self._get_valor_coletado_substancia('Potencial Hidrogênico - pH')),
			'dbo_520': self._get_dbo(self._get_valor_coletado_substancia('DBO 5.20')),
			'temperatura': self._get_temperatura(self._get_valor_coletado_substancia('Temperatura da Água')),
			'nitrogenio_total': self._get_nitrogenio_total(self._get_valor_coletado_substancia('Nitrogênio Total')),
			'fosforo_total': self._get_fosforo_total(self._get_valor_coletado_substancia('Fósforo Total')),
			'residuo_total': self._get_residuo_total(self._get_valor_coletado_substancia('Resíduo Total'))
		}

	def _get_valores_st_ipmca(self):
		return {
			'cadmio': self._get_valor_coletado_substancia('Cádmio'),
			'cromo': self._get_valor_coletado_substancia('Cromo Total'),
			'cobre_dissolvido': self._get_valor_coletado_substancia('Cobre Dissolvido'),
			'chumbo': self._get_valor_coletado_substancia('Chumbo'),
			'mercurio': self._get_valor_coletado_substancia('Mercúrio'),
			'niquel': self._get_valor_coletado_substancia('Niquel'),
			'fenois_totais': self._get_valor_coletado_substancia('Fenóis Totais'),
			'surfactantes': self._get_valor_coletado_substancia('Surfactantes'),
			'zinco': self._get_valor_coletado_substancia('Zinco')
		}

	def _get_valores_ipmca_ve(self):
		return {
			'od': self._get_valor_coletado_substancia('Oxigênio Dissolvido'),
			'ph': self._get_valor_coletado_substancia('Potencial Hidrogênico - pH')
		}

	def _get_ponderacao_ipmca_od(self):
		substancia = self._get_valores_ipmca_ve()
		
		if substancia['od'] >= 5:
			print 1
		elif substancia['od'] >= 3 and substancia['od'] < 5:
			print 2
		else:
			print 3

	def _get_ponderacao_ipmca_cadmio(self):
		pass

	def _get_ponderacao_ipmca_cromo(self):
		pass

	def __get_ponderacao_ipmca_cobre_dissolvido(self):
		pass

	def _get_ponderacao_ipmca_chumbo_total(self):
		pass

	def _get_ponderacao_ipmca_mercurio(self):
		pass

	def _get_ponderacao_ipmca_niquel(self):
		pass

	def _get_ponderacao_ipmca_niquel(self):
		pass

	def _get_ponderacao_ipmca_fenois_totais(self):
		pass

	def _get_ponderacao_ipmca_surfactantes(self):
		pass

	def _get_ponderacao_ipmca_zinco(self):
		pass

	def _get_ponderecao_ipmca_ph(self):
		substancia = self._get_valores_ipmca_ve()

		if substancia['ph'] >= 6 and substancia['ph'] <= 9:
			print 1
		elif substancia['ph'] > 5 and substancia['ph'] < 6:
			print 2
		elif substancia['ph'] > 9 and substancia['ph'] <= 9.5:
			print 2
		else:
			print 3

	def _get_substancia_com_maior_ponderacao(self):
		substancia = self._get_valores_ipmca_ve()
		
		if self._get_ponderecao_ph() > self._get_ponderacao_ipmca_od():
			return substancia['ph']
		else:
			return substancia['od']

	def _get_valores_st_isto(self):
		return {
			'pfhtm': self._get_valor_coletado_substancia('PFHTM'),
			'numero_celulas': self._get_valor_coletado_substancia('Número de Células Cianobactérias'),
			'cadmio': self._get_valor_coletado_substancia('Cádmio'),
			'chumbo': self._get_valor_coletado_substancia('Chumbo'),
			'cromo': self._get_valor_coletado_substancia('Cromo Total'),
			'mercurio': self._get_valor_coletado_substancia('Mercúrio'),
			'niquel': self._get_valor_coletado_substancia('Niquel')
		}

	def _get_valores_so_isto(self):
		return {
			'ferro_dissolvido': self._get_valor_coletado_substancia('Ferro Dissolvido'),
			'manganes': self._get_valor_coletado_substancia('Manganês'),
			'aluminio_dissolvido': self._get_valor_coletado_substancia('Alumínio Dissolvido'),
			'cobre_dissolvido': self._get_valor_coletado_substancia('Cobre Dissolvido'),
			'zinco': self._get_valor_coletado_substancia('Zinco')
		}

	def _get_valores_iet(self):
		return {
			'fosforo': self._get_valor_coletado_substancia('Fósforo Total'),
			'clorofila': self._get_valor_coletado_substancia('Clorofila'),
		}

	def _get_multipliacao_minimos_st(self):
		st = self._get_valores_st_isto()
		minimo1 = min(st.values())
		minimo2 = st.values()
		minimo2.remove(minimo1)
		return minimo1 * minimo2

	def _get_avg_so(self):
		so = self._get_valores_so_isto()
		so = so.values()
		return float(sum(so)) / len(so)
	
	def _get_od(self, oxigenio_dissolvido):
		if oxigenio_dissolvido > 140:
			return 47.0;
		else:
			return oxigenio_dissolvido

	def _get_cf(self, cf):
		if ct > 100000:
			return 3.0;
		else:
			return cf

	def _get_ph(self, ph):
		if ph <= 2:
			return 2.0
		elif ph >= 12:
			return 3.0
		else:
			return ph

	def _get_dbo(self, dbo):
		if dbo > 30:
			return 2.0
		else:
			return dbo

	def _get_temperatura(self, temperatura):
		if temperatura > 15:
			return 9.0
		else:
			return temperatura

	def _get_nitrogenio_total(self, nt):
		if nt > 90:
			return 1.0
		else:
			return nt

	def _get_fosforo_total(self, ft):
		if ft > 10:
			return 5.0
		else:
			return ft

	def _get_turbidez(self, turbidez):
		if turbidez > 100:
			return 5.0
		else:
			return turbidez

	def _get_residuo_total(self, rt):
		if rt > 500:
			return 30.0
		else:
			return rt


	def _calcula_iqa(self):
		valores_iqa = self._get_valores_iqa()
		calculo = math.pow(valores_iqa['oxigenio_dissolvido'], 0.17)
		calculo *= math.pow(valores_iqa['coliformes_termotolerantes'], 0.15)
		calculo *= math.pow(valores_iqa['ph'], 0.12)
		calculo *= math.pow(valores_iqa['dbo_520'], 0.10)
		calculo *= math.pow(valores_iqa['temperatura'], 0.10)
		calculo *= math.pow(valores_iqa['nitrogenio_total'], 0.10)
		calculo *= math.pow(valores_iqa['fosforo_total'], 0.10)
		calculo *= math.pow(valores_iqa['turbidez'], 0.08)
		calculo *= math.pow(valores_iqa['residuo_total'], 0.08)
		return calculo

	def _calcula_isto(self):
		return self._get_multipliacao_minimos_st() * self._get_so_isto()

	def _calcula_ipmca(self):
		ve = self._get_substancia_com_maior_ponderacao()
		st = self._get_media_tres_maiores_ponderacoes()
		return ve * st

	def _calcula_iet(self):
		valores_iet = self._get_valores_iet()
		iet_cl = 10 * (6 - ((-0.7 - 0.6 * math.log(valores_iet['clorofila'])) / math.log(2))) - 20
		iet_ptt = 10 * (6 - ((-0.42 - 0.36 * math.log(valores_iet['fosforo'])) / math.log(2))) - 20
		return iet_pt + iet_cl

	def _calcula_iva(self):
		return (1.2 * self._calcula_ipmca()) + self._calcula_iet()

	def get_classificacao_iap(self):
		valor_iap = self._calcula_iqa() * self._calcula_isto()
			
		if valor_iap <= 19: 
			return "pessima"
		elif valor_iap >= 20 or valor_iap <= 36:
			return "ruim" 
		elif valor_iap >= 37 or valor_iap <= 51:
			return "regular"
		elif valor_iap >= 52 or valor_iap <= 79:
			return "boa"
		else:
			return "otima"

	def get_classificacao_iva(self):
		valor_iva = self._calcula_iva()
		
		if valor_iva <= 2.5: 
			return "otima"
		elif valor_iva > 2.6 or valor_iva <= 3.3:
			return "boa" 
		elif valor_iva > 3.4 or valor_iva <= 4.5:
			return "regular"
		elif valor_iva > 4.6 or valor_iva <= 6.7:
			return "ruim"
		else:
			return "pessima"

	def __unicode__(self):
		return unicode(self.data_monitoramento) + ' | ('+str(self.ponto_monitoramento.latitude) + ', ' +str(self.ponto_monitoramento.longitude) + ') | ' + 'IAP: ' + self.classificacao_iap + ' - ' + 'IVA:' + self.classificacao_iva


class Regras(models.Model):
	risco             = models.CharField(max_length=1)
	solucao_sugerida  = models.TextField()
	entorno           = models.ForeignKey(Entorno)
	monitoramento     = models.ForeignKey(Monitoramento)
	
	def __unicode__(self):
		return self.solucao_sugerida