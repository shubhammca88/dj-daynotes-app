# Daynotes App - Django Web Application

A clean, responsive daynotes application built with Django and Bootstrap 5.

## Features

- 📝 Create, read, update, and delete notes
- 🎨 Modern Bootstrap 5 UI with responsive design
- 📱 Mobile-friendly interface
- 🔍 Clean dashboard with note previews
- 📊 Admin interface for note management

## Technology Stack

- **Backend**: Django 4.1.5
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.0.0
- **Database**: SQLite

## Installation & Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd django-notes-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the application**
- Web Interface: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Application Structure

```
daynotes-app/
├── daynotes/                 # Main Django app
│   ├── templates/           # HTML templates
│   ├── static/             # CSS files
│   ├── models.py           # Note model
│   ├── views.py            # Web views
│   └── urls.py             # URL patterns
├── daynotes_project/       # Django project settings
└── manage.py               # Django management script
```

## Web Interface Routes

| Route | Description |
|-------|-------------|
| `/` | Dashboard (redirects to `/daynotes/`) |
| `/daynotes/` | Main dashboard |
| `/daynotes/create/` | Create new note |
| `/daynotes/note/{id}/` | View note details |
| `/daynotes/edit/{id}/` | Edit note |
| `/daynotes/delete/{id}/` | Delete note confirmation |

## Features Overview

### Dashboard
- Clean, card-based layout showing all notes
- Quick actions: View, Edit, Delete
- Responsive grid layout
- Empty state with call-to-action

### Note Management
- Title and content fields
- Timestamps for creation and updates
- Confirmation dialogs for deletions

### Admin Interface
- Full CRUD operations
- Search and filter capabilities
- List view with key information