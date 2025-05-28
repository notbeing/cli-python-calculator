"""
Точка входа CLI-калкьулятора.

Отображает меню, запрашивает и обрабатывает пользовательский ввод.
"""

from __future__ import annotations

import sys
from typing import Dict

from core import arithmetics, converters, deposit, menu
from helpers.io import STOP_WORDS, ask_continue, clear_screen, read_float, read_int

_ARITHMETIC_OPERATIONS: Dict = {
    "+": arithmetics.add,
    "-": arithmetics.subtract,
    "*": arithmetics.multiply,
    "/": arithmetics.divide,
    "//": arithmetics.floor_divide,
    "%": arithmetics.mod,
    "**": arithmetics.power,
}


def _run_arithmetic() -> None:
    """Запрашивает у пользователя два числа и оператор, выводит результат."""
    while True:
        a = read_float("Первое число: ")
        b = read_float("Второе число: ")

        print("Доступные операции:")
        for op in _ARITHMETIC_OPERATIONS:
            print(f"  {op}")

        op = input("Оператор: ").strip()
        if op in STOP_WORDS:
            raise KeyboardInterrupt

        func = _ARITHMETIC_OPERATIONS.get(op)
        if func is None:
            print("Неизвестный оператор. Попробуйте снова.")
            continue

        try:
            result = func(a, b)
            print(f"Результат: {result}\n")
        except ZeroDivisionError as err:
            print(err)

        if not ask_continue():
            clear_screen()
            break


def _run_unit_converter() -> None:
    """Конвертация метров в футы и килограммов в фунты."""
    options = {
        1: ("Метры -> футы", converters.meter_to_feet),
        2: ("Футы -> метры", converters.feet_to_meter),
        3: ("Килограммы -> фунты", converters.kg_to_pounds),
        4: ("Фунты -> килограммы", converters.pounds_to_kg),
    }

    while True:
        print("Выберите направление конвертации:")
        for idx, (label, _) in options.items():
            print(f"  {idx}) {label}")
        idx = read_int("Номер: ")
        func_info = options.get(idx)
        if func_info is None:
            print("Неверный номер, попробуйте снова.")
            continue

        value = read_float("Значение: ")
        result = func_info[1](value)
        print(f"Результат: {result:.4f}\n")

        if not ask_continue():
            clear_screen()
            break


def _run_base_converter() -> None:
    """Перевод чисел из 2/8/16‑ичной в 10‑ичную систему."""
    while True:
        base = read_int("Исходная система (2/8/16): ")
        value = input("Число: ").strip()
        if value.lower() in STOP_WORDS:
            raise KeyboardInterrupt
        try:
            result = converters.base_to_decimal(value, base)
            print(f"Десятичное значение: {result}\n")
        except ValueError as err:
            print(err)

        if not ask_continue():
            clear_screen()
            break


def _run_deposit_calculator() -> None:
    """Калькулятор доходности вклада с учётом капитализации."""
    while True:
        principal = read_float("Начальная сумма: ")
        rate = read_float("Годовая ставка (%): ")
        years = read_int("Срок (лет): ")
        comp = read_int("Капитализаций в год (≥1): ")
        contrib = read_float("Регулярный взнос за период (0, если нет): ")

        try:
            fv = deposit.calculate_compound_interest(
                principal, rate, years, compounding=comp, contribution=contrib
            )
            print(f"Будущая стоимость: {fv}\n")
        except ValueError as err:
            print(err)

        if not ask_continue():
            clear_screen()
            break


def main() -> None:
    """Основная функция для взаимодействия с CLI-интерфейсом программы."""
    actions: Dict = {
        1: _run_arithmetic,
        2: _run_unit_converter,
        3: _run_base_converter,
        4: _run_deposit_calculator,
    }

    print("Добро пожаловать! (для выхода вводите 'q')")

    while True:
        try:
            print(menu.generate_menu())
            choice = read_int("Ваш выбор: ")
        except KeyboardInterrupt:
            break

        if choice == 0:
            break

        action = actions.get(choice)
        if action is None:
            print("Неизвестный пункт меню. Попробуйте снова.\n")
            continue

        try:
            action()
        except KeyboardInterrupt:
            print()
            continue

    print("Выход. Спасибо, что пользуетесь калькулятором!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПринудительный выход по Ctrl+C.")
        sys.exit(0)
