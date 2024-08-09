import items
import skills

class Player:
    def __init__(self):
        # Declaraciones 
        self.health = 100
        self.sanity = 100
        self.inventory = list()
        self.abilities = list()

        # Asignaciones
        self.set_basic_inventory()
        self.set_basic_abilities()
    
    # Seteamos los objetos basicos del jugador
    def set_basic_inventory(self):
        for key in items.item_creation_map:
            if key <= 3:
                self.inventory.append(items.create_item(key))
    
    # Seteamos las habilidades del jugador
    def set_basic_abilities(self):
        for key in skills.skills_cration_map:
            if key <= 52:
                self.abilities.append(skills.create_skill(key))
        
    # Acciones del Player
    # Usar Objeto
    def use_item(self, item_name):
        for i in self.inventory:
            if i.name == item_name:
                i.use()

    # Usar habilidad
    def use_skill(self, item_skill):
        for i in self.abilities:
            if i.name == item_skill:
                i.use_skill()

    # Ver Inventario
    def show_inventario(self):
        print("Inventario del Jugador:")
        for i in self.inventory:
            print(f"{i.name} - Poder:{i.power} - Cantidad:{i.quantity}")

    # Ver habilidades
    def show_abilities(self):
        print("Habilidades del Jugador:")
        for i in self.abilities:
            print(f"{i.name} - Poder:{i.power} - Usos:{i.uses}")

# Crear una instancia de Player
prueba = Player()
prueba.use_item("Poción de Salud")
prueba.use_skill("Puñetazo")
# Mostrar el inventario
prueba.show_inventario()
prueba.show_abilities()
