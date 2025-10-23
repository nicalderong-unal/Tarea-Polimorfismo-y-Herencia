#Autor: Nicolás Alexander Calderón García

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def esperar_enter(mensaje="\nPresione Enter para continuar..."):
    input(mensaje)


class Animal:
    
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass
    
    def moverse(self):
        pass
    
    def describeme(self):
        print(f"Soy un Animal del tipo {type(self).__name__}")


class Gato(Animal):
    
    def __init__(self, especie, edad, color_pelaje):
        super().__init__(especie, edad)
        self.color_pelaje = color_pelaje
    
    def hablar(self):
        print("Miau! Mrrr...")
    
    def moverse(self):
        print("Caminando sigilosamente con 4 patas")
    
    def describeme(self):
        print(f"Hola, soy un {self.especie} de {self.edad} años con pelaje {self.color_pelaje}")
    
    def ronronear(self):
        print("Prrrrr... prrrrr... (ronroneando felizmente)")
    
    def afilar_unas(self):
        print("Afilando mis unas en el sofa...")


class Pez(Animal):
    
    def __init__(self, especie, edad, tipo_agua):
        super().__init__(especie, edad)
        self.tipo_agua = tipo_agua
    
    def hablar(self):
        print("Glub glub... (hace burbujas)")
    
    def moverse(self):
        print("Nadando suavemente moviendo sus aletas")
    
    def describeme(self):
        print(f"Hola, soy un {self.especie} de {self.edad} años que vive en agua {self.tipo_agua}")
    
    def nadar_rapido(self):
        print("Nadando rapidamente para escapar del depredador!")
    
    def hacer_burbujas(self):
        print("Glub glub glub... (haciendo muchas burbujas)")


class Mapache(Animal):
    
    def __init__(self, especie, edad, habitat):
        super().__init__(especie, edad)
        self.habitat = habitat
    
    def hablar(self):
        print("Chirp chirp! (sonidos de mapache)")
    
    def moverse(self):
        print("Caminando con sus patas habilidosas y trepando arboles")
    
    def describeme(self):
        print(f"Hola, soy un {self.especie} de {self.edad} años que vive en {self.habitat}")
    
    def lavar_comida(self):
        print("Lavando mi comida en el agua antes de comerla!")
    
    def buscar_basura(self):
        print("Buscando comida deliciosa en los botes de basura...")


def hacer_sonido(animal: Animal):
    animal.hablar()


def mostrar_movimiento(animal: Animal):
    animal.moverse()


def main():
    limpiar_consola()
    
    print("=" * 60)
    print(" DEMOSTRACION DE POLIMORFISMO EN PYTHON")
    print("=" * 60)
    esperar_enter()
    
    print("\n--- CREANDO ANIMALES ---\n")
    
    print("Creando un Gato...")
    mi_gato = Gato("Mamifero", 3, "naranja")
    print("Gato creado!")
    esperar_enter()
    
    print("\nCreando un Pez...")
    mi_pez = Pez("Pez tropical", 1, "dulce")
    print("Pez creado!")
    esperar_enter()
    
    print("\nCreando un Mapache...")
    mi_mapache = Mapache("Mamifero", 4, "bosque urbano")
    print("Mapache creado!")
    esperar_enter()
    
    limpiar_consola()
    
    animales = [mi_gato, mi_pez, mi_mapache]
    
    print("=" * 60)
    print(" DEMOSTRACION DE POLIMORFISMO")
    print("=" * 60)
    print("\n(mismo metodo, diferente comportamiento.)")
    esperar_enter()
    
    for i, animal in enumerate(animales, 1):
        limpiar_consola()
        print(f"{'='*60}")
        print(f" ANIMAL #{i}: {type(animal).__name__.upper()}")
        print("=" * 60)
        esperar_enter()
        
        print("\nDescripcion:")
        animal.describeme()
        esperar_enter()
        
        print("\nHablando:")
        hacer_sonido(animal)
        esperar_enter()
        
        print("\nMoviendose:")
        mostrar_movimiento(animal)
        esperar_enter()
    
    limpiar_consola()
    
    print("=" * 60)
    print(" METODOS ESPECIFICOS DE CADA CLASE")
    print("=" * 60)
    esperar_enter()
    
    print("\n--- GATO ---")
    print("\nHabilidades especiales del Gato:")
    print("\n1. Ronronear:")
    mi_gato.ronronear()
    esperar_enter()
    
    print("\n2. Afilar unas:")
    mi_gato.afilar_unas()
    esperar_enter()
    
    limpiar_consola()
    print("=" * 60)
    print(" METODOS ESPECIFICOS DE CADA CLASE")
    print("=" * 60)
    print("\n--- PEZ ---")
    print("\nHabilidades especiales del Pez:")
    print("\n1. Nadar rapido:")
    mi_pez.nadar_rapido()
    esperar_enter()
    
    print("\n2. Hacer burbujas:")
    mi_pez.hacer_burbujas()
    esperar_enter()
    
    limpiar_consola()
    print("=" * 60)
    print(" METODOS ESPECIFICOS DE CADA CLASE")
    print("=" * 60)
    print("\n--- MAPACHE ---")
    print("\nHabilidades especiales del Mapache:")
    print("\n1. Lavar comida:")
    mi_mapache.lavar_comida()
    esperar_enter()
    
    print("\n2. Buscar en la basura:")
    mi_mapache.buscar_basura()
    esperar_enter()
    
    limpiar_consola()
    
    print("=" * 60)
    print(" DEMOSTRACIÓN DE HERENCIA")
    print("=" * 60)
    esperar_enter()
    
    print("\nJerarquia de clases:")
    print(f"\nClase padre de Gato: {Gato.__bases__}")
    esperar_enter()
    
    print(f"\nSubclases de Animal: {Animal.__subclasses__()}")
    esperar_enter()
    
    limpiar_consola()
    print("\n" + "=" * 60)
    print(" FIN")
    print("=" * 60)
    print("\nChao ")
    esperar_enter()


if __name__ == "__main__":

    main()
