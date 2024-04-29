# mlops_practice
УрФУ/Skillfactory. Автоматизация администрирования MLOps

Запуск приложения API
Для запуска приложения необходимо дать команду:

$ uvicorn task_3_api_v2:app

Проверка работы API
Для проверки разработаны скриты для утилиты curl:

curl_get_local_root.sh - проверяем обращение методом GET к корню сайта;
curl_post_local_predict.sh - проверяем обращения методом POST по пути /predict/.


You can then build and run the Docker image:

$ docker build -t mlops-lab3-app .
$ docker run -d --name mlops-lab3 mlops-lab3-app:latest

docker-compose up -d


