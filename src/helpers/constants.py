"""файл constants.py содержит неизменяемые переменные, используемые в калькуляторе."""

METER_TO_FEET: float = 3.2808399
FEET_TO_METER: float = 1 / METER_TO_FEET

KG_TO_POUND: float = 2.20462262
POUND_TO_KG: float = 1 / KG_TO_POUND

SUPPORTED_BASES: set[int] = {2, 8, 16}
STOP_WORDS: set[str] = {"q", "quit", "exit", "выход"}
