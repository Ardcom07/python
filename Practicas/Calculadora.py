class Calculadora:
    #atributos 
    numero1 = None 
    numero2 = None 
    resultado = None
    #constructor 
    def __init__(self,n1=0,n2=0):
        self.numero1 = n1 
        self.numero2 = n2
        self.resultado = 0
    #metodos
    def sumar(self):
        self.resultado = self.numero1 + self.numero2
        return self.resultado

    def getResultado(self):
        pass
    
    def restar(self): 
        self.resultado = self.numero1 - self.numero2
        return self.resultado

    def multiplicar(self):
        self.resultado = self.numero1 * self.numero2
        return self.resultado

    def dividir(self):
        self.resultado = self.numero1 / self.numero2
        return self.resultado

class CalculdoraCientifica(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1,n2)

    def factorial(self,num):
        if(num <= 1):
            return 1 
        else:
            return num * self.factorial(num -1)
    #sobreescribir, overrride, polimorfismo
    def getResultado(self):
        return  f"Operacion anterior: {self.resultado}"

class CalculadoraProgramador(Calculadora):
        def __init__(self, x, y):
            super().__init__(x, y)

        def decimalToBinario(self, num):
            digitoString = ""
            while(num >= 2): 
                c = int(num / 2)
                r = num % 2
                num = c 
                digitoString = str(r) + digitoString
            digitoString = str(num) + digitoString
            return digitoString

if __name__== "__main__":
    casio = Calculadora()
    casio.numero1 = 10 
    casio.numero2 = 5 
    print(f"La suma de 10 + 5 es : {casio.sumar()}")
    print(f"La resta de 10 - 5 es : {casio.restar()}")
    print(f"La multiplicacion de 10 * es : {casio.multiplicar()}")
    print(f"La division de 10 / 5 es : {casio.dividir()}")

    hp = CalculdoraCientifica(20,8)
    print(f"La suma con CC de . . . es {hp.sumar()}")
    print(f"Factorial de 5: {hp.factorial(5)}")

    cp = CalculadoraProgramador(2,5)
    decimal = int(input("Ingrese un decimal a convertir: "))
    print(f"El binario de {decimal}es" + cp.decimalToBinario(decimal)) 