class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            if pet not in self._pets:
                self._pets.append(pet)
        else:
            raise Exception("Pet must be an instance of Pet")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda p: p.name)
