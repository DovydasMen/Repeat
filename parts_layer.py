from abc import ABC, abstractmethod
from db_layer import CPU
from typing import Dict, Any


class PcParts(ABC):
    @abstractmethod
    def get_name() -> str:
        pass

    @abstractmethod
    def get_price() -> float:
        pass

    @abstractmethod
    def get_brand() -> str:
        pass


class Cpu(PcParts):
    def __init__(self, cpu_list: Dict[str, Any]) -> None:
        self.cpu_list = cpu_list

    def get_name(self) -> str:
        return

    def get_price(self) -> float:
        pass

    def get_brand(self) -> str:
        pass

    def set_price(self) -> None:
        pass


my_cpu = Cpu(CPU)

print(my_cpu.cpu_list)
