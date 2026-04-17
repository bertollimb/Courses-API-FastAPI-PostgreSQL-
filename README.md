# 📚 Courses API (FastAPI + PostgreSQL)

A REST API for managing courses, built with FastAPI, SQLAlchemy (async) and PostgreSQL.  
This project demonstrates backend development best practices, clean architecture and asynchronous programming.

---

## 🚀 Features

- Create courses
- List all courses
- Get course by ID
- Update courses
- Delete courses
- Async database integration
- Environment-based configuration (.env)
- Clean project structure

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy (Async ORM)
- PostgreSQL
- Pydantic v2
- Uvicorn
- Asyncpg

---

## 📁 Project Structure

api/
    v1/
        endpoints/
core/
    database.py
    settings_.py
    deps.py
models/
    __all_models.py
    course_models.py
schemas/
    course_schema.py

create_table.py
main.py
requirements.txt

---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/bertollimb/courses-api.git  
cd courses-api

---

### 2. Create virtual environment

python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows

---

### 3. Install dependencies
pip install fastapi psycopg2-binary sqlalchemy asyncpg uvicorn
pip freeze > requirements.txt
pip install pydantic-settings


---

### 4. Configure environment variables

Create a .env file:

DB_URL=postgresql+asyncpg://user:password@localhost:5432/dbname

---

### 5. Create database tables

python create_table.py

---

### 6. Run the server

uvicorn main:app --reload

---

## 📡 API Documentation

http://localhost:8000/docs

---

## 📌 Base URL

/api/v1/courses

---

## 🔥 Endpoints

### POST /courses/
Create a new course

{
  "title": "Python for Beginners",
  "course_classes": 40,
  "hours": 50
}

---

### GET /courses/
List all courses

---

### GET /courses/{id}
Get course by ID

---

### PUT /courses/{id}
Update a course

---

### DELETE /courses/{id}
Delete a course

---

## 🧠 What I learned from this project

- Building REST APIs with FastAPI
- Async database operations with SQLAlchemy
- Clean project structure for backend applications
- Environment variable management
- CRUD operations best practices

---

## 🚀 Future improvements

- Authentication with JWT
- Role-based access control
- Pagination and filtering
- Docker support
- Deployment (Render / Railway)

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Matheus Bertolli