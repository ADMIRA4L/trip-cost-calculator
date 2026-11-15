# ==========================================
# КАЛЬКУЛЯТОР СТОИМОСТИ ПОЕЗДКИ
# Изменённая версия предыдущего задания
# ==========================================

def calculate_trip_cost(distance, consumption, price):
    """Возвращает общую стоимость топлива для поездки."""
    liters_needed = (distance / 100) * consumption
    return liters_needed * price


def get_positive_number(prompt, data_type=float):
    """Запрашивает положительное число и повторяет ввод при ошибке."""
    while True:
        try:
            value = data_type(input(prompt))
            if value <= 0:
                print("Значение должно быть больше нуля. Повторите ввод.")
                continue
            return value
        except ValueError:
            print("Некорректный ввод. Введите число ещё раз.")


def main():
    print("=== Калькулятор стоимости поездки ===\n")

    driver_name = input("Введите ваше имя: ").strip()
    while not driver_name:
        print("Имя не должно быть пустым.")
        driver_name = input("Введите ваше имя: ").strip()

    passenger_count = get_positive_number(
        "Введите количество человек в машине: ", int
    )
    trip_distance = get_positive_number(
        "Введите расстояние поездки (в км): "
    )
    fuel_consumption = get_positive_number(
        "Расход топлива на 100 км (в литрах): "
    )
    fuel_price = get_positive_number(
        "Цена за 1 литр топлива (в рублях): "
    )

    total_price = calculate_trip_cost(
        trip_distance, fuel_consumption, fuel_price
    )
    cost_per_person = total_price / passenger_count

    extra_expenses = ["Платные дороги", "Парковка", "Перекус на АЗС"]

    print(f"\nПривет, {driver_name}! Вот итоговый расчет:")
    print(f"Общая стоимость топлива: {total_price:.2f} руб.")
    print(f"С каждого человека: {cost_per_person:.2f} руб.")

    print("\nВозможные дополнительные расходы:")
    for item in extra_expenses:
        print(f"- {item}")
    
if __name__ == "__main__":
    main()
# Тестовый коммит
