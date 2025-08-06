lista = 1 
def cargarcontenido(dato):
    lista.append(dato)

def imprimirlista():
    print(lista)

def quuitarDelista(dato):
    lista.remove(dato)

if __name__=="__main__":
    cargarcontenido("MOISES")
