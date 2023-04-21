﻿# Дипломный проект Яндекс Самокат: Автоматизация теста к API

- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск теста выполянется командой pytest
- Для запуска теста, необходимо указать рабочий URL в строке URL_SERVICE файла configuration.py

# Шаги автотеста:

- Выполнить запрос на создание заказа.
- Сохранить номер трека заказа.
- Выполнить запрос на получения заказа по треку заказа.
- Проверить, что код ответа равен 200.
