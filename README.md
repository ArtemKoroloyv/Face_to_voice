
## Стек

- Python 3.x
- FastAPI
- Uvicorn
- HTML, CSS, JavaScript

## Установка и запуск

1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/ArtemKorolovyy/DEMO_F2V.git
    cd DEMO_F2V
    ```

2. Создать виртуальное окружение:
    ```bash
    python -m venv venv
    ```

3. Активировать окружение:

    Windows:
    ```bash
    venv\Scripts\activate
    ```

    Linux/macOS:
    ```bash
    source venv/bin/activate
    ```

4. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

5. Запустить backend:
    ```bash
    uvicorn backend.main:app --reload
    ```

Backend будет доступен по адресу:  
http://127.0.0.1:8000  
Документация (Swagger):  
http://127.0.0.1:8000/docs

6. Открыть frontend:
    - Файл `frontend/index.html` открыть в браузере вручную.

## Локальное хранение данных

- Файлы сохраняются в каталоге `backend/storage/`
- Структура каталогов создается автоматически при выполнении сервера.

## Ограничения

- Максимальный размер изображения: 25 МБ
- Допустимые форматы изображений: JPG, PNG
- Максимальная длина текста: 5000 символов
- Обработка загруженных данных не выполняется

