class Singleton:
    _instance = None  # Klassvariabel för att lagra den enda instansen

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # Skapa instansen om den inte finns
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Kontrollera om instansen redan initierats
            self.value = value
            self.initialized = True
            

# Test av singleton
singleton1 = Singleton("Första värdet")
print(singleton1.value)  # Output: Första värdet

del(singleton1.initialized)

singleton2 = Singleton("Andra värdet")
print(singleton2.value)  # Output: Första värdet (singleton instansen ändras inte)

# Kontrollera att båda instanserna är samma
print(singleton1 is singleton2)  # Output: True
