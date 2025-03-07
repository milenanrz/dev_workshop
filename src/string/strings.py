class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = texto.lower() #convierte mayusculas en minuscular
        texto = texto.replace(" ", "") #quita los espacios
        texto = texto.replace("á", "a") #quita las tildes
        texto = texto.replace("é", "e")
        texto = texto.replace("í", "i")
        texto = texto.replace("ó", "o")
        texto = texto.replace("ú", "u")

        primerIndice = 0
        ultimoIndice = len(texto) - 1

        for i in range(0, len(texto)):
            if texto[primerIndice] == texto[ultimoIndice]:
                primerIndice += 1
                ultimoIndice -= 1
            else:
                return False
        return True            
        pass
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        reverso = "" 
        for i in texto: 
            reverso = i + reverso #
        return reverso    
        pass
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        cont = 0
        for i in texto:
            if i in vocales:
                cont += 1
        
        return cont
        pass
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        texto = texto.lower()
        consonantes = "bcdfghjklmnpqrstvwxyz"
        cont = 0
        for i in texto:
            if i in consonantes:
                cont += 1
        
        return cont
        pass
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1 = texto1.lower().replace(" ", "")
        texto2 = texto2.lower().replace(" ", "")

        if len(texto1) != len(texto2):
            return False
        return sorted(list(texto1)) == sorted(list(texto2))
        pass
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        texto = texto.strip() #elimina espacios iniciales y finales de la cadena

        if not texto:
            return 0
        
        texto = texto.split()
        return len(texto)
        pass
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        return texto.title()
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        texto = texto.split()
        return " ".join(texto)
        pass 
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if not texto: 
            return False

        if texto[0] in ('-', '+'): #elimina el signo de la cadena
            texto = texto[1:]
        
        if not texto: #verifica si despues de eliminar el signo la cadena esta vacia
            return False

        for i in texto:
            if not '0' <= i <= '9':
                return False

        return True
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass