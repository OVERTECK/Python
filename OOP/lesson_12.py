# Магический метод __call__. Функторы.

from typing import Any


class Counter:
    def __init__(self) -> None:
        self.count = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1

        return self.count
    
my_counter = Counter()

my_counter()
my_counter()
my_counter()

print(my_counter())