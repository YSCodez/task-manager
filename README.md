### Task Allocation Management System
A Django-based web application for managing tasks. The system allows users to add, view, edit, and delete tasks. Tasks can be marked as completed or left pending.

### Features
- Add new tasks with descriptions.
- View a list of tasks with timestamps.
- Edit existing tasks.
- Delete tasks from the list.
- Status of tasks (Pending/Completed).
- Technologies Used
- Backend: Django
- Frontend: Bootstrap, HTML, CSS
- Database: SQLite (default for Django, can be changed to other databases)
- Python: 3.x

### Setup
## Prerequisites
- Python 3.x
- Django
- Bootstrap (included via CDN in templates)

### Installation
1. Clone the Repository
```bash
git clone task-manager
cd task-manager
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Apply Migrations
```bash
python manage.py migrate
```
or
```bash
python3 manage.py migrate
```

4. Create a Superuser (Optional, for admin access)
```bash
python manage.py createsuperuser
```
or
```bash
python3 manage.py createsuperuser
```

5. Run the Development Server
```bash
python manage.py runserver
```
or
```bash
python3 manage.py runserver
```
