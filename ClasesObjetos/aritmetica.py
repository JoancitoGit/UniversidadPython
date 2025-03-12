class Aritmetica:

    def __init__(self, operando1 = None, operando2 = None):
        self.operando1 = operando1
        self.operando2 = operando2


    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

    def dividir(self):
        return self.operando1 / self.operando2

if __name__ == '__main__':
    aritmetica1 = Aritmetica(5,7)
    print(aritmetica1.sumar())

    aritmetica2 = Aritmetica(12,16)
    print(aritmetica2.sumar())
    #Tercer objeto
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    print(aritmetica3.sumar())

    # Cuarto Objeto
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 10
    aritmetica4.operando2 = 20
    print(aritmetica4.sumar())