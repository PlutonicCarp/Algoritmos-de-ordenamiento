import json
#Matrices donde su proposito es "Descomponer" las sentencias en caracteres
#el usuario "Haro", pasa a ser "H","a","r","o" y rellena los espacios faltantes
#hasta llegar a 8 
usuarios = [["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]]

contraseñas = [["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""]]

#Diccionarios
dic_usuario = {}

dic_contraseñas = {}   

dic_pregunta_uno = {}    

dic_pregunta_dos = {}    

i = 0
#Funcion dedicada a usar los archivos de texto donde se guardan
#las respuestas a las preguntas de seguridad
def cargar_preguntas_seguridad(usuario):
    # Cargar la respuesta de la primera pregunta
    with open(f"respuesta_pregunta1_usuario_{usuario}.txt", "r") as file_p1:
        p1 = file_p1.readline().split(":")[1].strip()

    # Cargar la respuesta de la segunda pregunta
    with open(f"respuesta_pregunta2_usuario_{usuario}.txt", "r") as file_p2:
        p2 = file_p2.readline().split(":")[1].strip()

    return p1, p2


#Funcion que permite registrar usuarios, iniciar sesion o salir.
def menu():
    global i 
    opc = 0
    while opc != 3:
        print("\nBienvenido al login")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        
        try:
            opc = int(input("Ingrese una opción: "))
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
            continue
        
        if opc == 1:
            log_in_result = log_in(usuarios, contraseñas)
            if log_in_result:
                Inicio()

        elif opc == 2:
            registro()

        elif opc == 3:
            print("\nSalida del programa con éxito.")

        else: 
            print("\nOpción no válida.")
            input("\nPresione una tecla para continuar")

#Funcion que permite iniciar sesion dentro de la cuenta
def log_in(usuarios, contraseñas):
    print("\nBienvenido! Para ingresar, ingresa las credenciales requeridas.")
    
    usuario_ingresado = input("\nUsuario: ")
    contraseña_ingresado = input("\nContraseña: ")
    
    k = 0
    while k < 8:
        #Se evalua si el usuario ingresado es igual al usuario 
        #en dicho diccionario y su indice, lo mismo con su contraseña
        if k in dic_usuario and usuario_ingresado == dic_usuario[k]:
            if k in dic_contraseñas and contraseña_ingresado == dic_contraseñas[k]:
                print("Inicio de sesion exitoso. !Bienvenido!")
                return True
            else:
                print("Contraseña o usuario incorrecto. ")
                return False
        k += 1
    
    print("Usuario no encontrado.")
    input("\nPresione una tecla para continuar")
    return False

#Funcion para registrar usuarios y guardarlos en su matriz y diccionarios
def registro():
    global usuarios, contraseñas
    
    
    while True:
                i = len(dic_usuario)
                user = input(f"\n{i+1}. Ingresa el nombre de usuario: ")
                dic_usuario[i] = user
                print(dic_usuario)
                contra = input(f"\n{i+1}. Ingresa su contraseña: ")
                #Validacion de contraseña con 8 caracteres
                while len(contra) != 8:
                    print("\nLa contraseña debe tener 8 caracteres.")
                    contra = input(f"\n{i+1}. Ingresa su contraseña: ") 
                dic_contraseñas[i] = contra
                
                #Preguntas de seguridad
                p1 = (input("Nombre de tu mejor amigo: "))
                p2 = (input("¿Donde se conocieron tus padres? "))
                
                guardar_preguntas_seguridad(i, p1, p2)
                
                #Guardar los datos en la matriz que descompone en caracteres
                usuarios[i] = list(user.ljust(8))
                contraseñas[i] = list(contra.ljust(8))
                
                i += 1
                print("\nUsuario registrado con éxito.")
                
                #Pregunta para romper el bucle y volver al menu (El lower sirve para volver a minusculas)
                opcion = input("¿Deseas registrar otro usuario? (Sí/No): ").lower()
                if opcion != 'si':
                    break

#Funcion para almacenar las respuestas a las preguntas de seguridad en 
#archivos de texto
def guardar_preguntas_seguridad(i, p1, p2):
    # Guardar la respuesta a la primera pregunta de seguridad en un archivo
    with open(f"respuesta_pregunta1_usuario_{i}.txt", "w") as file_p1:
        file_p1.write(f"Pregunta 1: {p1}\n")
    
    # Guardar la respuesta a la segunda pregunta de seguridad en otro archivo
    with open(f"respuesta_pregunta2_usuario_{i}.txt", "w") as file_p2:
        file_p2.write(f"Pregunta 2: {p2}\n")

#Funcion que, una vez iniciada sesion en una cuenta permite ya sea mostrar
#usuarios, contraseñas, restablecer contraseña y mostrar metodos de ordenamiento
#y de arbol
def Inicio():
    print("\n¿Qué deseas hacer?")
    print("1. Mostrar usuarios")
    print("2. Mostrar contraseñas")
    print("3. Restablecer contraseña")
    print("4. Algoritmos de ordenamiento")
    print("5. Estructuras de arbol")
    print("6. Cerrar sesión")
    #Es necesario el tipo de dato int ya que de lo contrario se omite la eleccion
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("\nLista de usuarios: ", usuarios)
        input("\nPresione una tecla para continuar")
        Inicio()
    elif opcion == 2:
        print("\nLista de contraseñas: ", contraseñas)
        input("\nPresione una tecla para continuar")
        Inicio()
    elif opcion == 3:
        restablecer_contraseña()
    elif opcion == 4:
        algoritmos_ordenamiento()
    elif opcion== 5:
        algoritmos_arbol()
    elif opcion == 6:
        print("\nCerrando sesión")
        input("\nPresione una tecla para continuar")
        menu()
    else:
        print("\nOpción no válida.")
        input("\nPresione una tecla para continuar")
        Inicio()

#Funcion dedicada a el menu de restablecer contraseña y su aplicacion
def restablecer_contraseña():
    opcion = 0
    j = 0
    print("\nMenú para restablecer contraseña\n")
    print("1. Ingresar contraseña")
    print("2. Olvidé mi contraseña")
    print("3. Salir")

    opcion = int(input("\nElige alguna de las opciones: "))

    if opcion == 1:
        usuario_ingresado = input("\nIngresa tu nombre de usuario: ")
        contraseña_actual = input("Ingresa tu contraseña actual: ")

        for i in range(len(dic_usuario)):
            if dic_usuario[i] == usuario_ingresado and dic_contraseñas[i] == contraseña_actual:
                nueva_contra = input("Ingresa la nueva contraseña: ")
                while len(nueva_contra) != 8:
                    print("\nLa contraseña debe tener 8 caracteres.")
                    nueva_contra = input("Ingresa la nueva contraseña: ")

                dic_contraseñas[i] = nueva_contra
                print("Contraseña restablecida con éxito.")
                break
        else:
            print("Nombre de usuario o contraseña actual incorrectos.")
            input("\nPresione una tecla para continuar")
            Inicio()
    elif opcion == 2:
        usuario_ingresado = input("Ingresa tu nombre de usuario: ")

        for i in range(len(dic_usuario)):
            if dic_usuario[i] == usuario_ingresado:
                p1, p2 = cargar_preguntas_seguridad(i)
                
                print(f"Nombre de tu mejor amigo: ")
                respuesta_p1 = input("Tu respuesta: ")

                print(f"¿Donde se conocieron tus padres? ")
                respuesta_p2 = input("Tu respuesta: ")
                
                if respuesta_p1 == p1 and respuesta_p2 == p2:
                    nueva_contra = input("Ingresa la nueva contraseña: ")
                    while len(nueva_contra) != 8:
                        print("\nLa contraseña debe tener 8 caracteres.")
                        nueva_contra = input("Ingresa la nueva contraseña: ")

                    dic_contraseñas[i] = nueva_contra
                    contraseñas[i] = list(nueva_contra.ljust(8))
                    
                    print("Contraseña restablecida con éxito.")
                    break
                else:
                    print("Respuestas de seguridad incorrectas.")
        else:
            print("Usuario no encontrado.")
    elif opcion == 3:
        print("Volviendo a el menú principal")
        Inicio()
    else:
        print("\nOpcion no valida")
        restablecer_contraseña()

#Funcion donde se puede ver la implementacion y explicacion de los metodos
#de ordenammiento        
def algoritmos_ordenamiento():
    print("\nBienvenido al menu de algoritmos de ordenamiento.")
    print("\nElige el metodo que quieres revisar. \n")
    
    print("1. Bubble sort")
    print("2. Cocktail sort")
    print("3. Insertion sort")
    print("4. Bucket sort")
    print("5. Counting sort")
    print("6. Merge sort")
    print("7. Shell sort")
    print("8. Comb sort")
    print("9. Selection sort")
    print("10. Salir")
    
    try:
        eleccion = int(input("Escribe tu eleccion: "))
    except ValueError:
        print("\nPor favor, ingrese un número válido.")
        algoritmos_ordenamiento()
    
    if eleccion == 1:
        bubblesort()
    elif eleccion == 2:
        cocktailsort()
    elif eleccion == 3:
        insertion_sort()
    elif eleccion == 4:
        bucket_sort()
    elif eleccion == 5:
        counting_sort()
    elif eleccion == 6:
        merge_sort()
    elif eleccion== 7:
        shell_sort()
    elif eleccion == 8:
        comb_sort()
    elif eleccion ==9:
        selection_sort()
    elif eleccion == 10:
        print("\nRegresando al menú principal.")
        input("\nPresione una tecla para continuar")
        Inicio()
    else:
        print("\nOpción invalida")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
            
#Funcion del metodo de ordenamiento bubblesort
def bubblesort():
    print("\nEscogiste bubblesort, ahora solo elige.")
    
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")
    
    b_opc = int(input("Escribe tu elección: "))
    
    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)
        
        consultas = 0  
        movimientos = 0  
        iteraciones = 0
        n = len(array)
        
        for i in range(n):
            # Se inicia un flag para optimizar el algoritmo. Si no hay intercambios, el arreglo ya está ordenado.
            swapped = False
            for j in range(0, n-i-1):
                consultas += 1  # Contamos cada comparación realizada.
                print(f"Iteración {iteraciones+1}, Consulta {consultas}: Comparando {array[j]} > {array[j+1]}")
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    movimientos += 1  # Contamos el movimiento (intercambio).
                    swapped = True
                    print(f"Movimiento {movimientos}: Intercambiando {array[j+1]} con {array[j]} -> {array}")
            iteraciones += 1
            if not swapped:
                # Si no hubo intercambios, el arreglo ya está ordenado y se puede salir del bucle.
                break
        
        print("Lista ordenada:", array)
        print("Número de movimientos:", movimientos)
        print("Número de consultas:", consultas)
        print("Número de iteraciones:", iteraciones)
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    elif b_opc==2:
        print(" El algoritmo de ordenamiento burbuja, también conocido como Bubble Sort en inglés\n")
        print(" es un sencillo algoritmo de ordenamiento que funciona comparando pares de elementos ")
        print("adyacentes en una lista y intercambiándolos si están en el orden incorrecto.")
        print("Este proceso se repite hasta que la lista esté ordenada.")
        
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
        
    else:
        print("Opcion no valida. ")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()

def cocktailsort():
    print("\nEscogiste cocktailsort, ahora solo elige.")
    
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite culaquier otra cosa para vover al menu de metodos de ordenamiento")
    
    b_opc = int(input("Escribe tu eleccion: "))
    
    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)

        consultas = 0  
        movimientos = 0  
        iteraciones = 0
        n = len(array)

        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            # Pasada hacia adelante
            for i in range(start, end):
                consultas += 1
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    movimientos += 1
                    swapped = True
            if not swapped:
                break
            swapped = False
            end = end - 1

        # Pasada hacia atrás
            for i in range(end - 1, start - 1, -1):
                consultas += 1
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    movimientos += 1
                    swapped = True
            start = start + 1
            iteraciones += 1  # Una iteración completa se cuenta después de ambas pasadas.

        print("Lista ordenada:", array)
        print("Número de movimientos:", movimientos)
        print("Número de consultas:", consultas)
        print("Número de iteraciones:", iteraciones)
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    elif b_opc == 2:
        """Este algoritmo acelerará las tortugas cambiando de dirección en cada iteración. 
        Así, con cada cambio de dirección, los “conejos” se convierten en “tortugas” y viceversa. 
        Esto no sólo permite que los elementos más grandes migren rápidamente al final de la lista,
        sino que también permite que los elementos más pequeños migren más rápido al principio."""
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    else:
        print("Opcion no valida. ")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
        
def insertion_sort():
    print("\nEscogiste insertion sort, ahora solo elige.")
    
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite culaquier otra cosa para vover al menu de metodos de ordenamiento")
    
    b_opc = int(input("Escribe tu eleccion: "))
        
    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)
        
        consultas = 0  
        movimientos = 0  
        iteraciones = 0
        n = len(array)
        
        for i in range(1, n):
            key = array[i]
            j = i - 1
            # Se agregó una variable para rastrear si se realizó un movimiento dentro del while.
            seMovio = False  
            while j >= 0 and array[j] > key:
                consultas += 1  # Se realiza una consulta aquí.
                array[j + 1] = array[j]
                seMovio = True
                j -= 1
            if seMovio:
                movimientos += 1  # Se contabiliza un movimiento si realmente se movió al menos una vez.
            array[j + 1] = key
            iteraciones += 1  # Cada paso completo por el arreglo cuenta como una iteración.
            if not seMovio:
                consultas += 1  # Asegurando que se cuenta una consulta incluso si no hubo movimientos.

        print("Lista ordenada:", array)
        print("Número de movimientos:", movimientos)
        print("Número de consultas:", consultas)
        print("Número de iteraciones:", iteraciones)
        input("\nPresione una tecla para continuar")
    if b_opc == 2:
        """Inicialmente, se tiene un solo elemento que, obviamente, es un conjunto ordenado. Después, cuando hay 
         k elementos ordenados de menor a mayor se toma el elemento k+1 
         y se compara con todos los elementos ya ordenados, deteniéndose cuando se encuentra un elemento menor (todos los elementos mayores han sido desplazados una posición a la derecha) o cuando ya no se encuentran elementos (todos los elementos fueron desplazados y este es el más pequeño). 
         En este punto se inserta el elemento k+1 debiendo desplazarse los demás elementos."""
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    else:
        print("Opcion no valida. ")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()

def selection_sort():
    print("\nEscogiste selection sort, ahora solo elige.")
    
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")
    
    b_opc = int(input("Escribe tu elección: "))
    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)

        movimientos = 0
        iteraciones = 0
        consultas = 0

        for i in range(len(array)): #For para recorrer el arreglo
            iteraciones += 1
            min_idx = i
            for j in range(i+1, len(array)): #For para comparar cada elmento del arreglo
                consultas += 1
                print(f"Consulta {consultas}: ¿{array[j]} < {array[min_idx]}?")
                if array[min_idx] > array[j]: #Si el elemento actual es mayor al siguiente, se intercambian
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            movimientos += 1
            print(f"Movimiento {movimientos}: Intercambiando {array[min_idx]} con {array[i]} -> {array}")
                
        print(f'La lista ordenada es: {array}')
        print(f'Número de iteraciones: {iteraciones}')
        print(f'Número de consultas: {consultas}')
        print(f'Número de movimientos: {movimientos}')
        input("\nPresione una tecla para continuar")
        
    elif b_opc == 2: 
        """Funciona de la siguiente manera:
        Buscar el Elemento Mínimo: Comienza buscando el elemento más pequeño en el arreglo.

        Intercambiar: Una vez encontrado el elemento mínimo, se intercambia con el elemento en la primera posición
        del arreglo (es decir, se coloca el elemento mínimo al inicio del arreglo).

        Repetir con Sublista Restante: A continuación, el proceso se repite para la sublista restante del arreglo 
        (es decir, el arreglo excluyendo el primer elemento ya ordenado), buscando el mínimo en esta sublista y colocándolo en la segunda posición.

        Continuar hasta Ordenar Todo el Arreglo: Este proceso se repite para cada posición en el arreglo, hasta 
        que la sublista restante se reduce a un solo elemento, momento en el cual el arreglo entero estará ordenado."""
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    else:
        print("Opcion no valida. ")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()

