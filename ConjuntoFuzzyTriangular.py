# coding: utf-8


def get_valores_conjunto(numero_conjunto):
	if(numero_conjunto is str(1)):
		return {
			"a": 0,
			"m": 1,
			"b": 1.5
		}

	if(numero_conjunto == str(2)):
		return {
			"a": 1,
			"m": 1.5,
			"b": 2
		}

	if(numero_conjunto is str(3)):
		return {
			"a": 1.5,
			"m": 2,
			"b": 2
		}


def calcula_pertinencia(conjunto, altura):
	altura = float(altura)

	if(altura <= conjunto['a']):
		return 0

	if(conjunto['a'] < altura and altura <= conjunto['m']):
		return (altura - conjunto['a']) / (conjunto['m'] - conjunto['a'])

	if(conjunto['m'] < altura and altura <= conjunto['b']):
		return (conjunto['b'] - altura) / (conjunto['b'] - conjunto['m'])

	if(altura > conjunto['b']):
		return 0


def calcula_pertinencia_para_um_intervalo(grupo, step):
	print('--------------------------------------------------')
	x = 0
	while (x <= 2):
		pertinencia = calcula_pertinencia(grupo, x)
		print("Valor " + str(x) + " tem pertinência igual a: " + str(pertinencia))
		x = x + float(step)
	print('--------------------------------------------------\n')


def calcula_suporte(conjunto):
	return "]" + str(conjunto['a']) + ", " + str(conjunto['b']) + "["


def calcula_nucleo(conjunto):
	return str(conjunto['m'])


def calcula_altura(conjunto):
	return ''


def calcula_alfa_corte():
	return ''
