# mlops_practice
УрФУ/Skillfactory. Автоматизация администрирования MLOps

Для запуска приложения API необходимо дать команду:

$ uvicorn src.api_app:app --host 0.0.0.0 --port 8000

или запустить командный файл **start.bat** (Windows), **start.sh** (*nix like).

Для проверки работы приложения имеется командный файл с утилитой curl:

$ predict.bat (predict.sh)

При этом осуществляется обращение к API приложению методом POST по пути /predict.

Для создания docker образа микросервиса создан файл Dokerfile. 
Создание образа вручную осуществляется командой:

$ docker build -t mlops-lab3-app .

Запуск контейнера из образа:

$ docker run -d --name mlops-lab3 mlops-lab3-app:latest

Автоматическая сборка образа и запуск контейнера осуществляется при помощи 
файла-сценария docker-compose.yml. Для этого необходимо выполнить команду: 

$ docker-compose up -d