def counting_sort():
    print("\nEscogiste counting sort, ahora solo elige.")
    
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")
    
    b_opc = int(input("Escribe tu elección: "))
    
    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)
        
        consultas = 0  
        movimientos = 0  
        iteraciones = 0
        n = len(array)
    
def bucket_sort(num_buckets=20):
    print("\nEscogiste bucket sort, ahora solo elige.")
    
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")
    
    b_opc = int(input("Escribe tu elección: "))
    
    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)
        
        consultas = 0  
        movimientos = 0  
        iteraciones = 0
        n = len(array)
        minimo = min(array)
        maximo = max(array)
        rango = maximo - minimo + 1

        tamaño_buckets = rango // num_buckets
        buckets = [[] for _ in range(num_buckets)]

        consultas_buckets = 0
        comparaciones_buckets = 0
        movimientos_buckets = 0
        iteraciones_buckets = 0

        for num in array:
            consultas_buckets += 1
            if num < 0:
                indice = 0
            else:
                indice = min((num - minimo) // tamaño_buckets, num_buckets - 1)
            buckets[indice].append(num)

        print("Buckets desordenados:")
        for i, bucket in enumerate(buckets):
            print(f"Bucket {i}: {bucket}")

        for i in range(num_buckets):
            comparaciones_i, movimientos_i, consultas_i, iteraciones_i = insertion_sort_aux(buckets[i])
            comparaciones_buckets += comparaciones_i
            movimientos_buckets += movimientos_i
            consultas_buckets += consultas_i
            iteraciones_buckets += iteraciones_i

        print("\nBuckets ordenados:")
        for i, bucket in enumerate(buckets):
            print(f"Bucket {i}: {bucket}")

        # Concatenando buckets ordenados
        arreglo_ordenado = []
        for bucket in buckets:
            arreglo_ordenado.extend(bucket)
            
        print("\nArreglo ordenado (Bucket Sort):", arreglo_ordenado)
        print("Consultas realizadas (Bucket Sort):", consultas_buckets)
        print("Comparaciones realizadas (Bucket Sort):", comparaciones_buckets)
        print("Movimientos realizados (Bucket Sort):", movimientos_buckets)
        print("Iteraciones realizadas (Bucket Sort):", iteraciones_buckets)
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
        
        return arreglo_ordenado, consultas_buckets, comparaciones_buckets, movimientos_buckets, iteraciones_buckets  
    if b_opc==2:
        """El algoritmo divide el arreglo original en mitades hasta que cada subarreglo contenga un solo elemento o ningún elemento. 
        Esto se hace de manera recursiva.
        Luego, comienza a combinar esos subarreglos (que consideramos ordenados) de dos en dos, ordenándolos en el proceso. 
        Este paso de "conquista" se realiza mediante una función auxiliar, comúnmente llamada merge, que se encarga de fusionar
        dos subarreglos ordenados en un solo subarreglo ordenado.
        Finalmente, el proceso de combinación continúa hasta que todos los subarreglos se han fusionado de nuevo en un único arreglo ordenado."""
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    else:
        print("Opcion no valida. ")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
def insertion_sort_aux(lista):
    comparaciones = 0
    movimientos = 0
    consultas = 0
    iteraciones = 0
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and temp < lista[j]:
            comparaciones += 1
            consultas += 1  # Contar la consulta realizada
            lista[j + 1] = lista[j]
            j -= 1
            movimientos += 1
            iteraciones += 1
        lista[j + 1] = temp
        movimientos += 1
        consultas += 1  # Contar la consulta realizada al asignar temp
        iteraciones += 1
    return comparaciones, movimientos, consultas, iteraciones

def merge_sort(array=None):
    global iteraciones, consultas, movimientos
    iteraciones, consultas, movimientos = 0, 0, 0

    if array is None:
        print("\nEscogiste merge sort, ahora solo elige.")
        print("1. Ver implementacion ")
        print("2. Ver explicacion")
        print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")
        
        b_opc = int(input("Escribe tu elección: "))
        
        if b_opc == 1:
            array = []
            size = int(input("Ingresa el tamaño del arreglo: "))
            for k in range(size):
                a = int(input(f"{k+1}. Ingresa el dato:  "))
                array.append(a)
            
            sorted_array, _, _, _ = merge_sort(array)  # Recibir y descartar los contadores aquí
            print("Arreglo ordenado:", sorted_array)
            print("Iteraciones:", iteraciones)
            print("Consultas:", consultas)
            print("Movimientos:", movimientos)
            input("\nPresione una tecla para continuar")
        elif b_opc == 2:
            print("El algoritmo de merge sort divide el arreglo en mitades, las ordena y luego las mezcla.")
            input("\nPresione una tecla para continuar")
            algoritmos_ordenamiento()
        else:
            print("\nVolviendo al menú principal.")
            input("\nPresione una tecla para continuar")
            algoritmos_ordenamiento()
        return  # Finalizamos la ejecución si estábamos mostrando el menú
    if len(array) < 2:
        return array, 0, 0, 0
    
    middle = len(array) // 2
    left, li, lc, lm = merge_sort(array[:middle])
    right, ri, rc, rm = merge_sort(array[middle:])
    merged, mi, mc, mm = merge(left, right)
    
    # Sumar contadores de iteraciones, consultas y movimientos
    iteraciones += li + ri + mi
    consultas += lc + rc + mc
    movimientos += lm + rm + mm
    
    return merged, iteraciones, consultas, movimientos

def merge(left, right):
    iteraciones = 0
    consultas = 0
    movimientos = 0

    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        iteraciones += 1
        consultas += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        movimientos += 1

    movimientos += len(left[i:]) + len(right[j:])
    result.extend(left[i:])
    result.extend(right[j:])

    return result, iteraciones, consultas, movimientos

def shell_sort():
    counters = {'iteraciones': 0, 'consultas': 0, 'movimientos': 0}

    print("\nEscogiste shell sort, ahora solo elige.")
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")

    b_opc = int(input("Escribe tu elección: "))

    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)

        n = len(array)
        gap = n // 2

        while gap > 0:
            counters['iteraciones'] += 1
            print(f"Iteración con gap {gap}:")
            for i in range(gap, n):
                temp = array[i]
                j = i
                counters['consultas'] += 1
                print(f"Consulta: Comparando {array[j - gap]} y {temp}")
                while j >= gap and array[j - gap] > temp:
                    counters['movimientos'] += 1
                    print(f"Movimiento: Intercambiando {array[j - gap]} y {array[j]}")
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2

        print("Arreglo ordenado:", array)
    elif b_opc == 2:
        print("El algoritmo de Shell Sort mejora el ordenamiento por inserción al permitir el intercambio de elementos con varios lugares de distancia. Se comienza con un gap grande que se reduce gradualmente. Esto permite a elementos lejanos moverse a posiciones más apropiadas rápidamente.")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()
    else:
        print("\nVolviendo al menú principal.")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()

    if b_opc == 1:
        print("Iteraciones:", counters['iteraciones'])
        print("Consultas:", counters['consultas'])
        print("Movimientos:", counters['movimientos'])
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()

