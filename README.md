# TLN API v0.0.2

## Overview
TLN API is a Django-based project that provides a backend system for managing accounts, bookings, and studios. It is designed to handle user authentication, studio management, and booking functionalities. The project is structured into three main Django apps:

1. **Accounts**: Handles user authentication and registration.
2. **Bookings**: Manages studio bookings.
3. **Studios**: Manages studio information.

---

## Project Structure

```
TLN-0.0.2V/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── accounts/
│   ├── __init__.py
│   ├── adapter.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── bookings/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── studios/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
```

---

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TLN-0.0.2V
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Accounts
- **`POST /accounts/login/`**: User login.
- **`POST /accounts/logout/`**: User logout.
- **`POST /accounts/register/`**: User registration.

### Bookings
- **`GET /bookings/`**: List all bookings.
- **`POST /bookings/`**: Create a new booking.
- **`GET /bookings/<id>/`**: Retrieve a specific booking.
- **`PUT /bookings/<id>/`**: Update a specific booking.
- **`DELETE /bookings/<id>/`**: Delete a specific booking.

### Studios
- **`GET /studios/`**: List all studios.
- **`POST /studios/`**: Add a new studio.
- **`GET /studios/<id>/`**: Retrieve a specific studio.
- **`PUT /studios/<id>/`**: Update a specific studio.
- **`DELETE /studios/<id>/`**: Delete a specific studio.

---

## Usage

### Running the Server
To start the development server, run:
```bash
python manage.py runserver
```

### Example Requests
#### Login
```bash
curl -X POST http://127.0.0.1:8000/accounts/login/ -d "username=<USERNAME>&password=<PASSWORD>"
```

#### Create a Booking
```bash
curl -X POST http://127.0.0.1:8000/bookings/ -d "studio_id=<STUDIO_ID>&date=<DATE>&time=<TIME>"
```

#### List Studios
```bash
curl -X GET http://127.0.0.1:8000/studios/
```

---

## Testing
To run the tests, execute:
```bash
python manage.py test
```

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
