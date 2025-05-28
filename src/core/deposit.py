"""
Файл deposit.py содержит в себе калькулятор сложных процентов, вычисляющий будущую стоимость вклада.
"""

__all__ = ["calculate_compound_interest"]


def calculate_compound_interest(
    principal: float,
    annual_rate: float,
    years: int,
    /,
    *,
    compounding: int = 1,
    contribution: float = 0.0,
) -> float:
    """Вычисляет будущую стоимость вклада."""
    if any(x < 0 for x in (principal, annual_rate, years, contribution)):
        raise ValueError("Все числовые параметры должны быть неотрицательны.")
    if compounding < 1:
        raise ValueError("Частота капитализации должна быть ≥ 1.")

    rate_per_period = (annual_rate / 100) / compounding
    total_periods = years * compounding

    fv_principal = principal * (1 + rate_per_period) ** total_periods

    if contribution:
        fv_contribution = contribution * (
            ((1 + rate_per_period) ** total_periods - 1) / rate_per_period
        )
    else:
        fv_contribution = 0.0

    return round(fv_principal + fv_contribution, 2)
