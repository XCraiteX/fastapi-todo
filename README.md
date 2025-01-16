# Simple TODO

**Very simpl TODO REST API for Python + SQLAlchemy**

## Stack
- **Python3**
- **SQLAlchemy (sqlite)**
- **FastAPI**

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/XCraiteX/fast-todo
```

### 2. Run code on `localhost`
```bash
uvicorn todo:app --reload
```

### 3. Use Postman for tests

## API Functions

### 1. Get all tasks | `GET`
 
`/get_tasks`

**Returns all tasks by classes in JSON**


### 2. Create Task | `POST`  

`/create_task`

**Creating task and returns "Successfully"**

- **"title"**: str
- **"content"**: str

**Example:**
```json
{
    "title": "Test task",
    "content": "Target"
}
```

### 3. Update Task | `PUT`

`/update_task/{task_id}`

- **"title"**: str
- **"content"**: str
- **"completed"**: bool

**Example:**
`/update_task/3`
```json
{
    "title": "Task 3",
    "content": "New content",
    "completed": true
}
```

### 4. Delete Task | `DELETE`

`/delete_task/{task_id}`

**Delete task and returns "Successfully"**