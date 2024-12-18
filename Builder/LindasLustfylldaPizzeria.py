## BAD CODE

class Pizza:
    def __init__(
            self, 
            size:str, 
            crust:str, 
            toppings:list[str], 
            sauce:str
        ) -> None:
        

        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.sauce = sauce

    def __str__(self) -> str:
        return (f"Pizza -> Storlek '{self.size}', deg/kant '{self.crust}', "
                f"sås '{self.sauce}' och pålägg: {', '.join(self.toppings)}")
    
pizzas = {
    1: "Margarita",
    2: "Vesuvio",
    3: "Funghi",
    4: "Calzone",
    5: "Al Tono",
    6: "Hawaii",
    7: "Blanco"
}

sizes = {
    "small"
    "medium"
    "large"
    "family"
}

pizzas_toppings = {
    "Margarita": ["ost"],
    "Vesuvio": ["ost", "skinka"],
    "Funghi": ["ost", "champinjoner"],
    "Calzone": ["ost", "skinka"],
    "Al Tono": ["ost", "lök", "tonfisk"],
    "Hawaii": ["ost", "skinka", "annanas"]
    }

def print_pizza_menu() -> None:
    for number, pizza in pizzas.items():
        print(f"{number}: {pizza}")

def print_pizza_sizes() -> None:
    print("Possible sizes:")
    for size in sizes:
        print(f"\t{size}")


if __name__ == "__main__":
    print("Välkommna till Lindas Lustfyllda Pizzeria!")
    while True:
        print("Var vänlig och gör en beställning eller stick härifrån!")
        print("1. Beställ pizza🍕")
        print("0. Spring här ifrån")
        
        menu_choice = input("Gör ett val: ")

        if menu_choice == "0": break

        if menu_choice == "1":
            order = []
            while True:
                print_pizza_menu()                
                select_pizza_type = input("Ange en pizza eller q för att avsluta: ")

                if (select_pizza_type.isdigit() 
                    and (pizza_number:=int(select_pizza_type)) in pizzas):

                    while True:
                        print_pizza_sizes()
                        selected_size = input("Ange storlek: ")
                        if selected_size in sizes: break

                        print("Ogiltligt val, välj storlek!")
                            
                    if pizza_number == 4:
                        pizza_type = "inbakad"
                    else:
                        while True:
                            style = input("Välj pizzastil: tunn eller pan? ")
                            if style in ["tun", "pan"]: break
                            print("Du måste välja stil!")
                        pizza_type = style

                    pizza = Pizza(selected_size, pizza_type, pizzas_toppings[pizzas[pizza_number]], "Tomatsås")
                    order.append(pizza)