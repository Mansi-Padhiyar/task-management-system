Architecture Decision

Frontend: React (component-based UI)

Backend: Flask (lightweight REST API)

Database: SQLite (lightweight relational DB)

Why?

Clear separation of concerns

Simple but scalable architecture

Easy to extend

Database Decision

Why SQLite?

Relational

No server setup

Auto file-based storage

Suitable for small-to-medium apps

Easily replaceable with PostgreSQL later

Validation Decision

Validation handled at API boundary

Backend rejects empty titles

Prevents invalid system states

Error Handling

HTTP status codes used correctly:

200 → success

201 → created

400 → bad request