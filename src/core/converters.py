"""
Файл converters.py содержит в себе конвертер единиц измерения и систем счисления.
"""

from helpers import constants

__all__ = [
    "meter_to_feet",
    "feet_to_meter",
    "kg_to_pounds",
    "pounds_to_kg",
    "base_to_decimal",
]


def meter_to_feet(value: float) -> float:
    """Метры -> футы."""
    return value * constants.METER_TO_FEET


def feet_to_meter(value: float) -> float:
    """Футы -> метры."""
    return value * constants.FEET_TO_METER


def kg_to_pounds(value: float) -> float:
    """Килограммы -> фунты."""
    return value * constants.KG_TO_POUND


def pounds_to_kg(value: float) -> float:
    """Фунты -> килограммы."""
    return value * constants.POUND_TO_KG


def base_to_decimal(value: str, base: int) -> int:
    """Перевод числа из системы с основанием в десятичную.

    Поддерживаются основания 2, 8 и 16.
    """
    if base not in constants.SUPPORTED_BASES:
        raise ValueError("Допустимы только системы 2, 8 или 16.")

    try:
        return int(value, base)
    except ValueError as exc:
        raise ValueError(
            f"'{value}' не является корректным числом в системе {base}."
        ) from exc
