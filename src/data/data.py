class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        listaInvertida = []
        indice = len(lista) - 1
        while indice >= 0:
            listaInvertida.append(lista[indice])
            indice -= 1
        return listaInvertida
        pass
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for indice, valor in enumerate(lista): #obtiene tanto el indice como el elemento
            if valor == elemento:
                return indice
        return -1
        pass
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        listaSinDuplicados = []
        elementosDuplicados =[]
        for i in lista:
            elemento = (i, type(i)) #obtiene el tipo de dato
            if elemento not in elementosDuplicados:
                elementosDuplicados.append(elemento)
                listaSinDuplicados.append(i) #agrega elementos a la lista
        return listaSinDuplicados
        pass
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        return sorted(lista1 + lista2)
        pass
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
            return []

        for i in range(k):
            aux = lista[len(lista) - 1] #se guarda el ultimo elemento en aux
            for j in range(len(lista) - 1, 0, -1):
                lista[j] = lista[j - 1]
            lista[0] = aux #elemento guardado en aux se pone en primera posicion de la lista
        return lista    
        pass
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1  # número total de elementos
        sumaTotal = n * (n + 1) // 2  # suma de los primeros n números
        sumaLista = sum(lista)
        return sumaTotal - sumaLista
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for i in conjunto1:
            if i not in conjunto2:
                return False
        return True
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = [] #Last In First Out

        def push(elemento): #agrega elemento en la ultima posicion
            pila.append(elemento)

        def pop(): #elimina el ultimo elemento
            if not is_empty():
                return pila.pop()
            else:
                return None  

        def peek(): #devuelve el elemento que esta en el tope
            if not is_empty():
                return pila[-1]
            else:
                return None  

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty,
        }

        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = [] #First In First Out

        def enqueue(elemento): #añade un elemento al inicio
            cola.append(elemento)
        
        def dequeue(): #elimina el primer elemento
            if not len(cola) == 0:
                return cola.pop(0)
            else:
                return None  

        def peek(): #devuelve el primer elemento
            if not len(cola) == 0:
                return cola[0]
            else:
                return None 
        
        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty,
        }

        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz or not matriz[0]:  # verifica si la matriz está vacía
            return []

        transpuesta = []

        for i in range(len(matriz[0])):
            transpuesta.append([])
            for j in range(len(matriz)):
                transpuesta[i].append(matriz[j][i])
        return transpuesta        

        pass