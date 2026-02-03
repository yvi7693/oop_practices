# task2

class Smartphone:
    brand: str
    model: str
    operating_system: str
    storage: int
    free_storage: float
    ram: int
    charge: int
    is_work: bool


    def __init__(self, brand: str, model: str, operating_system: str, storage: int, ram: int, charge: int, is_work: bool, free_storage: float):

        self.brand = brand
        self.model = model
        self.operating_system = operating_system
        self.storage = storage
        self.free_storage = free_storage
        self.ram = ram
        self.charge = charge
        self.is_work = is_work


    def __str__(self):
        return (f"Марка {self.brand} "
                f"\nМодель: {self.model}"
                f"\nОперационная система: {self.operating_system}"
                f"\nВстроенная память: {self.storage}"
                f"\nСвободная память: {self.free_storage}"
                f"\nОперативная память: {self.ram}"
                f"\nТекущий заряд: {self.charge}"
                f"\nСостояние работы: {self.is_work}")


    def turn_on(self) -> None:
        is_work = True

    def turn_off(self) -> None:
        is_work = False

    def replace_operating_system(self, new_operating_system: str) -> None:
        self.operating_system = new_operating_system

    def installation_app(self, required_storage) -> None | str:
        if required_storage < 0:
            raise ValueError

        if self.free_storage < required_storage:
            return "Очистите память"

        self.free_storage -= required_storage
        return None

    def delete_app(self, required_storage) -> None:
        if required_storage < 0 or required_storage > self.storage:
            raise ValueError

        self.free_storage += required_storage
        return None

    def charging(self, growth_charge) -> None:
        if growth_charge > 100 or (growth_charge + self.charge) > 100 or growth_charge < 0:
            raise ValueError

        self.charge += growth_charge

    def discharge(self, decrease_charge) -> None:
        if decrease_charge > 100 or decrease_charge < 0 or (self.charge - decrease_charge) < 0:
            raise ValueError

        self.charge -= decrease_charge


    def get_is_work(self) -> bool:
        return self.is_work

    def get_charge(self) -> int:
        return self.charge

    def get_ram(self) -> int:
        return self.ram

    def get_free_storage(self) -> float:
        return self.free_storage

    def get_storage(self) -> int:
        return self.storage

    def get_operating_system(self) -> str:
        return self.operating_system

    def get_model(self) -> str:
        return self.model

    def get_brand(self) -> str:
        return self.brand


    def set_operating_system(self, new_system: str) -> None:
        self.operating_system = new_system

    def set_storage(self, new_storage: int) -> None:
        self.storage = new_storage

    def set_ram(self, new_ram: int) -> None:
        self.ram = new_ram

    def set_charge(self, new_charge: int) -> None:
        self.charge = new_charge

    def set_is_work(self, new_is_work: bool) -> None:
        self.is_work = new_is_work



# task3

class Ingredient:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Potion:

    name: str
    ingredients: list[Ingredient]
    level_difficult: int
    effect: str
    is_readiness: bool


    def __init__(self, name: str, ingredients: list[Ingredient], level_difficult: int, effect: str, is_readiness: bool):
        self.name = name
        self.ingredients = ingredients
        self.level_difficult = level_difficult
        self.effect = effect
        self.is_readiness = is_readiness

    def __str__(self):
        return f"Name: {self.name} \ningredients: {self.get_ingredients()} \nlevel difficult: {self.level_difficult} \neffect: {self.effect} \nis readiness: {self.is_readiness}"

    def add_ingredient(self, new_ingredient: Ingredient) -> None:
        self.ingredients.append(new_ingredient)

    def delete_ingredient(self, delete_ingredient: Ingredient):
        global delete_index

        for i in range(len(self.ingredients)):
            if self.ingredients[i] == delete_ingredient:
                delete_index = i

        self.ingredients.pop(delete_index)

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

        return [ingredient.name for ingredient in self.ingredients]

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









