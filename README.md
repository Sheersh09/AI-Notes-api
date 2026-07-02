# AI Notes API

A learning project built with **FastAPI** to understand modern backend development before building a larger application.

The project is being developed incrementally, with each phase introducing new backend concepts and ending with a working application.

---

## Current Progress

| Phase                                    | Status   |
| ---------------------------------------- | -------- |
| ✅ Phase 0 – Project Setup                | Complete |
| ✅ Phase 1 – API Fundamentals             | Complete |
| ✅ Phase 2 – Request Validation           | Complete |
| ✅ Phase 3 – CRUD Operations (In-Memory)  | Complete |
| ✅ Phase 4 – Project Structure & Routers  | Complete |
| ✅ Phase 5 – SQLite & SQLAlchemy          | Complete |
| ⬜ Phase 6 – Service Layer                | Upcoming |
| ⬜ Phase 7 – Search, Pagination & Sorting | Upcoming |
| ⬜ Phase 8 – Error Handling               | Upcoming |
| ⬜ Phase 9 – AI Integration               | Upcoming |
| ⬜ Phase 10 – API Documentation           | Upcoming |
| ⬜ Phase 11 – Deployment                  | Upcoming |

---

# Features Implemented

## Phase 0

* FastAPI project setup
* Virtual environment
* Uvicorn server
* Swagger UI (`/docs`)
* GitHub repository

---

## Phase 1

* GET endpoints
* Basic API routing
* HTTP methods
* Path parameters
* Query parameters
* JSON responses

---

## Phase 2

* Request body validation
* Pydantic models
* Type validation
* Automatic request validation
* Interactive Swagger request forms

---

## Phase 3

* CRUD implementation
* Basic backend logic
* Lists Storage
* HTTP Status Code
* Features

---

## Phase 4

* APIRouter
* Modular Architecture
* Packages

---

## Phase 5

* SQLite
* SQLAlchemy
* ORM
* Tables
* Sessions

---


# Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

---

# Project Structure

```text
ai-notes-api/
│
├── app/
│   ├── main.py
│   │
│   └── routers/
│       └── notes.py          # All note-related endpoints
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# API Endpoints

## General

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| GET    | `/`      | Welcome message     |
| GET    | `/about` | Project information |

---

## Notes

| Method | Endpoint           | Description                            |
| ------ | ------------------ | -------------------------------------- |
| GET    | `/notes/{note_id}` | Get a note by ID                       |
| GET    | `/notes?limit=`    | Demonstrate query parameters           |
| POST   | `/notes`           | Create a note using request validation |

---

# Learning Objectives

This project is focused on learning:

* FastAPI fundamentals
* REST API development
* Request validation with Pydantic
* Backend project organization
* Database integration
* AI API integration
* Deployment

---

# Run Locally

Install dependencies

```bash
pip install -r requirements.txt
```

Start the development server

```bash
uvicorn app.main:app --reload
```

Open:

* http://127.0.0.1:8000
* http://127.0.0.1:8000/docs

---

# Roadmap

* [x] Project setup
* [x] API fundamentals
* [x] Request validation
* [ ] CRUD operations
* [ ] Modular project structure
* [ ] SQLite integration
* [ ] SQLAlchemy ORM
* [ ] AI summarization
* [ ] Quiz generation
* [ ] Deployment on Render

---

# Purpose

This project serves as a stepping stone toward building a full-featured AI application. Each phase introduces new backend engineering concepts while keeping the project functional and deployable throughout development.
