## BAD CODE
from enum import Enum


class Pizza:
    def __init__(self) -> None:
        self.size = None
        self.crust = None
        self.toppings = []
        self.sauce = None

    def __str__(self) -> str:
        return (f"Pizza -> Storlek '{self.size}', deg/kant '{self.crust}', "
                f"sås '{self.sauce}' och pålägg: {', '.join(self.toppings)}")
    
class PizzaBuilder:

    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size):
        self._pizza.size = size
        return self

    def set_crust(self, crust):
        self._pizza.crust = crust
        return self

    def set_sauce(self, sauce):
        self._pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self._pizza.toppings.append(topping)
        return self

    def build(self):
        return self._pizza
    
class PizzaBoss:
    """The Director"""

    def __init__(self, builder):
        self._builder:PizzaBuilder = builder


    def make_margherita(self) -> Pizza:
        return (self._regular_pizza_base()
                .add_topping("ost")
                .build())
    
    def make_vesuvio(self) -> Pizza:
        return (self._regular_pizza_base()
                .add_topping("ost")
                .add_topping("skinka")
                .build())
           
    def make_funghi(self) -> Pizza:
        return (self._regular_pizza_base()
                .add_topping("ost")
                .add_topping("champinjoner")
                .build())

    def make_calzone(self) -> Pizza:
        return (self._builder
                .set_size("medium")
                .set_crust("inbakad")
                .set_sauce("tomatsås")
                .add_topping("ost")
                .add_topping("skinka")
                .build())           

    def make_al_tono(self) -> Pizza:
        return (self._regular_pizza_base()
                .add_topping("ost")
                .add_topping("lök")
                .add_topping("tonfisk")
                .build())
    

    def make_al_tono(self) -> Pizza:
        return (self._regular_pizza_base()
                .add_topping("ost")
                .add_topping("skinka")
                .add_topping("annanas")
                .build())
    
    def make_blanco(self) -> Pizza:
        return (self._builder
                .set_size("medium")
                .set_crust("tunn")
                .set_sauce("ingen")
                .add_topping("ost")
                .add_topping("skinka")
                .add_topping("annanas")
                .build())
    
    def _regular_pizza_base(self) -> PizzaBuilder:
        return(self._builder
                .set_size("medium")
                .set_crust("tunn")
                .set_sauce("tomatsås"))

    
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
                builder = PizzaBuilder()
                pizza_boss = PizzaBoss(builder)
                
                print_pizza_menu()                
                select_pizza_type = input("Ange en pizza eller q för att avsluta: ")

                if select_pizza_type == "q": break

                if select_pizza_type.isdigit():
                    pizza_number=int(select_pizza_type)

                    match pizza_number:
                        case 1: new_pizza = pizza_boss.make_margherita()
                        case 2: new_pizza = pizza_boss.make_vesuvio()
                        case 3: new_pizza = pizza_boss.make_funghi()
                        case 4: new_pizza = pizza_boss.make_calzone()
                        case 5: new_pizza = pizza_boss.make_al_tono()
                        case 6: new_pizza = pizza_boss.make_blanco()
                        case _: new_pizza = None

                    if new_pizza: 
                        order.append(new_pizza)
                    else:
                        print("Ogiltligt pizzaval!")

            print("Du har beställt följande pizzor:")
            for pizza in order:
                print(pizza)


                    