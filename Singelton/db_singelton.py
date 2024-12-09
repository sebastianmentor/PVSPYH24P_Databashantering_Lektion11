class DatabaseConnection:
    _instance = None  # Klassvariabel för att lagra den enda instansen

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # Skapa instansen om den inte finns
        return cls._instance

    def __init__(self, database):
        if not hasattr(self, 'initialized'):  # Kontrollera om instansen redan initierats
            self.database = database
            self.initialized = True

    def connect(self) -> bool:
        try: 
            self.database.connect()
        except ValueError:
            ...
            
