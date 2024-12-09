

class Bok:
    def __init__(self, id, titel, författare):
        self.id = id 
        self.titel = titel
        self.författare = författare

    def __str__(self):
        return f"ID: {self.id}, Titel:{self.titel}, Författare:{self.författare}"

class Bokregister:
    _instans = None 
    _register = {}

    def __new__(cls):
        if not cls._instans:
            cls._instans = super().__new__(cls)  # Skapa instansen om den inte finns
        return cls._instans

    def lägg_till_bok(self, bok:Bok) -> bool:
        if bok.id in self._register: return False

        self._register[bok.id] = bok
        return True

    def hämta_bok(self, bok_id:int) -> Bok|None:
        return self._register.get(bok_id, None)
    
    def print_register(self) -> None:
        for bok in self._register.values():
            print(bok)
    
    

class Bokhandel:
    def __init__(self):
        self._bokregister = Bokregister()


    def köp_in_bok(self, titel, författare, id):
        bok = Bok(id, titel, författare)
        gick_bra = self._bokregister.lägg_till_bok(bok)

        if not gick_bra: raise ValueError("Gick inte att köpa in bok!!")

    def visa_böcker(self):
        self._bokregister.print_register()

if __name__ == "__main__":
    bokhandel_1 = Bokhandel()
    bokhandel_2 = Bokhandel()

    bokhandel_1.köp_in_bok("Harry Potter", "J.K.Rowling", 1)
    bokhandel_2.visa_böcker()


