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
- **Database**: SQLite (default) / MySQL 8.0 (Docker)
- **Containerization**: Docker & Docker Compose

## Installation & Setup

### Option 1: Docker (Recommended)

1. **Clone the repository**
```bash
git clone <repository-url>
cd dj-daynotes-app
```

2. **Create environment file**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

3. **Run with Docker Compose**
```bash
docker-compose up -d
```

4. **Run migrations**
```bash
docker-compose exec daynotes-app python manage.py migrate
```

5. **Create superuser (optional)**
```bash
docker-compose exec daynotes-app python manage.py createsuperuser
```

### Option 2: Local Development

1. **Clone the repository**
```bash
git clone <repository-url>
cd dj-daynotes-app
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

### Access the Application
- Web Interface: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Application Structure

```
dj-daynotes-app/
├── daynotes/                 # Main Django app
│   ├── templates/           # HTML templates
│   ├── static/             # CSS files
│   ├── models.py           # Note model
│   ├── views.py            # Web views
│   └── urls.py             # URL patterns
├── daynotes_project/       # Django project settings
├── docker-compose.yml      # Docker services configuration
├── Dockerfile              # Docker image definition
├── .env.example            # Environment variables template
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

## Docker Usage

### Environment Variables
Create a `.env` file with the following variables:
```
MYSQL_DATABASE=daynotes_db
MYSQL_USER=daynotes_user
MYSQL_PASSWORD=your_password
MYSQL_ROOT_PASSWORD=root_password
SECRET_KEY=your_django_secret_key
DB_NAME=daynotes_db
DB_USER=daynotes_user
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=3306
DEBUG=False
```

### Generate Django Secret Key
For new users, generate a secure Django secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Or use this example key for development:
```
SECRET_KEY=django-insecure-example-key-change-in-production-abc123xyz789
```

### Docker Commands
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and start
docker-compose up --build -d

# Execute Django commands
docker-compose exec daynotes-app python manage.py <command>
```

### Database
- **Production**: MySQL 8.0 (via Docker)
- **Development**: SQLite (local setup)
- **Port**: 3306 (MySQL)
- **Health checks**: Automatic MySQL readiness verification