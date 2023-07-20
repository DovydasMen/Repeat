from abc import ABC, abstractmethod
from db_layer import CPU
from typing import Dict, Any


class BluePrint(ABC):
    @abstractmethod
    def get_name() -> str:
        pass

    @abstractmethod
    def get_price() -> float:
        pass

    @abstractmethod
    def get_brand() -> str:
        pass


class Baseparts(BluePrint):
    def __init__(self, item_dict: Dict[str, Any]) -> None:
        self.item_dict = item_dict

    def show_all_products(self) -> None:
        for i in self.item_dict.keys():
            if i == None:
                pass
            else:
                print(i)

    def get_name(self, product_name: str) -> str:
        name_to_return = ""
        for i in self.item_dict.keys():
            if i == product_name:
                name_to_return = i
        return name_to_return

    def get_price(self, product_name: str) -> float:
        return self.item_dict[product_name]["price"]

    def get_brand(self, product_name: str) -> str:
        return self.item_dict[product_name]["manufacturer"]


class Cpu(Baseparts):
    def __init__(self, item_dict: Dict[str, Any]) -> None:
        super().__init__(item_dict)
        self.item_dict = item_dict

    def set_new_price(self, item_name: str, price: float) -> str:
        self.item_dict[item_name]["price"] = price
        return print("You have succesfully changed price!")


cpu_items = Cpu(CPU)

print(cpu_items.get_price("Core i7 - 13700K"))
cpu_items.set_new_price("Core i7 - 13700K", 150.1)
print(cpu_items.get_price("Core i7 - 13700K"))
