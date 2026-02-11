"""
Основное Flask приложение для API учета товаров
"""

from flask import Flask, jsonify
from flask_cors import CORS
import os

# Создаем Flask приложение
app = Flask(__name__)

# Включаем CORS для работы с фронендом
CORS(app)

# Основной маршрут
@app.route('/')
def home():
    """Главная страница API"""
    return jsonify({
        'message': 'API системы учета товаров',
        'version': '1.0.0',
        'endpoints': '1.0.0',
        'endpoints': {
            'GET /': 'Информация об API',
            'GET /health': 'Проверка состояния сервера'
        }
    })