def comb_sort():
    counters = {'iteraciones': 0, 'consultas': 0, 'movimientos': 0}

    print("\nEscogiste comb sort, ahora solo elige.")
    print("1. Ver implementacion ")
    print("2. Ver explicacion")
    print("\nDigite cualquier otra cosa para volver al menu de métodos de ordenamiento")

    b_opc = int(input("Escribe tu elección: "))

    if b_opc == 1:
        array = []
        size = int(input("Ingresa el tamaño del arreglo: "))
        for k in range(size):
            a = int(input(f"{k+1}. Ingresa el dato:  "))
            array.append(a)
            
         # Inicializar el gap
        gap = len(array)
        # Inicializar el swapped como true para entrar al bucle
        swapped = True
        shrink = 1.3  # Factor común de reducción

        while gap > 1 or swapped:
            # Encuentra el siguiente gap
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            swapped = False
            counters['iteraciones'] += 1  # Cada vez que se completa una pasada

            # Hacer un recorrido con el gap actual
            for i in range(0, len(array) - gap):
                counters['consultas'] += 1  # Por cada comparación
                if array[i] > array[i + gap]:
                    # Si estos elementos están en el orden equivocado, intercambiarlos
                    array[i], array[i + gap] = array[i + gap], array[i]
                    swapped = True
                    counters['movimientos'] += 1  # Por cada intercambio

        print("Arreglo ordenado:", array)
    elif b_opc == 2:
        print("El algoritmo de Comb Sort mejora el Bubble Sort al eliminar los 'conejos de tortuga' mediante el uso de un gap que se reduce en cada pasada. Es más eficiente y suele usar un factor de reducción de 1.3.")
        input("\nPresione una tecla para continuar")
    else:
        print("\nVolviendo al menú principal.")
        input("\nPresione una tecla para continuar")
        algoritmos_ordenamiento()

    if b_opc == 1:
        print("Iteraciones:", counters['iteraciones'])
        print("Consultas:", counters['consultas'])
        print("Movimientos:", counters['movimientos'])
        input("\nPresione una tecla para continuar")

