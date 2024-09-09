# Task Manager API

## Description

**Task Manager API** is a RESTful API developed with **Flask** y **MongoDB** for task management (To-Do list). 
Users can register, log in, and manage their tasks (create, get, update and delete). 
**JWT (JSON Web Tokens)** is used to authenticate users.

## Technologies used

- **Flask** (microframework web)
- **MongoDB Atlas** (base de datos en la nube)
- **Flask-JWT-Extended** (para la autenticación con JWT)
- **Flask-PyMongo** (para interactuar con MongoDB)
- **python-dotenv** (para manejar variables de entorno)

---

## Installation

Sigue estos pasos para configurar y ejecutar el proyecto en tu maquina local:

### 1. Clone the repository

```bash
git clone https://github.com/tu-usuario/task-manager-api.git
cd task-manager-api

```
### 2. Create and activate the virtual environment

## On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## On Windows

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setting environment variables

Create a .env file in the root of the project with the following contents, replacing the values ​​of MONGO_URI and JWT_SECRET_KEY with your own credentials:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
JWT_SECRET_KEY=your_secret_key
```

MONGO_URI: The connection URL for your MongoDB database in MongoDB Atlas.
JWT_SECRET_KEY: A random secret key that will be used to sign the JWT tokens.

### 5. Running the application

```bash
python run.py
```
The application should now be running on http://127.0.0.1:5000/


## Use

### 1. Testing the API

To test the API, you can use Postman, Insomnia, or any REST API client. Make sure to include the header Authorization: Bearer <token> for routes that require authentication.

### 2. API Documentation

# Headers
- **Content-Type**: application/json
- **X-Api-Key**: "api key"

## Endpoints
- [POST /auth/register](#authregister-post) : Register a new user
- [POST /auth/login](#authlogin-post) : Login a user by email and password
- [POST /api/tasks](#apitasks-post) : Create a new task
- [GET /api/tasks](#apitasks-get) : Get all tasks of the authenticated user
- [PUT /api/tasks/{task_id}](#apitaskstask_id-put) : Update a task by its ID
- [DELETE /api/tasks/{task_id}](#apitaskstask_id-delete) : Delete a task by its ID

### /auth/register [Post]
- **Description**: register a user by email and password.
- **Parameters**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```
- **Response**:
```json
{
  "success": true, 
  "message": "User created successfully"
}
```

### /auth/login [Post]
- **Description**: Login with email and password. Returns a JWT token.
- **Parameters**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```
- **Response**:
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### /api/tasks [Post]
- **Description**: Create a new task for the authenticated user.
- **Parameters**:
```json
{
  "title": "buy milk",
  "status": "pending"
}
```
- **Response**:
```json
{
  "success": true,
  "id": "60f6f1b65f7e9d3bb8f2c7b1"
}
```

### /api/tasks [GET]
- **Description**: Get all tasks associated with the authenticated user.
- **Headers**: 
    Authorization: "Bearer <token>"
- **Response**:
```json
{
  "success": true,
  "tasks": [
    {
      "id": "60f6f1b65f7e9d3bb8f2c7b1",
      "title": "Comprar leche",
      "status": "pending"
    },
    {
      "id": "60f6f1d65f7e9d3bb8f2c7b2",
      "title": "Pagar facturas",
      "status": "completed"
    }
  ]
}
```

### /api/tasks/{task_id} [PUT]
- **Description**: Update a task by its ID. You can update the title and status.
- **Headers**: 
    Authorization: "Bearer <token>"
- **Parameters**:
```json
{
  "title": "buy milk",
  "status": "completed"
}
```
- **Response**:
```json
{
  "success": true,
  "message": "Task updated"

}
```

### /api/tasks/{task_id} [DELETE]
- **Description**: Delete a task by its ID.
- **Headers**: 
    Authorization: "Bearer <token>"
- **Parameters**:
```json
{
  "task_id": "60f6f1b65f7e9d3bb8f2c7b1"
}
```
- **Response**:
```json
{
  "success": true,
  "message": "Task deleted"
}
```