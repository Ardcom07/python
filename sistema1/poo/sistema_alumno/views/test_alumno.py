import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), " . .")))

from controllers.alumno_controller import AlumnoController
from models.alumno import Alumno

class TestAlumno: 
    def __init__(self):
        self.ac = AlumnoController()

    def main(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("-------MENU-------")
            print("1 Cargar alumno")
            print("2. Ver alumno")
            print("3. Actualizar alumno")
            print("4. Borrar alumno")
            print("5. Ver todo")
            print("0 Salir")
            resp = input("opcion: ")
            if resp =="1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                matricula = input("Matricula: ")
                self.ac.save(Alumno(nombre, email, matricula))
            elif resp == "5":
                print(self.ac.getA11())
                input("Presiona Enter para continuar...")
            elif resp == "0":
                print("BYE")
                break

if __name__== "__main__":
    vista = TestAlumno()
    vista.main()