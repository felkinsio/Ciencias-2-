#Realizado por
#Kevin Daniel Agudelo Sotelo - 20222020125
#Santiago Alejandro Guada Bohorquez - 20231020182 
#Johan Felipe Pinzon Garcia - 20222020176
#Andres felipe correa mendez - 20221020141


class Nodo:
    def __init__(self, hoja=False):
        self.claves = []
        self.hijos = []
        self.hoja = hoja
        

    @property
    def cant(self):
        return len(self.claves)
    
class ArbolB: 
    
    def __init__(self, maxHijos):
        self.raiz = Nodo(True)
        self.maxHijos = maxHijos

    def dividir(self, nodo_padre, i):
        indice_mediana = (self.maxHijos // 2) - 1
        
        nodo_lleno = nodo_padre.hijos[i]
        nuevo_nodo = Nodo(nodo_lleno.hoja)

        nodo_padre.claves.insert(i, nodo_lleno.claves[indice_mediana])
        nodo_padre.hijos.insert(i + 1, nuevo_nodo)

        nuevo_nodo.claves = nodo_lleno.claves[indice_mediana + 1:]
        nodo_lleno.claves = nodo_lleno.claves[0:indice_mediana]
        
       
        if not nodo_lleno.hoja:
            nuevo_nodo.hijos = nodo_lleno.hijos[self.maxHijos // 2:]
            nodo_lleno.hijos = nodo_lleno.hijos[0:self.maxHijos // 2]

    def insertar(self, clave):
        raiz_actual = self.raiz
        
        if raiz_actual.cant == self.maxHijos - 1:
            nueva_raiz = Nodo()
            self.raiz = nueva_raiz
            nueva_raiz.hijos.insert(0, raiz_actual)
            self.dividir(nueva_raiz, 0)
            self.insertarNoLleno(nueva_raiz, clave)
        else:
            self.insertarNoLleno(raiz_actual, clave)

    def insertarNoLleno(self, nodo, clave):
        i = nodo.cant - 1
        if nodo.hoja:
            nodo.claves.append(0) 
            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i+1] = nodo.claves[i]
                i -= 1
            nodo.claves[i+1] = clave
        else:
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1
            if nodo.hijos[i].cant == self.maxHijos - 1:
                self.dividir(nodo, i)
                if clave > nodo.claves[i]:
                    i += 1
            self.insertarNoLleno(nodo.hijos[i], clave)

    def eliminar(self, clave):
        if not self.raiz:
            print("El árbol está vacío")
            return
        
        self.eliminarRecursivo(self.raiz, clave)

    
        if self.raiz.cant == 0 and not self.raiz.hoja and self.raiz.hijos:
            self.raiz = self.raiz.hijos[0]

    def eliminarRecursivo(self, nodo, clave):
    
        min_claves_suficientes = self.maxHijos // 2
        
        i = 0
        while i < nodo.cant and clave > nodo.claves[i]:
            i += 1
        
        if nodo.hoja:
            if i < nodo.cant and nodo.claves[i] == clave:
                nodo.claves.pop(i)
            else:
                print(f"La clave {clave} no existe en el árbol.")
            return

        if i < nodo.cant and nodo.claves[i] == clave:
            hijo_izq = nodo.hijos[i]
            hijo_der = nodo.hijos[i+1]

            if hijo_izq.cant >= min_claves_suficientes:
                predecesor = self.predecesor(hijo_izq)
                nodo.claves[i] = predecesor
                self.eliminarRecursivo(hijo_izq, predecesor)
            elif hijo_der.cant >= min_claves_suficientes:
                sucesor = self.sucesor(hijo_der)
                nodo.claves[i] = sucesor
                self.eliminarRecursivo(hijo_der, sucesor)
            else:
                self.unir(nodo, i) 
                self.eliminarRecursivo(nodo.hijos[i], clave)
        else:
            hijo = nodo.hijos[i]
            if hijo.cant < min_claves_suficientes:
                self.llenarHijo(nodo, i)
            
            if i > nodo.cant:
                self.eliminarRecursivo(nodo.hijos[i-1], clave)
            else:
                self.eliminarRecursivo(nodo.hijos[i], clave)

    def llenarHijo(self, padre, i):
        min_claves_suficientes = self.maxHijos // 2
        
        if i != 0 and padre.hijos[i-1].cant >= min_claves_suficientes:
            self.prestarAnterior(padre, i)
        elif i != padre.cant and padre.hijos[i+1].cant >= min_claves_suficientes:
            self.prestarSiguiente(padre, i)
        else:
            if i != padre.cant:
                self.unir(padre, i)
            else:
                self.unir(padre, i-1)

    def prestarAnterior(self, padre, i):
        hijo = padre.hijos[i]
        hermano = padre.hijos[i-1]
        
        hijo.claves.insert(0, padre.claves[i-1])
        padre.claves[i-1] = hermano.claves.pop()

        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())

    def prestarSiguiente(self, padre, i):
        hijo = padre.hijos[i]
        hermano = padre.hijos[i+1]

        hijo.claves.append(padre.claves[i])
        padre.claves[i] = hermano.claves.pop(0)

        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))

    def unir(self, padre, i):
        hijo = padre.hijos[i]
        hermano = padre.hijos[i+1]
        
        hijo.claves.append(padre.claves.pop(i))
        hijo.claves.extend(hermano.claves)
        hijo.hijos.extend(hermano.hijos)
        
        padre.hijos.pop(i+1)

    def predecesor(self, nodo):
        while not nodo.hoja:
            nodo = nodo.hijos[-1]
        return nodo.claves[-1]

    def sucesor(self, nodo):
        while not nodo.hoja:
            nodo = nodo.hijos[0]
        return nodo.claves[0]



    def mostrarPorNivel(self):
        if not self.raiz or self.raiz.cant == 0:
            print("El árbol está vacío.")
            return

        cola = [self.raiz]
        nivel = 0
        while cola:
            nodos_en_nivel = len(cola)
            print(f"Nivel {nivel}: ", end="")
            for _ in range(nodos_en_nivel):
                nodo_actual = cola.pop(0)
                print(f"{nodo_actual.claves}", end="  |  ")
                if not nodo_actual.hoja:
                    for hijo in nodo_actual.hijos:
                        cola.append(hijo)
            print()
            nivel += 1


#AQUI SE DEFINE EL NUMERO MAXIMO DE HIJOS
if __name__ == '__main__':    
    arbol = ArbolB(maxHijos=4) 
    while True:
        print("\n1. Insertar clave")
        print("2. Eliminar clave")
        print("3. Mostrar árbol")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                clave = int(input("Ingrese la clave a insertar: "))
                arbol.insertar(clave)
                print(f"Clave {clave} insertada.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")
                
        elif opcion == "2":
            try:
                clave = int(input("Ingrese la clave a eliminar: "))
                arbol.eliminar(clave)
            except ValueError:
                print("Error: Ingrese un número entero válido.")

        elif opcion == "3":
            print("\n--- Visualización del Árbol B por Nivel ---")
            arbol.mostrarPorNivel()
            print("------------------------------------------")

        elif opcion == "4":
            break
            
        else:
            print("Opción inválida")