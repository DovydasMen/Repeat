# pylint:disable-all
from abc import ABC, abstractmethod
from db_layer import CPU
from typing import Dict, Any
from logger import console_logger, file_logger
from error_handler import ItemsNotFoundError, PriceNotChangedError


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
        try:
            for i in self.item_dict.keys():
                if i == None:
                    raise ItemsNotFoundError
                else:
                    console_logger.info(f" Here is {i}!")
        except ItemsNotFoundError:
            console_logger.info(
                "Our database have zero entries regarding this argument!"
            )
        except Exception as e:
            console_logger.info(f"We have faced unexpected troubles!")
            file_logger.info("We faced unexpected error: {e}")

    def get_name(self, product_name: str) -> str:
        name_to_return = ""
        try:
            for i in self.item_dict.keys():
                if i == product_name:
                    name_to_return = i
            return name_to_return
        except KeyError:
            console_logger.info(f"We don't have such item in our database!")
        except Exception as e:
            console_logger.info(f"We have faced unexpected troubles!")
            file_logger.info("We faced unexpected error: {e}")

    def get_price(self, product_name: str) -> float:
        try:
            return self.item_dict[product_name]["price"]
        except KeyError:
            console_logger.info(f"We don't have such key argument in our database!")
        except Exception as e:
            console_logger.info(f"We have faced unexpected troubles!")
            file_logger.info("We faced unexpected error: {e}")

    def get_brand(self, product_name: str) -> str:
        try:
            return self.item_dict[product_name]["manufacturer"]
        except KeyError:
            console_logger.info(f"We don't have such key argument in our database!")
        except Exception as e:
            console_logger.info(f"We have faced unexpected troubles!")
            file_logger.info("We faced unexpected error: {e}")


class Cpu(Baseparts):
    def __init__(self, item_dict: Dict[str, Any]) -> None:
        super().__init__(item_dict)
        self.item_dict = item_dict
        file_logger.info(f"Our database looks like this: {self.item_dict}")

    def set_new_price(self, item_name: str, price: float) -> str:
        try:
            if self.get_name(item_name) == "":
                raise PriceNotChangedError
            else:
                self.item_dict[item_name]["price"] = price
                file_logger.info(f"We are changing {item_name} price to new {price}")
                console_logger.info("You have succesfully changed the price!")
                return price
        except PriceNotChangedError:
            console_logger.info(
                f"We haven't found any item, so the price wasn't changed!"
            )
        except KeyError:
            console_logger.info(f"We don't have such key argument in our database!")
        except Exception as e:
            console_logger.info(f"We have faced unexpected troubles!")
            file_logger.info("We faced unexpected error: {e}")


cpu_items = Cpu(CPU)

cpu_items.set_new_price("Core i7 - 13700K", 500.01)
