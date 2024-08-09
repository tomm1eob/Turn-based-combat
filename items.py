# Definición de la clase Item
class Item:

    # Constructor de Item
    def __init__(self, item_id, quantity, name, item_type, effect, power):
        self.item_id = item_id
        self.quantity = quantity
        self.name = name
        self.item_type = item_type
        self.effect = effect
        self.power = power
    
    # Función añadir cantidad
    def add_quantity(self, amount):
        self.quantity += amount
    
    # Función usar 
    def use(self):
        if self.quantity > 0:
            self.quantity -= 1
            print(f"Usaste {self.name}. Quedan {self.quantity} en stock.")
        else:
            print(f"No hay más {self.name} en el inventario.")

# Metodos para crear instancias de un objeto 
def create_little_potion_health():
    return Item(1, 1, "Poción de Salud", "consumable", "increase_health", 15)

def create_little_potion_sanity():
    return Item(2, 1, "Poción de Cordura", "consumable", "increase_sanity", 15)

def create_little_potion_damage():
    return Item(3, 1, "Poción de Fuerza", "consumable", "increase_damage", 10)

# Mapeamos estos métodos a un diccionario para su uso segun su id:
item_creation_map = {
    1: create_little_potion_health,
    2: create_little_potion_sanity,
    3: create_little_potion_damage
}

# Creador de items
def create_item(item_id):
    return item_creation_map.get(item_id, lambda: None)() # Si no coincide llama al metodo creador, sino "None"

