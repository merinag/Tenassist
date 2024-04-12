# Tenassist Django Project

This is a Django project for Tenassist,  The project uses Bootstrap for styling and SQLite as the database.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

git clone https://github.com/Atesfahun/Tenassist.git
2. Navigate to the project directory:

cd Tenassist
3. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate (Mac/Linux)
venv\Scripts\activate (Windows)
4. Install the dependencies:

pip install -r requirements.txt
5. Run the Django migrations:

python manage.py migrate
6. Start the Django development server:

python manage.py runserver
7. Open your web browser and go to <http://localhost:8000/> to see the application in action.

## Project Structure

The project structure is as follows:

* `Tenassist`: The main Django project directory.
	+ `manage.py`: The Django management script.
	+ `Tenassist`: The Django project module.
	+ `settings.py`: The Django project settings.
	+ `urls.py`: The Django project URL declarations.
	+ `wsgi.py`: The Django project WSGI script.
	+ `asgi.py`: The Django project ASGI script.
* `tenassist`: The Django app directory.
	+ `migrations`: The Django app migrations directory.
	+ `templates`: The Django app templates directory.
	+ `static`: The Django app static files directory.
	+ `admin.py`: The Django app admin configuration.
	+ `apps.py`: The Django app configuration.
	+ `models.py`: The Django app models.
	+ `tests.py`: The Django app tests.
	+ `urls.py`: The Django app URL declarations.
	+ `views.py`: The Django app views.

## Bootstrap

Bootstrap is used for styling the application. The Bootstrap CSS and JavaScript files are included in the `base.html` template, which is extended by all other templates in the project.

## SQLite

SQLite is used as the database for the application. The database file is named `db.sqlite3` and is located in the project root directory.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request.

## License

The project is licensed under the MIT License. See the `LICENSE` file for deta
