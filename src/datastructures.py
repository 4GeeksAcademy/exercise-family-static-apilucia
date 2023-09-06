
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    #Inicializa la clase con el apellido proporcionado que queda fijo
    def __init__(self, last_name):
        self.last_name = last_name

        # lista inicial de miembros ficticios, la lista que guardada en self._members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "age": "33",
            "lucky_numbers": [7, 13, 22]
            },
            {
            "id": self._generateId(),
            "first_name": "Jane",
            "age": "35",
            "lucky_numbers": [10, 14, 3]
            },
            {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "age": "5",
            "lucky_numbers": [1]
            }
        ]
            
 

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
     
        self._members.append(member)#self._member es la lista append agrega member(o sea el miembro que quiero agregar) a la lista

        return None #le pido que no retorne nada
        pass

    def delete_member(self, id):
        for member in self._members:#para un miembro en la lista 
            if member ["id"] == id:# si el id del miembro que ingreso coincide con el id de alguno de los de la lista 
                self._members.remove(member)#elimino de la lista el miembro
                return self._members#devuleve la nueva lista sin el miembro
        
    
    def get_member(self, id):
        for member in self._members:#para el miembro en la lista
            if member ["id"] == id:#si coincide la id que pido con uno de la lista
                return member# me retorna ese miembro



    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
