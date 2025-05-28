import csv

from homework_11_API_weather.config import get_weather_data


CITIES = ["Москва", "Нью-Йорк", "Токио", "Лондон", "Берлин"]


def main():
    weather_data = []

    for city in CITIES:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)

    if weather_data:
        total_temp = sum(item['temperature'] for item in weather_data)
        avg_temp = total_temp / len(weather_data)
        max_temp_city = max(weather_data, key=lambda x: x['temperature'])
        min_temp_city = min(weather_data, key=lambda x: x['temperature'])

        print(f"Средняя температура: {avg_temp:.2f}°C")
        print(f"Город с самой высокой температурой: {max_temp_city['city']} ({max_temp_city['temperature']}°C)")
        print(f"Город с самой низкой температурой: {min_temp_city['city']} ({min_temp_city['temperature']}°C)")

        with open('weather_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=weather_data[0].keys())
            writer.writeheader()
            writer.writerows(weather_data)


if __name__ == "__main__":
    main()
