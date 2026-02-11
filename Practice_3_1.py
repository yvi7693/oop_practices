# task2

class Smartphone:
    brand: str
    model: str
    operating_system: str
    memory: int
    hard_memory: float
    ram: int
    battery_level: int
    is_work: bool


    def __init__(self, brand: str, model: str, operating_system: str, memory: int, ram: int, battery_level: int, is_work: bool, hard_memory: float):

        self.__brand = brand
        self.__model = model
        self.__operating_system = operating_system
        self.__memory = memory
        self.__hard_memory = hard_memory
        self.__ram = ram
        self.__battery_level = battery_level
        self.__is_work = is_work


    def __str__(self):
        return (f"Марка {self.__brand} "
                f"\nМодель: {self.__model}"
                f"\nОперационная система: {self.__operating_system}"
                f"\nВстроенная память: {self.__memory}"
                f"\nСвободная память: {self.__hard_memory}"
                f"\nОперативная память: {self.__ram}"
                f"\nТекущий заряд: {self.__battery_level}"
                f"\nСостояние работы: {self.__is_work}")


    def try_turn_on(self) -> bool:
        if self.__battery_level > 0:
            return True

        return False

    def turn_on(self) -> None:
        if self.try_turn_on():
            self.__is_work = True

        return None

    def turn_off(self) -> None:
        self.is_work = False

    def system_deployment(self, new_operating_system: str) -> None:
        self.__operating_system = new_operating_system

    def try_installation_app(self, required_storage: float) -> bool:
        if required_storage < 0:
            raise ValueError

        if self.__hard_memory < required_storage:
            return False

        self.__hard_memory -= required_storage
        return True

    def delete_app(self, required_storage) -> None:
        if required_storage < 0 or required_storage > self.__memory:
            raise ValueError

        self.__hard_memory += required_storage
        return None

    def charging(self, growth_charge) -> None:
        if growth_charge > 100 or (growth_charge + self.__battery_level) > 100 or growth_charge < 0:
            raise ValueError

        self.__battery_level += growth_charge

    def discharge(self, decrease_charge) -> None:
        if decrease_charge > 100 or decrease_charge < 0 or (self.__battery_level - decrease_charge) < 0:
            raise ValueError

        self.__battery_level -= decrease_charge


    def get_is_work(self) -> bool:
        return self.__is_work

    def get_charge(self) -> int:
        return self.__battery_level

    def get_ram(self) -> int:
        return self.__ram

    def get_free_storage(self) -> float:
        return self.__hard_memory

    def get_storage(self) -> int:
        return self.__memory

    def get_operating_system(self) -> str:
        return self.__operating_system

    def get_model(self) -> str:
        return self.__model

    def get_brand(self) -> str:
        return self.__brand


    def set_brand(self, new_brand: str) -> None:
        self.__brand = new_brand

    def set_model(self, new_model: str) -> None:
        self.__model = new_model

    def set_operating_system(self, new_system: str) -> None:
        self.__perating_system = new_system

    def set_storage(self, new_memory: int) -> None:
        self.__memory = new_memory

    def set_ram(self, new_ram: int) -> None:
        self.__ram = new_ram

    def set_charge(self, new_battery_level: int) -> None:
        self.__battery_level = new_battery_level

    def set_is_work(self, new_is_work: bool) -> None:
        self.__is_work = new_is_work


iphone = Smartphone("apple", "13", "IOS", 128, 16, 90, False, 30)

iphone.turn_on()
iphone.system_deployment("Android")
iphone.try_installation_app(4)
iphone.delete_app(4)
iphone.charging(6)
iphone.discharge(3)
print(iphone)




# task3

class Ingredient:
    name: str

    def __init__(self, name: str):
        self.__name = name

    def __str__(self):
        return self.name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_name(self) -> str:
        return self.__name


class Potion:

    name: str
    ingredients: list[Ingredient]
    level_difficult: int
    effect: str
    is_readiness: bool


    def __init__(self, name: str, ingredients: list[Ingredient], level_difficult: int, effect: str, is_readiness: bool):
        self.__name = name
        self.__ingredients = ingredients
        self.__level_difficult = level_difficult
        self.__effect = effect
        self.__is_readiness = is_readiness

    def __str__(self):
        return f"Name: {self.__name} \ningredients: {self.get_ingredients()} \nlevel difficult: {self.__level_difficult} \neffect: {self.__effect} \nis readiness: {self.__is_readiness}"

    def add_ingredient(self, new_ingredient: Ingredient) -> None:
        self.__ingredients.append(new_ingredient)

    def delete_ingredient(self, delete_ingredient: Ingredient):

        for i in range(len(self.__ingredients)):
            if self.__ingredients[i] == delete_ingredient:
                delete_index = i

        self.__ingredients.pop(delete_index)

    def make_potion(self) -> str:
        return "Зелье приготовлено"


    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def set_level_difficult(self, new_level_difficult: int) -> None:
        self.level_difficult = new_level_difficult

    def set_effect(self, new_effect) -> None:
        self.effect = new_effect

    def set_is_readiness(self, new_is_readiness):
        self.is_readiness = new_is_readiness


    def get_name(self) -> str:
        return self.name

    def get_ingredients(self) -> list[str]:

        return [ingredient.get_name() for ingredient in self.__ingredients]

    def get_level_difficult(self) -> int:
        return self.level_difficult

    def get_effect(self) -> str:
        return self.effect

    def get_is_readiness(self) -> bool:
        return self.is_readiness


bubotuber_pus = Ingredient("Слизь бубонтюбера")
boomslang_skin = Ingredient("Кожа бумсланга")

polyjuice = Potion("Оборотное зелье", [bubotuber_pus, boomslang_skin], 9, "Активность", False)

print(polyjuice)









