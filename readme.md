# TechTrack API

**Customer company:** TechTrack

## Project Description

TechTrack is developing a platform for monitoring and managing technical equipment such as industrial robots, manufacturing equipment, and quality control systems. This API is designed to handle equipment management and provide functionalities for creating, reading, updating, and deleting users and equipment data. 

The API uses JWT-based authentication and supports CRUD operations for managing equipment data, including tracking of equipment status (e.g., temperature, speed, pressure). Additionally, it generates alerts for critical equipment conditions that require operator attention.

## Features

- **CRUD Operations**: Manage equipment, equipment data, and alerts.
- **JWT-based Authentication**: Secured API endpoints using access tokens.
- **Error Handling**: Returns appropriate HTTP statuses and error messages.
- **Data Integrity**: Ensures data consistency via database transactions.
- **Swagger Documentation**: Automatically generated API documentation.

## API Endpoints

### Authentication
- **POST** `/api/token/`: Obtain a JWT token by providing username and password.
- **POST** `/api/token/refresh/`: Refresh JWT token using the refresh token.

### Equipment
- **GET** `/api/equipment/`: Retrieve a list of equipment.
- **POST** `/api/equipment/`: Create new equipment.
- **GET** `/api/equipment/{id}/`: Retrieve a specific equipment by ID.
- **PUT** `/api/equipment/{id}/`: Update a specific equipment by ID.
- **DELETE** `/api/equipment/{id}/`: Delete a specific equipment by ID.

### Data
- **GET** `/api/data/`: Retrieve a list of equipment data.
- **POST** `/api/data/`: Create new data for equipment.
- **GET** `/api/data/{id}/`: Retrieve a specific data entry by ID.
- **PUT** `/api/data/{id}/`: Update a specific data entry by ID.
- **DELETE** `/api/data/{id}/`: Delete a specific data entry by ID.

### Alerts
- **GET** `/api/alerts/`: Retrieve a list of alerts.
- **POST** `/api/alerts/`: Create a new alert for equipment.
- **GET** `/api/alerts/{id}/`: Retrieve a specific alert by ID.
- **PUT** `/api/alerts/{id}/`: Update a specific alert by ID.
- **DELETE** `/api/alerts/{id}/`: Delete a specific alert by ID.

## Requirements

- **Python 3.x**
- **Django 3.x**
- **Django REST Framework**
- **djangorestframework-simplejwt** for JWT Authentication
- **drf-yasg** for Swagger documentation

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/techtrack-api.git
   cd techtrack-api

2. **Set up a virtual environment:**

   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`


3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt


4. **Run database migrations:**

   ```bash
    python manage.py makemigrations
    python manage.py migrate


5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser


6. **Start the Django development server:**

   ```bash
   python manage.py runserver


7. **Access the API:**

   ```bash
   You can now access the API at http://127.0.0.1:8000/api/.

## Swagger API Documentation

You can view the automatically generated API documentation at:
    ```bash
    http://127.0.0.1:8000/swagger/
    ```


## Testing the API
1. Obtain a JWT token:

Use the following curl command to obtain a JWT token:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'

```
2. Use the JWT token for authenticated requests:

Include the JWT token in the Authorization header for subsequent requests:

```bash
curl -H "Authorization: Bearer your_jwt_access_token" http://127.0.0.1:8000/api/equipment/
```
## FAQ
### How will you ensure the security of your API?
We use JWT-based authentication to secure the API. Only authenticated users with valid access tokens can access protected resources.

### How will you ensure the performance of your API?
We implement data caching and database query optimization to improve performance. The application can be scaled horizontally to handle large volumes of requests.

### How will you ensure data consistency?
We use transaction mechanisms in the database to ensure data integrity during create, update, and delete operations.




