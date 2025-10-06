# Definición de la clase Pila
class Pila:

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if not self.esVacia():
            return self._elementos.pop()

    def tope(self):
        if not self.esVacia():
            return self._elementos[-1]

    def esVacia(self):
        return len(self._elementos) == 0


# ==== Ejecución interactiva ====

p = Pila()   # Creamos una pila vacía
print("¿Está vacía?", p.esVacia())  

print("\n--- Agregamos elementos ---")
p.push(10)
p.push(20)
p.push(30)
print("Tope actual:", p.tope())      

print("\n--- Sacamos un elemento ---")
print("Elemento sacado:", p.pop())   
print("Nuevo tope:", p.tope())       

print("\n--- Vaciamos toda la pila ---")
print("Sacado:", p.pop())            
print("Sacado:", p.pop())            
print("¿Está vacía ahora?", p.esVacia())  
