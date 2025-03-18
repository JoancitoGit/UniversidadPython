class Aritmetica:

    def __init__(self, operando1 = None, operando2 = None):
        self._operando1 = operando1
        self._operando2 = operando2


    def sumar(self):
       resultado = self._operando1 + self._operando2
       print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado división: {resultado}')

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2

if __name__ == '__main__':
    print('*** Ejemplo Clase Aritmética ***')
    aritmetica1 = Aritmetica(5,7)
    print('---Primer Objeto---')
    print(f'Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}')
    print(f'Valor operando2 del objeto aritmetica1: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    aritmetica1.operando1 = 9
    aritmetica1.operando2 = 15
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()