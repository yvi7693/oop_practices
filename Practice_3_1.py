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





