# Student Project Management System (SPMS)

A comprehensive web-based platform for managing student projects, assignments, and submissions. Built with Django, this system provides a user-friendly interface for students, teachers, and administrators.

## Features

- **User Management**
  - Role-based authentication (Student, Teacher, Admin)
  - Custom user profiles with avatars
  - Password reset functionality

- **Class Management**
  - Create and manage classes
  - Add/remove students from classes
  - View class details and enrolled students

- **Project Management**
  - Create and assign projects to classes
  - Set due dates and maximum scores
  - File upload support for project materials

- **Submission System**
  - Students can submit their work
  - Support for file uploads
  - Comments and feedback system
  - Submission status tracking

- **Grading System**
  - Teachers can grade submissions
  - Provide feedback to students
  - View submission history

## Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mrerror313coder/spms.git
   cd spms
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the project root and add your configuration:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Production Deployment (PythonAnywhere)

1. Sign up for a PythonAnywhere account at https://www.pythonanywhere.com/

2. Go to the Dashboard and create a new Web App:
   - Choose Manual Configuration
   - Choose Python 3.9 or later

3. Set up your virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 spms-env
   ```

4. Clone your repository:
   ```bash
   git clone https://github.com/mrerror313coder/spms.git
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Create a .env file with production settings:
   - Copy the contents from .env.production
   - Update with your actual values

7. Configure your web app:
   - Source code: /home/yourusername/spms
   - Working directory: /home/yourusername/spms
   - Virtual environment: /home/yourusername/.virtualenvs/spms-env

8. Update WSGI configuration file:
   ```python
   import os
   import sys
   from dotenv import load_dotenv
   
   # Add your project directory to the sys.path
   path = '/home/yourusername/spms'
   if path not in sys.path:
       sys.path.append(path)
   
   # Load environment variables
   load_dotenv(os.path.join(path, '.env'))
   
   # Set up Django
   os.environ['DJANGO_SETTINGS_MODULE'] = 'spms.settings'
   
   # Import Django WSGI handler
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

9. Set up static files:
   ```bash
   python manage.py collectstatic
   ```

10. Configure static files in PythonAnywhere:
    - URL: /static/
    - Directory: /home/yourusername/spms/staticfiles

11. Configure media files:
    - URL: /media/
    - Directory: /home/yourusername/spms/media

12. Create database and superuser:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

13. Reload your web app

## Usage Guide

### For Administrators
1. Access the admin interface at `/admin`
2. Create teacher accounts
3. Monitor system activity

### For Teachers
1. Log in to your account
2. Create classes and add students
3. Create projects and assignments
4. Grade submissions and provide feedback

### For Students
1. Log in to your account
2. Join classes (if not automatically added)
3. View and submit assignments
4. Track your progress and grades

## Security Features

- SSL/TLS encryption in production
- Secure password hashing
- CSRF protection
- XSS prevention
- Secure cookie handling
- Password reset functionality
- Role-based access control

## Tech Stack

- Django 5.0+
- Bootstrap 5
- Crispy Forms
- SQLite (default) / PostgreSQL (recommended for production)
- Font Awesome Icons

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- [M Hamza Mirani](https://github.com/mrerror313coder)

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Font Awesome Icons
