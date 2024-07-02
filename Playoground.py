from LaberintoBuilder.Director import Director
from Ente.Personaje import Personaje
# También deberíamos de importar la interfaz del GUI, pero que la he realizado traia consigo muchos errores y he decidio no ponerla
import os
import sys

nombre = input("Nombre del personaje: ")
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

json_idx = input("Selecciona un json: ")
while not json_idx.isdigit() or int(json_idx) < 0 or int(json_idx) >= len(jsons):
    print("Inválido. Por favor, selecciona un número entre 0 y", len(jsons) - 1)
    json_idx = input("Selecciona un json: ")

json_file = jsons[int(json_idx)] #json que seleccione

director = Director()
director.procesar(os.path.join('json', json_file))
juego = director.getJuego()
forma = director.form
personaje.apodo = nombre
juego.agregarPersonaje(personaje)
juego.prota = personaje

while not juego.fase.esFinal():
    if forma == "Cuadrado":
            print("¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
                  "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsillo\n    8. Mostrar comandos cuerpo\n",   
                  "   H. Obtener hijos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
            
            sys.stdin.flush()
            eleccion = input("Ingresa tu elección: ")

            if eleccion == "1":
                personaje.irAlNorte()
            if eleccion == "2":
                personaje.irAlEste()
            if eleccion == "3":
                personaje.irAlOeste()
            if eleccion == "4":
                personaje.irAlSur()
            if eleccion == "5":
                juego.openDoors()
            if eleccion == "6":
                juego.fabricarBichoAgresivo(2)
            if eleccion == "7":
                i = 0
                coms=personaje.mochila.obtenerComandos(personaje)
                if len(coms) > 0:
                    for com in coms:
                        print("    ",i,". ",com,"\n")
                        i += 1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    coms[el].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")
            if eleccion == "8":
                print("    1. ¿De verdad quieres usar el brazo ataque?")
                sys.stdin.flush()
                el = input()
                el = int(el)
                if el == 1:
                    i = 0
                    if personaje.cuerpo.brazoAtaque is not None:
                        for com in (coms:=personaje.cuerpo.brazoAtaque.commmands):
                            print("    ",i,". ",com,"\n")
                            i += 1
                        ele = input()
                        ele = int(ele)
                        coms[ele].ejecutar(personaje)
                    else:
                        print("No hay nada en la mano derecha.")

            if eleccion == "a" or eleccion == "A":
                personaje.atacar()
            
            if eleccion == "h" or eleccion == "H":
                hijos = juego.getChildrenPosition()
                if len(hijos) > 0:
                    print("Selecciona hijo: ")
                    i = 0
                    for hijo in hijos:
                        print("    ",i,". ",hijo)
                        i+=1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    if el < len(hijos) and el >= 0:
                        hijos[el].entrar(personaje)
                    else:
                        print("Has introducido un índice incorrecto.")
            else:
                print("No hay hijos disponibles.")
            
            if eleccion == "c" or eleccion == "C":
                coms = personaje.obtenerComandos(personaje)
                if len(coms) > 0:
                    print("Selecciona comando: ")
                    i = 0
                    for com in coms:
                        print("    ",i,". ",com)
                        i+=1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    if el < len(coms) and el >= 0:
                        coms[el].ejecutar(personaje)
                else:
                    print("Has introducido un índice incorrecto.")
            else:
                print("No hay comandos disponibles.")

            if eleccion == "i" or eleccion == "I":
                print("Inventario:")
                if len(personaje.mochila.children) > 0:
                    for idx, obj in enumerate(personaje.mochila.children):
                        print(f"    {idx}. {obj}")
                    el = input("Selecciona un objeto (número): ")
                    while not el.isdigit() or int(el) < 0 or int(el) >= len(personaje.mochila.children):
                        print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                        el = input("Selecciona un objeto (número): ")
                    
                    coms = personaje.mochila.children[int(el)].obtenerComandos(personaje)
                    if len(coms) > 0:
                        print("Comandos disponibles:")
                        for idx, com in enumerate(coms):
                            print(f"    {idx}. {com}")
                        ele = input("Selecciona un comando (número): ")
                        while not ele.isdigit() or int(ele) < 0 or int(ele) >= len(coms):
                            print("Selección inválida. Introduce un número válido correspondiente al comando.")
                            ele = input("Selecciona un comando (número): ")
                        coms[int(ele)].ejecutar(personaje)
                    else:
                        print("No hay comandos disponibles para este objeto.")
            else:
                print("No hay objetos en la mochila.")

    if forma == "Rombo":
            print("¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al noreste\n    2. Mover al noroeste\n    3. Mover al sureste\n    4. Mover al suroeste\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",
              "   H. Obtener hijos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
            
            sys.stdin.flush()
            eleccion = input("Ingresa tu elección: ")
            
            if eleccion == "1":
                personaje.irAlNoreste()
            if eleccion == "2":
                personaje.irAlNoroeste()
            if eleccion == "3":
                personaje.irAlSureste()
            if eleccion == "4":
                personaje.irAlSuroeste()
            if eleccion == "5":
                juego.openDoors()
            if eleccion == "6":
                juego.fabricarBichoAgresivo(2)
            if eleccion == "7":
                i = 0
                coms=personaje.mochila.obtenerComandos(personaje)
                if len(coms) > 0:
                    for com in coms:
                        print("    ",i,". ",com,"\n")
                        i += 1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    coms[el].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")
            if eleccion == "8":
                print("    1. ¿De verdad quieres usar el brazo ataque?")
                sys.stdin.flush()
                el = input()
                el = int(el)
                if el == 1:
                    i = 0
                    if personaje.cuerpo.brazoAtaque is not None:
                        for com in (coms:=personaje.cuerpo.brazoAtaque.commmands):
                            print("    ",i,". ",com,"\n")
                            i += 1
                        ele = input()
                        ele = int(ele)
                        coms[ele].ejecutar(personaje)
                    else:
                        print("No hay nada en la mano derecha.")

            if eleccion == "a" or eleccion == "A":
                personaje.atacar()
            
            if eleccion == "h" or eleccion == "H":
                hijos = juego.getChildrenPosition()
                if len(hijos) > 0:
                    print("Selecciona hijo: ")
                    i = 0
                    for hijo in hijos:
                        print("    ",i,". ",hijo)
                        i+=1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    if el < len(hijos) and el >= 0:
                        hijos[el].entrar(personaje)
                    else:
                        print("Has introducido un índice incorrecto.")
            else:
                print("No hay hijos disponibles.")
            
            if eleccion == "c" or eleccion == "C":
                coms = personaje.obtenerComandos(personaje)
                if len(coms) > 0:
                    print("Selecciona comando: ")
                    i = 0
                    for com in coms:
                        print("    ",i,". ",com)
                        i+=1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    if el < len(coms) and el >= 0:
                        coms[el].ejecutar(personaje)
                else:
                    print("Has introducido un índice incorrecto.")
            else:
                print("No hay comandos disponibles.")

            if eleccion == "i" or eleccion == "I":
                print("Inventario:")
                if len(personaje.mochila.children) > 0:
                    for idx, obj in enumerate(personaje.mochila.children):
                        print(f"    {idx}. {obj}")
                    el = input("Selecciona un objeto (número): ")
                    while not el.isdigit() or int(el) < 0 or int(el) >= len(personaje.mochila.children):
                        print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                        el = input("Selecciona un objeto (número): ")
                    
                    coms = personaje.mochila.children[int(el)].obtenerComandos(personaje)
                    if len(coms) > 0:
                        print("Comandos disponibles:")
                        for idx, com in enumerate(coms):
                            print(f"    {idx}. {com}")
                        ele = input("Selecciona un comando (número): ")
                        while not ele.isdigit() or int(ele) < 0 or int(ele) >= len(coms):
                            print("Selección inválida. Introduce un número válido correspondiente al comando.")
                            ele = input("Selecciona un comando (número): ")
                        coms[int(ele)].ejecutar(personaje)
                    else:
                        print("No hay comandos disponibles para este objeto.")
            else:
                print("No hay objetos en la mochila.")
            
    elif forma == "Triangulo":
            print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n",
                "   4. Abrir Puertas\n    5. Lanzar bichos\n    6. Mostrar comandos bolsa\n    7. Mostrar comandos cuerpo\n",
                "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
            
            sys.stdin.flush()
            eleccion = input("Ingresa tu elección: ")

            if eleccion == "1":
                personaje.irAlNorte()
            if eleccion == "2":
                personaje.irAlEste()
            if eleccion == "3":
                personaje.irAlOeste()
            if eleccion == "4":
                juego.openDoors()
            if eleccion == "5":
                juego.fabricarBichoAgresivo(2)
            if eleccion == "6":
                i = 0
                coms=personaje.mochila.obtenerComandos(personaje)
                if len(coms) > 0:
                    for com in coms:
                        print("    ",i,". ",com,"\n")
                        i += 1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    coms[el].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")
            if eleccion == "7":
                print("    1. ¿De verdad quieres usar el brazo ataque?")
                sys.stdin.flush()
                el = input()
                el = int(el)
                if el == 1:
                    i = 0
                    if personaje.cuerpo.brazoAtaque is not None:
                        for com in (coms:=personaje.cuerpo.brazoAtaque.commmands):
                            print("    ",i,". ",com,"\n")
                            i += 1
                        ele = input()
                        ele = int(ele)
                        coms[ele].ejecutar(personaje)
                    else:
                        print("No hay nada en la mano derecha.")

            if eleccion == "a" or eleccion == "A":
                personaje.atacar()
            
            if eleccion == "h" or eleccion == "H":
                hijos = juego.getChildrenPosition()
                if len(hijos) > 0:
                    print("Selecciona hijo: ")
                    i = 0
                    for hijo in hijos:
                        print("    ",i,". ",hijo)
                        i+=1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    if el < len(hijos) and el >= 0:
                        hijos[el].entrar(personaje)
                    else:
                        print("Has introducido un índice incorrecto.")
            else:
                print("No hay hijos disponibles.")
            
            if eleccion == "c" or eleccion == "C":
                coms = personaje.obtenerComandos(personaje)
                if len(coms) > 0:
                    print("Selecciona comando: ")
                    i = 0
                    for com in coms:
                        print("    ",i,". ",com)
                        i+=1
                    sys.stdin.flush()
                    el = input()
                    el = int(el)
                    if el < len(coms) and el >= 0:
                        coms[el].ejecutar(personaje)
                else:
                    print("Has introducido un índice incorrecto.")
            else:
                print("No hay comandos disponibles.")

            if eleccion == "i" or eleccion == "I":
                print("Inventario:")
                if len(personaje.mochila.children) > 0:
                    for idx, obj in enumerate(personaje.mochila.children):
                        print(f"    {idx}. {obj}")
                    el = input("Selecciona un objeto (número): ")
                    while not el.isdigit() or int(el) < 0 or int(el) >= len(personaje.mochila.children):
                        print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                        el = input("Selecciona un objeto (número): ")
                    
                    coms = personaje.mochila.children[int(el)].obtenerComandos(personaje)
                    if len(coms) > 0:
                        print("Comandos disponibles:")
                        for idx, com in enumerate(coms):
                            print(f"    {idx}. {com}")
                        ele = input("Selecciona un comando (número): ")
                        while not ele.isdigit() or int(ele) < 0 or int(ele) >= len(coms):
                            print("Selección inválida. Introduce un número válido correspondiente al comando.")
                            ele = input("Selecciona un comando (número): ")
                        coms[int(ele)].ejecutar(personaje)
                    else:
                        print("No hay comandos disponibles para este objeto.")
            else:
                print("No hay objetos en la mochila.")

        


            

    
        


        

        