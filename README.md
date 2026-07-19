# Career Copilot AI

Платформа для подготовки к собеседованиям с помощью AI.

## 🚀 Возможности

- **AI Interview Simulation** - Практикуйтесь в интервью с AI
- **Resume Analysis** - Анализ и улучшение резюме
- **Vacancy Matching** - Поиск подходящих вакансий
- **Performance Tracking** - Отслеживание прогресса

## 📋 Требования

- Python 3.10+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose (опционально)

## 🛠️ Установка

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## 📝 Конфигурация

Создайте файл `.env` в директории `backend`:

```env
DATABASE_URL=postgresql://user:password@localhost/career_copilot
JWT_SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-openai-key
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

## 🚀 Запуск

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm start
```

## 🗄️ База данных

```bash
cd backend
alembic upgrade head
```

## 🧪 Тестирование

```bash
cd backend
pytest
```

## 📚 API Documentation

После запуска backend'а документация доступна по адресу:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🐳 Docker Compose

```bash
docker-compose up -d
```

## 📄 Лицензия

MIT
