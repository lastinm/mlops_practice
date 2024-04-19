import os
import random
import numpy as np
import csv

# Зафиксируем постоянство генерируемых данных
random.seed = 42

# Создание данных температуры с шумами и аномалиями
def create_temperature_data(num_samples, noise_level=0.1, anomaly_chance=0.1):
    hours = np.arange(24)
    mean_temp = 25  # средняя температура
    # создаем нормальное распределение для температуры с пиком в 14 часов
    temperatures = np.exp(-0.5 * ((hours - 14) / 3)**2) * 10 + mean_temp
    # устанавливаем минимальное значение в ночные часы с 2 до 5
    temperatures[2:6] = 20
    return temperatures

# Сохранение данных в CSV файл
def save_data_to_csv(data, folder_name):
    os.makedirs(folder_name, exist_ok=True)
    for i, temperatures in enumerate(data):
        filename = os.path.join(folder_name, f"data_{i}.csv")
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Hour', 'Temperature'])
            for hour, temp in enumerate(temperatures):
                writer.writerow([hour, temp])

# Генерация данных для тренировочного и тестового наборов
num_train_samples = 10
num_test_samples = 5

train_data = [create_temperature_data(24, noise_level=0.3, anomaly_chance=0.1) for _ in range(num_train_samples)]
test_data = [create_temperature_data(24, noise_level=0.3, anomaly_chance=0) for _ in range(num_test_samples)]

save_data_to_csv(train_data, "train")
save_data_to_csv(test_data, "test")

print("Данные созданы и сохранены в папках 'train' и 'test' в формате CSV.")