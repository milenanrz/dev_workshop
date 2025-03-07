class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        pass
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        else:
            fibo = [0, 1]
            while len(fibo) < n:
                siguiente = fibo[-1] + fibo[-2]
                fibo.append(siguiente)
            return fibo
        pass
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True 
        pass
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        lista = []
        cont = 0

        for i in range(2, n+1):
            for j in range(2, int(i/2) + 1):
                if i % j == 0:
                    cont += 1

            if cont == 0:
                lista.append(i)
            cont = 0    
        
        return lista
        pass
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n <= 1: #numeros perfectos son mayores a 1
            return False 

        suma = 0
        for i in range(1, n):
            if n%i == 0:
                suma += i
        
        return suma == n
        pass
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        matriz = [] #guarda las filas
        aux = 0

        for x in range(filas):
            matriz.append([])

        for x in range(filas):
            for y in range (x+1):
                if y==0 or y==x: #para que los extremos sean 1
                    matriz[x].append(1)
                else:    
                    aux = matriz[x-1][y] + matriz[x-1][y-1]
                    matriz[x].append(aux)

        return matriz    
        pass
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        c = 1
        fac = 1
        while (c<=n):
            fac=fac*c
            c=c+1
        
        return fac
        pass 
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a 
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        #guardan el valor original de a y b
        a0 = a 
        b0 = b 

        while b != 0:
            temp = b
            b = a % b
            a = temp

        mcd = a
        mcm = abs(a0 * b0) // mcd

        return mcm

        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        suma = 0
        while n > 0:
            suma += n%10
            n //= 10
        return suma
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        conv = str(n) #convierte el numero en string
        aux = 0 

        for i in range(len(conv)):
            aux += (int(conv[i]) ** len(conv)) #accede a los digitos del numero

        if aux == n: 
            return True
        else:
            return False    
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        if len(matriz) == len(matriz[0]): #si filas es igual a columnas
            suma = sum(matriz[0])

            for i in range(1, len(matriz)):
                if suma != sum(matriz[i]):
                    return False

            for j in range(len(matriz[0])):
                sumaColumna = sum([matriz[i][j] for i in range(len(matriz))])
                if suma != sumaColumna:
                    return False
            
            
            sumaDiagonalPrincipal = sum([matriz[i][i] for i in range(len(matriz))])
            if suma != sumaDiagonalPrincipal:
                return False

            columnas = len(matriz[0]) - 1
            sumaDiagonalSecundaria = 0
            for i in range(len(matriz)):
                sumaDiagonalSecundaria += matriz[i][columnas]
                columnas -= 1
            return suma == sumaDiagonalSecundaria    

        else:
            return False
        pass