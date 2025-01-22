"""
Модуль маршрутов Flask-приложения.

Содержит обработчики запросов для различных URL.
"""

from flask import request
from app import app

@app.route('/')
def hello():
    """
    Обработчик для корневого URL (/).

    Возвращает сообщение с подставленными значениями из GET-запроса.
    Если параметры не переданы, используются значения по умолчанию.

    Returns:
        str: Сообщение в формате "Hello {name}! {message}!".
    """
    name = request.args.get('name', 'Recruto')  # Получаем значение параметра 'name' из запроса
    message = request.args.get('message', 'Давай дружить')  # Получаем значение параметра 'message' из запроса
    return f'Hello {name}! {message}!'