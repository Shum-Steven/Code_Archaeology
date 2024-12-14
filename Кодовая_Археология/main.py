# Импортируем необходимые модули Flask для создания веб-приложения
from flask import Flask, render_template, request, jsonify
# Импортируем наш класс калькулятора из отдельного модуля
from calculator import TruckSpeedCalculator

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Создаем экземпляр калькулятора для использования в приложении
calculator = TruckSpeedCalculator()

# Маршрут для корневой страницы (главная страница)
@app.route('/')
def index():
    # Возвращаем HTML-шаблон index.html при обращении к корневому URL
    return render_template('index.html')

# Маршрут для расчета скорости с использованием метода POST
@app.route('/calculate', methods=['POST'])
def calculate():
    # Получаем значения из формы
    mass = request.form['mass']  # Масса тягача
    travel_time = request.form['travel_time']  # Время перемещения
    distance = request.form['distance']  # Расстояние

    # Устанавливаем параметры в калькулятор
    calculator.set_parameters(mass, travel_time, distance)

    # Рассчитываем скорость
    speed = calculator.calculate_speed()

    # Возвращаем результат в формате JSON
    return jsonify({'speed': speed})

# Точка входа в приложение
if __name__ == '__main__':
    # Запускаем Flask-сервер на всех сетевых интерфейсах
    # порт 8080 позволяет избежать конфликтов с другими службами
    app.run(host='0.0.0.0', port=8080)