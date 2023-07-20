import unittest
from parts_layer import Cpu
from db_layer import CPU


class TestCpu(unittest.TestCase):
    def test_get_price(self) -> None:
        cpu_testing = Cpu(CPU)
        self.assertEqual(cpu_testing.get_price("Ryzen 5 5600X"), 162.66)


if __name__ == "__main__":
    unittest.main()
