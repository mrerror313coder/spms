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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spms.git
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

## Usage

1. Access the admin interface at `/admin` to manage users and content
2. Create classes and add students
3. Create projects and assign them to classes
4. Students can submit their work through the platform
5. Teachers can grade submissions and provide feedback

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

- Your Name

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Font Awesome Icons
