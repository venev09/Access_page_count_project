# Page Counter Django Project

This Django project is designed to count the number of times a specific page has been accessed by users. The project follows the Model-View-Template (MVT) architecture of Django and consists of a single page at the URL `/counts`.

## Project Structure

The project is organized as follows:

```
pagecounter/
├── pagecounter/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── counter/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── counter/
│           └── count.html
├── manage.py
└── README.md
```

## Features

- **Access Count**: The application tracks how many times the `/counts` page has been accessed.
- **Database Storage**: The access count is stored in a database, allowing for persistent tracking across server restarts.

## Setup Instructions

1. **Install Django**: Make sure you have Django installed in your Python environment. You can install it using pip:

   ```
   pip install django
   ```

2. **Run Migrations**: Navigate to the project directory and run the following command to apply migrations:

   ```
   python manage.py migrate
   ```

3. **Run the Development Server**: Start the Django development server with the following command:

   ```
   python manage.py runserver
   ```

4. **Access the Application**: Open your web browser and go to `http://127.0.0.1:8000/counts` to see the access count.

## License

This project is open-source and available under the MIT License.