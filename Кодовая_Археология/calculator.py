# Класс для расчета скорости тягача с учетом массы, времени и расстояния
class TruckSpeedCalculator:
    def __init__(self):
        # Инициализация начальных значений:
        # масса тягача, время перемещения и расстояние
        self.mass = 0.0  # Масса тягача (кг)
        self.travel_time = 0.0  # Время перемещения (часы)
        self.distance = 0.0  # Расстояние (км)

    def calculate_speed(self):
        # Метод расчета скорости с несколькими защитными механизмами

        # Защита от деления на ноль
        if self.travel_time == 0:
            return 0.0

        # Базовая скорость среднего тягача
        base_speed = 60.0  # км/ч

        # Коэффициент замедления в зависимости от массы
        # Чем больше масса, тем меньше коэффициент
        mass_coefficient = 1 - (self.mass / 20000)

        # Расчет средней скорости с учетом:
        # 1. Пройденного расстояния
        # 2. Времени в пути
        # 3. Коэффициента массы
        average_speed = (self.distance / self.travel_time) * mass_coefficient

        # Округление результата до двух знаков после запятой
        return round(average_speed, 2)

    def set_parameters(self, mass, travel_time, distance):
        # Метод установки параметров для расчёта
        # Преобразование входных данных в числа с плавающей точкой
        self.mass = float(mass)  # масса в килограммах
        self.travel_time = float(travel_time)  # время в часах
        self.distance = float(distance)  # расстояние в километрах