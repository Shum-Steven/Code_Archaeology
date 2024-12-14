# coding: utf-8
from typing import Tuple

def calculate_salary(
    hours_worked: float, 
    hourly_rate: float, 
    social_security_rate: float = 30.0
) -> Tuple[float, float, float]:
    """
    Рассчитывает зарплату с учетом социальных отчислений.
    
    Args:
        hours_worked: Количество отработанных часов
        hourly_rate: Почасовая ставка
        social_security_rate: Процент социальных отчислений (по умолчанию 30%)
    
    Returns:
        Кортеж из (брутто-зарплата, социальные отчисления, нетто-зарплата)
    """
    gross_pay = hours_worked * hourly_rate  # Брутто-зарплата
    social_security = gross_pay * social_security_rate / 100.0  # Отчисления на соц. страхование
    net_pay = gross_pay - social_security  # Нетто-зарплата
    
    return gross_pay, social_security, net_pay

def main() -> None:
    """
    Основная функция для интерактивного ввода и расчета зарплаты.
    """
    try:
        # Исправлена опечатка: inpyt -> input
        hours_worked = float(input("Введите количество проработанных часов: "))
        hourly_rate = float(input("Введите почасовую ставку: "))
        
        # Вынос ставки социальных отчислений в аргумент функции по умолчанию
        gross_pay, social_security, net_pay = calculate_salary(
            hours_worked, 
            hourly_rate
        )
        
        # Использование f-строк для более читаемого форматирования
        print(f"Брутто-зарплата: {gross_pay:.2f} руб.")
        print(f"Отчисления на соц. страхование: {social_security:.2f} руб.")
        print(f"Нетто-зарплата: {net_pay:.2f} руб.")
    
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")
# Исправлена опечатка в проверке точки входа в программу
if __name__ == "__main__":
    main()