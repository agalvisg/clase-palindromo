
class Palindromo():
    
    def __init__(self,palabra):
        self.palabra=palabra
        
    def get_palabra(self):
        return palabra
    
    def es_palindromo():
        palabra=self.palabra.replace('','').lower()
        return palabra == palabra[::-1]
    
    def resultado(self):
        if self.es_palindromo():
            return f"la palabra {self.palabra} es un palindromo"
        else: 
            return f"la palabra {self.palabra} no es un palindrmo"

    def test (self):
        return (self.es_palindromo(),self.palabra.upper())  
          
    def __str__(self):
        return self.resultado
    
    
def main():
    palabra = input ("Escribe una palabra: ")
    palindromo= Palindromo(palabra)
    print(palindromo)

if __name__ =="main":
    main()