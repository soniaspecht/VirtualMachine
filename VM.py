import os
import platform

# Clase básica para manejar las operaciones de las pilas. 
class Pila:

    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la pila.
        self.items = []  # Lista de elementos de la pila.
        self.tipos_insertados = {}  # Diccionario para evitar duplicados por tipo. 
        

    # AÑADIR ELEMENTOS A LA PILA (Operación 1). 
    def push(self, item, tipo_item):
        # If para verificar si la pila ya tiene un tipo asignado.
        if tipo_item in self.tipos_insertados:
            print(f"No se puede agregar '{item}'. Ya hay un elemento del tipo '{tipo_item}' en la pila '{self.nombre}'.")
        else:
            self.items.append(item)  # Se añade el elemento a la pila.
            self.tipos_insertados[tipo_item] = item  # Se almacena el tipo del nuevo elemento. 

    # ELIMINAR ÚLTIMO ELEMENTO DE LA PILA (Operación 2). 
    def pop(self):
        if not self.is_empty():
            item = self.items.pop()  # Se remueve el último elemento. 
            tipo_item = obtener_tipo(item)  # Se obtiene el tipo del elemento eliminado.
            self.tipos_insertados.pop(tipo_item, None)  # Se remueve el tipo del diccionario. 
            print(f"Removiendo el item {item} de la modelo...")
            return item
        print(f"La pila de {self.nombre} está vacía.")
        return None
    
    # PREGUNTAR SI ESTÁ VACÍA LA PILA (Operación 3). 
    def is_empty(self):
        return len(self.items) == 0  # Devuelve True si la pila está vacía.

    # MOSTRAR ÚLTIMO ELEMENTO (Operación 4). 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Muestra el último elemento sin removerlo.
        print(f"La pila de {self.nombre} está vacía.")
        return None
    
    # MOSTRAR CANTIDAD DE ELEMENTOS EN LA PILA (Operación 5). 
    def size(self):
        return len(self.items)

    # SABER SI UN ELEMENTO ESPECÍFICO SE ENCUENTRA EN LA PILA (Operación 6). 
    def contains(self, item):
        if item in self.items:
            print(f"La caracteristica {item} si pertenece a la modelo.")
            return True
        else: 
            print(f"La caracteristica {item} no pertenece a la modelo.")
            return False


# Función para OBTENER EL TIPO DE UN ELEMENTO (modelo, peinado, alas o zapatos).
def obtener_tipo(elemento):

    if elemento in ["KateMoss", "AdrianaLima", "GigiHadid", "BellaHadid", "BarbaraPalvin"]:
        return "modelo"
    elif elemento in ["ColetaAlta", "OndasSueltas", "PeloLiso", "Recogido"]:
        return "peinado"
    elif elemento in ["AlasBlancas", "AlasRosas", "AlasMulticolor", "AlasRojas", "AlasNegras"]:
        return "alas"
    elif elemento in ["TaconesPlumas", "TaconesBrillo", "Sandalias"]:
        return "zapatos"


