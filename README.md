Project Title: Full-Stack Task Management System
Overview

This project is a full-stack task management application built using:

Frontend: React

Backend: Flask

Database: SQLite (Relational Database)

The system allows users to create and view tasks through a REST API architecture.

Architecture

The system follows a three-layer architecture:

Presentation Layer – React frontend

Application Layer – Flask REST API

Persistence Layer – SQLite relational database

The frontend communicates with the backend via HTTP requests.
The backend handles validation, business logic, and persistence.

Technical Decisions
1. Flask for Backend

Flask was chosen because it is lightweight, flexible, and suitable for building RESTful APIs with minimal overhead.

2. React for Frontend

React was selected for its component-based architecture and state management capabilities.

3. SQLite as Relational Database

SQLite was chosen because:

It is fully relational (tables, primary keys, SQL support)

Requires no external server setup

Suitable for small-to-medium applications

Easily replaceable with PostgreSQL or MySQL in production

4. API Validation at Backend

Validation is enforced at the API boundary:

Empty titles are rejected

Proper HTTP status codes are returned

This ensures system consistency and prevents invalid states.

5. REST Standards

GET /tasks → Retrieve tasks

POST /tasks → Create task

Uses correct HTTP status codes (200, 201, 400)

Database Schema

Table: tasks

Column	Type	Constraint
id	INTEGER	PRIMARY KEY AUTOINCREMENT
title	TEXT	NOT NULL
Risks & Limitations

No authentication implemented

No automated testing included

SQLite not ideal for high concurrency

No update/delete functionality yet

Extension Approach

Future improvements:

Add PUT and DELETE endpoints

Implement authentication

Replace SQLite with PostgreSQL

Add unit and integration tests

Containerize using Docker

How to Run
Backend
cd backend
pip install -r requirements.txt
python app.py
Frontend
cd frontend
npm install
npm start