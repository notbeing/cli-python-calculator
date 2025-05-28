"""
Файл io.py содержит в себе различные операции с получением/выводом пользовательских данных.
"""

from __future__ import annotations

import os
from typing import Callable

from .constants import STOP_WORDS

__all__ = [
    "read_float",
    "read_int",
    "clear_screen",
    "ask_continue",
    "STOP_WORDS",
]


def clear_screen() -> None:
    """Очищает вывод консоли."""
    os.system("cls")


def _safe_input(prompt: str) -> str:
    """Возвращает строку, обрезав пробелы слева/справа."""
    return input(prompt).strip()


def _read_number(prompt: str, caster: Callable[[str]]):
    """Безопасное чтение числа."""
    while True:
        raw = _safe_input(prompt)

        if raw.lower() in STOP_WORDS:
            raise KeyboardInterrupt

        try:
            return caster(raw.replace(",", "."))
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз.")


def read_float(prompt: str = "Введите число: ") -> float:
    """Безопасное чтение float-числа."""
    return _read_number(prompt, float)


def read_int(prompt: str = "Введите целое число: ") -> int:
    """Безопасное чтение int-числа."""
    return _read_number(prompt, int)


def ask_continue() -> bool:
    """Неизменяемая функция, запрашивающая у пользователя дальнейшие действия."""
    answer = _safe_input("Продолжить? (д/н): ").lower()
    return answer in {"д", "y", "yes", "да"}
