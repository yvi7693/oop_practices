from hw_4.task3.car import Car
from hw_4.task3.dealership import Dealership
from hw_4.task3.entities import Customer, Salesperson

bmw = Car("BMW", "M5", 10000, 2025, "в наличии")
fresh = Dealership([bmw])


ferrari = Car("Ferrari", "F40", 50000, 1996, "в наличии")
fresh.shipment(ferrari)

print(fresh)
print()

yaroslav = Customer("Yaroslav", 89696588194, "yvi_7693@icloud.com")
bob = Salesperson("bob", 5)

fresh.hire(bob)

bob.vend(ferrari)
fresh.vend(ferrari)
fresh.lead_generation(yaroslav)

print(fresh)


