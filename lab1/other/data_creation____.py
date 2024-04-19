import numpy as np
from sklearn.datasets import make_classification # генерируем наборы данных
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

N = 150
noises = 0.15

# Функция по генерированию линейно-разделимых данных
def make_binary_clf(N,
                    noises = 0.15,
                    random_state = 42,):
    """Создание синтетического набора данных
    для бинарной классификации
    Входные переменные:
    ===========
    N: количество точек
    noises: коэффициент ~ сила шума
    random_state: фиксированный сид случайных чисел (для повторяемости)
    """
    # фиксируем случайный seed
    if random_state: rng = np.random.RandomState(seed = random_state)

    # создаем набор данных с использованием функции make_classification
    # это будут линейно-разделимые данные
    X, y = make_classification(n_samples=N, # количество точек
                               n_features=2, # количество признаков
                               n_redundant=0, # количество бесполезных признаков
                               n_informative=2,# количество информативных признаков
                               n_clusters_per_class=1, # количество групп точек на класс
                               class_sep=2, # количество классов
                               random_state=random_state # фиксированный сид случайных чисел
                               )
    X += np.random.randn(*X.shape) *noises # добавляем к признакам случайный шум

    return X,y

X, y = make_binary_clf(N, noises = noises)

print(X)
print(y)