#Funcion donde se puede ver la implementacion y explicacion de los metodos
#arbol     
def algoritmos_arbol():
    print("\nBienvenido al menu de algoritmos de arbol.")
    print("\nElige el metodo que quieres revisar. \n")
    
    print("1. Binary tree sort")
    print("2. ")
    
    try:
        eleccion = int(input("Escribe tu eleccion: "))
    except ValueError:
        print("\nPor favor, ingrese un número válido.")
        algoritmos_arbol()
        
    if eleccion == 1:
        binary_tree()
    elif eleccion == 2:
        arbol_avl()
#Clase donde se definen los nodos que serán usados por ambos arboles. 
class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key
            self.height = 1  
#Arbol de tipo binario con inserción. 
def binary_tree():
    root = None
    while True:
        try:
            data = input("Ingrese un número para insertar en el árbol (o 'salir' para terminar): ")
            if data.lower() == 'salir':
                break
            data = int(data)
            root = insert(root, data)
            print("\nÁrbol binario actual:")
            print_tree(root)
        except ValueError:
            print("Por favor, ingrese un número válido.")
     
def insert(root, key):
    """ Inserta un nuevo nodo con la clave especificada en el árbol binario. """
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree(root, depth=0, prefix=""):
    """ Imprime el árbol visualmente con espaciado y nodos alineados """
    if root is not None:
        print_tree(root.right, depth + 1, "    ")
        print(" " * (depth * 4) + prefix + str(root.val))
        print_tree(root.left, depth + 1, "    ")    

