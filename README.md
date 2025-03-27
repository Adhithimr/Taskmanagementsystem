# Taskmanagementsystem
This is a Django REST Framework (DRF) project for managing tasks. It includes user registration, login with JWT authentication, and CRUD operations for tasks.

##Features
**User Authentication:**
    * User registration.
    * User login with JWT (JSON Web Tokens) authentication.
    * Secure password handling.
**Task Management:**
    * Create, read, update, and delete tasks.
    * Filtering tasks by completion status and due date.
    * Authentication required for task management.
**Admin Interface:**
    * Django admin for user management.

## Technologies
  * Python
  * Django
  * Django REST Framework (DRF)
  * djangorestframework-simplejwt
## Setup
1.**Clone the Repository**
2.**Create a Virtual Environment (Recommended)**
3.**Run Migrations:**
  -python manage.py makemigrations
  -python manage.py migrate
4.**Create a Superuser (for Django admin):**
  -python manage.py createsuperuser
5. **Run the Server:**
  -python manage.py runserver
6.**Access the API:**
  -homepage- http://127.0.0.1:8000/ 
  -admin - http://127.0.0.1:8000/admin/
7.**User Registration:**
    * `POST /register/`
    * Requires `username` and `password` in the request body

8.**Tasks:**
    * `GET /tasks/` - List all tasks (with optional filtering).
    * `POST /tasks/` - Create a new task.
    * `GET /tasks/{id}/` - Retrieve a specific task.
    * `PUT /tasks/{id}/` - Update a specific task.
    * `PATCH /tasks/{id}/` - Partially update a specific task.
    * `DELETE /tasks/{id}/` - Delete a specific task.
    * Requires JWT authentication

