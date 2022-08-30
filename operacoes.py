import math


class operacoes:
    def __init__(self):
        pass

    def somar(self, num1, num2):
        return float(num1) + float(num2)

    def subtrair(self, num1, num2):
        return float(num1) - float(num2)

    def multiplicar(self, num1, num2):
        return float(num1) * float(num2)

    def dividir(self, num1, num2):
        if num2 == 0:
            return  "Impossível dividir por zero!"
        else:
            return float(num1) / float(num2)

    def potencia(self, base, expoente):
        if float(expoente) == 0:
            return 1
        elif float(expoente) == 1:
            return float(base)
        else:
            return math.pow(base, expoente)

    def rais(self, num):
        if float(num) < 0:
            return "Impossível calcular"
        else:
            return math.sqrt(float(num))

    def tabuada(self, num):
        for i in range(11):
            resultado = resultado + "\n{} * {} = {}".format(num, i, int(num*i))
        return resultado