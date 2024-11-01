# To-Do API Project

A simple To-Do list API built using **FastAPI**. This project provides basic CRUD (Create, Read, Update, Delete) operations to manage tasks, with endpoints to interact with and update a list of tasks.

## Features

- **Create a Task**: Add a new to-do item.
- **Read Tasks**: View all tasks or individual task details.
- **Update a Task**: Modify existing tasks.
- **Delete a Task**: Remove tasks when completed.
![image](https://github.com/user-attachments/assets/42c9aee9-5907-4835-80a8-236828765164)

## Getting Started

### Prerequisites

- **Python 3.8+**
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

### Running the API

Run the server with FastAPI:
```bash
uvicorn app:app --reload
```

API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

1. **GET /tasks** - Retrieve all tasks.
2. **POST /tasks** - Add a new task.
3. **PUT /tasks/{task_id}** - Update a specific task.
4. **DELETE /tasks/{task_id}** - Delete a task.

## Example Requests

- **Adding a Task**:
  ```json
  {
    "title": "New Task",
    "description": "Task details here"
  }
  ```

## Models

Define and manage task data in `models.py`, handling essential fields like `title` and `description` for each task.

## License

MIT License

!
