# FastAPI Todo App

This is a simple FastAPI application that allows you to manage Todo items. You can perform CRUD (Create, Read, Update, Delete) operations on Todo items using this application. The application uses an SQLite database to store Todo items.

## Getting Started

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/fastapi-todo-app.git
   ```

2. Navigate to the project directory:
   ```sh
   cd fastapi-todo-app
   ```

3. Install dependencies (ensure you have Python and pip installed):
   ```sh
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:
   ```sh
   uvicorn main:app_fast --reload
   ```

   The API will be available at `http://localhost:8000`.

## API Endpoints

### 1. Get All Todo Items

- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Get a list of all Todo items.

### 2. Create a Todo Item

- **Endpoint**: `/create/`
- **Method**: `POST`
- **Description**: Create a new Todo item.
- **Request Body**: JSON object with `todo` (string) and `is_done` (boolean) fields.

### 3. Update a Todo Item

- **Endpoint**: `/update/{todo_id}`
- **Method**: `PUT`
- **Description**: Update an existing Todo item by its ID.
- **Path Parameter**: `todo_id` (integer)
- **Request Body**: JSON object with `todo` (string) and `is_done` (boolean) fields.

### 4. Delete a Todo Item

- **Endpoint**: `/delete/{todo_id}`
- **Method**: `DELETE`
- **Description**: Delete a Todo item by its ID.
- **Path Parameter**: `todo_id` (integer)


## Technologies Used

**FastAPI**: Web framework for building APIs with Python 3.6+.
**SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for Python.