#Arbol tipo avl y las funciones para reasignar los datos según los datos.
def arbol_avl():
    root = None
    while True:
        try:
            data = input("Ingrese un número para insertar en el árbol (o 'salir' para terminar): ")
            if data.lower() == 'salir':
                break
            data = int(data)
            root = insert(root, data)
            print("\nÁrbol AVL actual:")
            print_tree(root)
        except ValueError:
            print("Por favor, ingrese un número válido.")

def update_height(node):
    """ Actualiza la altura del nodo basada en las alturas de sus hijos """
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_height(node):
    """ Obtiene la altura del nodo, considerando 0 si el nodo es None """
    if not node:
        return 0
    return node.height

def get_balance(node):
    """ Calcula el balance del nodo como la diferencia entre las alturas de los subárboles izquierdo y derecho """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    """ Realiza una rotación a la derecha """
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def left_rotate(x):
    """ Realiza una rotación a la izquierda """
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    """ Inserta un nuevo nodo de manera recursiva y lo balancea si es necesario """
    if not node:
        return Node(key)
    elif key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    update_height(node)
    balance = get_balance(node)

    # Rotación Simple Derecha
    if balance > 1 and key < node.left.val:
        return right_rotate(node)
    # Rotación Simple Izquierda
    if balance < -1 and key > node.right.val:
        return left_rotate(node)
    # Rotación Doble Izquierda-Derecha
    if balance > 1 and key > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # Rotación Doble Derecha-Izquierda
    if balance < -1 and key < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def print_tree(root, depth=0, prefix=""):
    """ Imprime el árbol visualmente """
    if root is not None:
        print_tree(root.right, depth + 1, "    ")
        print(" " * (depth * 4) + prefix + str(root.val))
        print_tree(root.left, depth + 1, "    ")

arbol_avl()
menu()