from tkinter import *
import os 

def abrirCalculadora():
    os.system("Calc")

def abrirChrome():
    os.system("Chrome")

def abrirBlocdeNotas():
    os.system("Bloc de Notas")

Ventana = Tk()
Ventana.title("Menu principal")
Ventana.config(bg = "yellow")
Ventana.geometry("520x480")
Ventana.resizable(0,0)

botonCalc = Button(text="Calculadora", command=abrirCalculadora)
botonCalc.place(x=50, y=50)
Ventana.mainloop()

botonChrome = Button(text="Explorador de Archivos", command=abrirChrome)
botonChrome.place(x=70, y=70)
Ventana.mainloop()

botonBlocdeNotas = Button(text="Bloc de Notas", command=abrirBlocdeNotas)
botonBlocdeNotas.place(x=80, y=80)
Ventana.mainloop()