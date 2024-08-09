# Definición de la clase Skills
class Skills:

    # Creación del constructor
    def __init__(self, skill_id, name, uses_max, uses, skill_type, category, effect, power):
        self.skill_id = skill_id
        self.name = name
        self.uses_max = uses_max
        self.uses = uses_max
        self.skill_type = skill_type
        self.category = category
        self.effect = effect
        self.power = power
    
    # Función uso
    def use_skill(self):
        if self.uses > 0:
            self.uses -= 1
    
    # Función añadir
    def add_uses(self, mount):
        if self.uses_max >= self.uses:
            if (mount + self.uses) > self.uses_max:
                self.uses = 30
            else:
                uses = mount + self.uses

# Funciones de las Skills
def create_physical_punch():
    return Skills(51, "Puñetazo", 20, 20, "atack", "fisic", "physical_punch", 15)
def create_clumsy_curse():
    return Skills(52, "Maldición Torpe", 10, 10, "atack", "curse", "clumsy_Curse", 18)

# Mapeos de id_skills
skills_cration_map = {
        51: create_physical_punch,
        52: create_clumsy_curse
}

# Funcion creadora de Skills
def create_skill(id_skill):
    return skills_cration_map.get(id_skill, lambda: None)()
