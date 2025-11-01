import re
from typing import Callable, Generator


# Завдання 1

def caching_fibonacci() -> Callable:
    cache = {}

    def fibonacci(n) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


fib = caching_fibonacci()
# print(fib(10))
# print(fib(15))

# Завдання 2


def generator_numbers(text: str) -> Generator[float]:
    numbers = re.findall(r"\s\b\d+(?:\.\d+)?\b\s", text)
    for item in numbers:
        yield float(item)


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: " \
    "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 " \
    "і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
