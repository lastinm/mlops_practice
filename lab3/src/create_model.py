import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump                                 # в scikit-learn ничего такого особенного нет
                                                        # пользуемся joblib

# Загрузка датасета iris
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели случайного леса
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Предсказание на тестовом наборе
rf_y_pred = rf_model.predict(X_test)

# Оценка точности модели случайного леса
rf_accuracy = accuracy_score(y_test, rf_y_pred)
print("Random Forest Accuracy:", rf_accuracy)

# Получаем правильные пути
# script_directory = os.path.dirname(os.path.abspath(__file__))
# print("Каталог, из которого запущен скрипт:", script_directory)
script_directory = os.path.abspath(__file__)
parent_dir = os.path.dirname(script_directory)
parent_parent_dir = os.path.dirname(parent_dir)
# print("Путь к вышестоящему каталогу:", parent_parent_dir)
true_path = os.path.join(parent_parent_dir, 'model', 'model.joblib')
# print(true_path)

# Сохраняем обученную модель в файл
try:
    dump(rf_model, true_path)
    print('Модель успешно сохранена в:', true_path)
except Exception as e:
    print('Произошла ошибка при сохранении модели:', e)