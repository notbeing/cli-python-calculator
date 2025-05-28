"""
Файл arithmetics.py содержит базовые арифметические операции.
"""

from typing import Union

Number = Union[int, float]

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "floor_divide",
    "mod",
    "power",
]


def add(a: Number, b: Number) -> Number:
    """Сложение a и b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Вычитание b из a."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Умножение a на b."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Деление a на b."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо.")
    return a / b


def floor_divide(a: Number, b: Number) -> Number:
    """Целочисленное деление a на b."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо.")
    return a // b


def mod(a: Number, b: Number) -> Number:
    """Остаток от деления a на b."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо.")
    return a % b


def power(a: Number, b: Number) -> Number:
    """Возведение a в степень b."""
    return a**b