# Clase principal que GESTIONA LAS PILAS Y LOS OUTFITS. Es decir, la Máquina Virtual. 
class StackVM():
    
    def __init__(self):

        # Inicializar pilas específicas.
        self.vestir = Pila("vestir")  # Pila para construir el outfit de la modelo.

        # Listas de elementos permitidos para cada categoría. 
        self.modelos_permitidos = ["KateMoss", "AdrianaLima", "GigiHadid", "BellaHadid", "BarbaraPalvin"]
        self.peinados_permitidos = ["ColetaAlta", "OndasSueltas", "PeloLiso", "Recogido"]
        self.alas_permitidos = ["AlasBlancas", "AlasRosas", "AlasMulticolor", "AlasRojas", "AlasNegras"]
        self.zapatos_permitidos = ["TaconesPlumas", "TaconesBrillo", "Sandalias"]

        # Memoria inmodificable de outfits predefinidos por modelo.
        self.outfits_memoria = [
            ["KateMoss", "OndasSueltas", "AlasNegras", "Sandalias"],
            ["AdrianaLima", "ColetaAlta", "AlasMulticolor", "TaconesPlumas"],
            ["GigiHadid", "PeloLiso", "AlasRosas", "TaconesBrillo"]
        ]

        # Videos asociados a cada modelo. 
        self.videos_modelos = {
            "KateMoss": "/Users/soniaspechtdelatorre/Desktop/Uni/3_4/Leng_paradigmas/interprete/final4/katemoss.mp4",
            "AdrianaLima": "/Users/soniaspechtdelatorre/Desktop/Uni/3_4/Leng_paradigmas/interprete/final4/adrianlima.mp4",
            "GigiHadid": "/Users/soniaspechtdelatorre/Desktop/Uni/3_4/Leng_paradigmas/interprete/final4/gigihadid.mp4"
        }

    # Función para INTERPRETAR COMANDOS DE LA MV y ejecutarlos.
    def interpretar_comando(self, comando):

        partes = comando.split()  # Divide el comando en partes.

        # Comandos PUSH para agregar elementos a la pila "vestir" (push). 
        if partes[0] == "PUSH_MODELO": # Introducir modelo. 
            if partes[1] in self.modelos_permitidos:
                tipo = obtener_tipo(partes[1])
                self.vestir.push(partes[1], tipo)
            else: 
                print("Esta modelo no esta dentro de las opciones.")
            
        elif partes[0] == "PUSH_PEINADO": # Introducir peinado. 
            if partes[1] in self.peinados_permitidos:
                tipo = obtener_tipo(partes[1])
                self.vestir.push(partes[1], tipo)
            else: 
                print("Este peinado no esta dentro de las opciones.")

        elif partes[0] == "PUSH_ALAS": # Introducir color de alas. 
            if partes[1] in self.alas_permitidos:
                tipo = obtener_tipo(partes[1])
                self.vestir.push(partes[1], tipo)
            else: 
                print("Este color de alas no esta dentro de las opciones.")

        elif partes[0] == "PUSH_ZAPATOS": # Introducir tipo de zapatos. 
            if partes[1] in self.zapatos_permitidos:
                tipo = obtener_tipo(partes[1])
                self.vestir.push(partes[1], tipo)
            else: 
                print("Estos zapatos no esta dentro de las opciones.")
        
        # Verifica si la pila "vestir" está vacía (is_empty).
        elif partes[0] == "EMPTY":
            if (self.vestir.is_empty() == True):
                print("No has creado un outfit para la modelo.")
            else:
                print("Ya has creado un outfit para la modelo.\n")

        # Remover el último elemento agregado (pop).
        elif partes[0] == "POP":
            self.vestir.pop()
            if not self.vestir.is_empty():
                print("La modelo decide no usar el último accesorio.")
            
        # Mostrar el outfit actual. 
        elif partes[0] == "DESFILAR":
            self.completo()

        # Cambiar el último par de alas por otro.
        elif partes[0] == "CAMBIAR_ALAS":
            self.vestir.pop()  # Remueve las alas actuales.
            tipo_alas = obtener_tipo(partes[1])
            self.vestir.push(partes[1], tipo_alas)  # Añade las nuevas alas.
            print(f"La modelo decide cambiar el color de sus alas por: {partes[1]}.")

        # Mostrar el último elemento en la pila sin removerlo (peek). 
        elif partes[0] == "PEEK":
            tope = self.vestir.peek()
            if tope:
                print(f"La última elección de la modelo es: {tope}.")

        # Se compara el outfit actual con los predefinidos. 
        elif partes[0] == "COMPARE":
            self.comparar_outfit()

        # Obtener el número de items que posee la modelo (size). 
        elif partes[0] == "SIZE":
             print(f"La modelo tiene {self.vestir.size()} accesorios.")
        
        elif partes[0] == "CONTAINS":
            self.vestir.contains(partes[1])
        
        else: 
            print("Comando no reconocido.") 


    # Función para VERIFICAR SI EL OUTFIT ESTÁ COMPLETO. 
    def completo(self):

        print("La modelo muestra su outfit actual: ")
        
        # Conjunto esperado de tipos
        elementos_esperados = {"modelo", "peinado", "alas", "zapatos"}
        
        # Diccionario para almacenar los elementos actuales clasificados por tipo.
        elementos_actuales = {
            "modelo": None,
            "peinado": None,
            "alas": None,
            "zapatos": None
        }
        
        # Clasificar los elementos en la pila según su tipo.
        for item in self.vestir.items:
            tipo_item = obtener_tipo(item)  # Obtener el tipo del elemento.
            if tipo_item in elementos_esperados:
                elementos_actuales[tipo_item] = item  # Asignar el elemento a su tipo correspondiente.
        
        # Identificar elementos faltantes.
        elementos_faltantes = [tipo for tipo, valor in elementos_actuales.items() if valor is None]

        # Verificar si el outfit está completo (es decir, si no hay elementos faltantes).
        if not elementos_faltantes:
            modelo = elementos_actuales["modelo"]
            peinado = elementos_actuales["peinado"]
            alas = elementos_actuales["alas"]
            zapatos = elementos_actuales["zapatos"]
            print(f"MODELO: '{modelo}'\nPEINADO: '{peinado}'\nCOLOR DE ALAS: '{alas}'\nZAPATOS: '{zapatos}'")
            print("El outfit está completo. ¡Lista para desfilar!")
        else:
            print("El outfit no está completo. Faltan los siguientes elementos:")
            for elemento in elementos_faltantes:
                print(f"- {elemento}")


    # Función para COMPARAR EL OUTFIT CON LOS OUTFITS PREDEFINIDOS. 
    def comparar_outfit(self):

        if len(self.vestir.items) == 0:
            print("\nNo has seleccionado ningún outfit para comparar.")
            return False

        # Clasificar los elementos de la pila según su tipo.
        elementos_clasificados = {"modelo": None, "peinado": None, "alas": None, "zapatos": None}
        for item in self.vestir.items:
            tipo_item = obtener_tipo(item)
            elementos_clasificados[tipo_item] = item
        
        outfit_actual = [
            elementos_clasificados["modelo"],
            elementos_clasificados["peinado"],
            elementos_clasificados["alas"],
            elementos_clasificados["zapatos"]
        ]

        # Verificar si el outfit coincide con uno de la memoria.
        for outfit in self.outfits_memoria:
            
            if outfit_actual == outfit:
                modelo = outfit_actual[0]
                print(f"\n✨¡Outfit correcto para {modelo}!✨ Redirigiendo al video...")

                # Mostrar el video de la modelo que coincida. 
                if os.path.exists(self.videos_modelos[modelo]):
                    print("El archivo existe y se puede acceder.")
                    if platform.system() == "Darwin":  # macOS
                        os.system(f"open '{self.videos_modelos[modelo]}'")
                else:
                    print("El archivo no se encuentra.")
                return True

        print("\nHas creado un outfit original. ¡Qué buen gusto! Te robas todas las miradas en la pasarela 🎀")
        return False

    # Función para LEER y EJECUTAR un archivo .fais (creado por nosotras). 
    def execute(self, filename):
        
        if not filename.endswith(".fais"):
            print("Error: File must have a .fais extension.")
            sys.exit(1)

        try:

            with open(filename, 'r') as f:
                comandos = f.readlines()  # Leer los comandos del archivo.
            for comando in comandos:
                comando = comando.strip()  # Quitar espacios en blanco.

                # Se añade esto para poder comentar en el archivo .fais. 
                if comando.startswith("#") or comando.startswith("//") or not comando:
                    continue  # Ignorar comentarios o líneas vacías. 

                if comando:
                    print(f"\nEjecutando comando: {comando}")
                    self.interpretar_comando(comando)
                    
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado.")
            
# PROGRAMA PRINCIPAL. 
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python VM.py <filename.extension>")
        sys.exit(1)

    filename = sys.argv[1]
    # Ejecutar la VM con el archivo dado. 
    StackVM().execute(filename)
