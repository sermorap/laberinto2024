from LaberintoBuilder.Director import Director
from Ente.Personaje import Personaje
import os
import sys

# Para evitar errores de recursión
nombre = input("Nombre personaje: ")
personaje = Personaje()

opcion = input("Seleccione una opción:\n    1.Jugar\n    2.Salir\n")

while opcion not in ["1", "2"]:
    print("No ha seleccionado una opción correcta. Por favor, selecciona (1 o 2).")
    opcion = input("Opciones:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

if opcion == "2":
    sys.exit()

jsons = os.listdir('json/')
print("JSON disponibles:")
for idx, json_file in enumerate(jsons):
    print(f"    {idx}. {json_file}")

while opcion not in ["1", "2"]:
    print("No ha seleccionado una opción correcta. Por favor, selecciona (1 o 2).")
    opcion = input("Opciones:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

json_idx = input("Selecciona un json: ")
while not json_idx.isdigit() or int(json_idx) < 0 or int(json_idx) >= len(jsons):
    print("Selección incorrecta. Introduce un número válido correspondiente al JSON.")
    json_idx = input("Selecciona un json: ")

json_file = jsons[int(json_idx)] #json seleccionado por el usuario

director = Director()
director.procesar(os.path.join('json', json_file))
juego = director.getJuego()
forma = director.form
personaje.seudonimo = nombre
juego.agregarPersonaje(personaje)
juego.prota = personaje

while not juego.etapa.esFinal():
    if forma == "Cuadrado":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsillomagico\n    8. Mostrar comandos cuerpo\n",   
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar Bolsillo Mágico")
        
    elif forma == "Triangulo":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n",
              "   4. Abrir Puertas\n    5. Lanzar bichos\n    6. Mostrar comandos bolsillomagico\n    7. Mostrar comandos cuerpo\n",
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar Bolsillo Mágico")
    elif forma == "Rombo":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al noreste\n    2. Mover al noroeste\n    3. Mover al sureste\n    4. Mover al suroeste\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsillomagico\n    8. Mostrar comandos cuerpo\n",
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar Bolsillo Mágico")

    sys.stdin.flush()
    accion = input("Elige: ")

    if accion == "1":
        if forma == "Cuadrado":
            personaje.irAlNorte() #CUADRADO VAMOS NORTE
        elif forma == "Triangulo":
            personaje.irAlNorte() #TRIANGULO VAMOS NORTE
        elif forma == "Rombo":
            personaje.irAlNoreste() #ROMBO VAMOS NORESTE


    elif accion == "2":
        if forma == "Cuadrado":
            personaje.irAlEste() #CUADRADO VAMOS ESTE
        elif forma == "Triangulo":
            personaje.irAlEste() #TRIANGULO VAMOS ESTE
        elif forma == "Rombo":
            personaje.irAlNoroeste() #ROMBO VAMOS NOROESTE

    elif accion == "3":
        if forma == "Cuadrado":
            personaje.irAlOeste() #CUADRADO VAMOS OESTE
        elif forma == "Triangulo":
            personaje.irAlOeste() #TRIANGULO VAMOS OESTE
        elif forma == "Rombo":
            personaje.irAlSureste() #ROMBO VAMOS SURESTE

    elif accion == "4":
        if forma == "Cuadrado": 
            personaje.irAlSur() #CUADRADO VAMOS SUR
        elif forma == "Rombo":
            personaje.irAlSuroeste() #ROMBO VAMOS SUROESTE
        else:
            juego.openDoors() #TRIANGULO ABRIMOS PUERTA (NO QUEDAN ORIENTACIONES)

    elif accion == "5":
        if forma == "Triangulo":
            juego.fabricarBichoAgresivo(2) #TRIANGULO BICHO AGRESIVO
        else:
            juego.openDoors() #CUADRADO Y ROMBO ABRIMOS PUERTA

    elif accion == "6":
        if forma == "Triangulo":
            coms = personaje.bolsillomagico.obtenerComandos(personaje) # TRIANGULO MOSTRAMOS COMANDOS BOLSILLOMAGICO
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                el = input("Seleccione comando: ")
                while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                    print("Selección incorrecta. Introduce número que corresponda al comando que desees.")
                    el = input("Seleccione comando: ")
                coms[int(el)].ejecutar(personaje)
            else:
                print("No hay objetos.")
        else:
            juego.fabricarBichoAgresivo(2) #CUADRADO Y ROMBO BICHO AGRESIVO

    elif accion == "7":
        if forma == "Triangulo": 
            print("¿De verdad quieres usar el brazo ataque?")
            respuesta = input("1. Sí\n Otra tecla. No: ")
            if respuesta == "1":
                if personaje.cuerpo.brazoAtaque is not None:
                    coms = personaje.cuerpo.brazoAtaque.commmands # TRIANGULO MOSTRAMOS COMANDOS CUERPO
                    if len(coms) > 0:
                        print("Comandos disponibles:")
                        for idx, com in enumerate(coms):
                            print(f"    {idx}. {com}")
                        el = input("Seleccione comando: ")
                        while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                            print("Selección incorrecta. Introduce número que corresponda al comando que desees.")
                            el = input("Seleccione comando: ")
                        coms[int(el)].ejecutar(personaje)
                    else:
                        print("No hay comandos disponibles para el brazo de ataque.")
                else:
                    print("No hay nada en la mano.")
        else:
            coms = personaje.bolsillomagico.obtenerComandos(personaje) # CUADRADO Y ROMBO MOSTRAMOS COMANDOS BOLSILLOMAGICO
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                el = input("Seleccione comando: ")
                while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                    print("Selección incorrecta. Introduce número que corresponda al comando que desees.")
                    el = input("Seleccione comando: ")
                coms[int(el)].ejecutar(personaje)
            else:
                print("No hay objetos.")

    elif accion == "a" or accion == "A":
        personaje.atacar() #ATACAMOS

    elif accion == "h" or accion == "H":
        hijos = juego.getChildrenPosition() #OBTENEMOS OBJETOS POSICION PERSONAJE
        if len(hijos) > 0:
            print("Objetos disponibles:")
            for idx, hijo in enumerate(hijos):
                print(f"    {idx}. {hijo}")
            el = input("Seleccione objeto: ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(hijos):
                print("Selección incorrecta. Introduce número que corresponda al objeto que desees.")
                el = input("Seleccione objeto: ")
            hijos[int(el)].entrar(personaje)
        else:
            print("No hay objetos en la habitación.")

    elif accion == "c" or accion == "C":
        coms = personaje.obtenerComandos(personaje) #OBTENEMOS COMANDOS
        if len(coms) > 0:
            print("Comandos disponibles:")
            for idx, com in enumerate(coms):
                print(f"    {idx}. {com}")
            el = input("Seleccione comando: ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                print("Selección incorrecta. Introduce número que corresponda al comando que desees.")
                el = input("Seleccione comando: ")
            coms[int(el)].ejecutar(personaje)
        else:
            print("No hay comandos disponibles.")
    
    elif accion == "i" or accion == "I":
        print("Bolsillo magico de Doraemon:") #MOSTRAMOS BOLSILLO MAGICO
        if len(personaje.bolsillomagico.children) > 0:
            for idx, obj in enumerate(personaje.bolsillomagico.children):
                print(f"    {idx}. {obj}")
            el = input("Seleccione objeto: ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(personaje.bolsillomagico.children):
                print("Selección incorrecta. Introduce número que corresponda al objeto que desees.")
                el = input("Seleccione objeto: ")
            
            coms = personaje.bolsillomagico.children[int(el)].obtenerComandos(personaje)
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                ele = input("Seleccione comando: ")
                while not ele.isdigit() or int(ele) < 0 or int(ele) >= len(coms):
                    print("Selección incorrecta. Introduce número que corresponda al comando que desees.")
                    ele = input("Selecciona comando: ")
                coms[int(ele)].ejecutar(personaje)
            else:
                print("No hay comandos disponibles para este objeto.")
        else:
            print("No hay objetos en el bolsillomagico.")
