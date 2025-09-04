# Django GraphQL Project

A Django-based GraphQL API for managing books using Graphene Django.

## 📋 Project Overview

This project provides a GraphQL API for book management with the following features:
- Query all books or individual books by ID
- Create new books via GraphQL mutations
- CORS support for frontend integration
- SQLite3 database (default)

## 🚨 Important: SQLite3 Issue & Solutions

### The Problem

If you encounter this error when running Django commands:
```
ModuleNotFoundError: No module named '_sqlite3'
```

This happens because Python was compiled without SQLite3 support. This is common with Python version managers like `asdf`, `pyenv`, or manual compilations.

### Root Cause

The `_sqlite3` module is a C extension that must be compiled when Python is built. If SQLite3 development libraries aren't available during Python compilation, this module won't be included.

### Solutions

Choose one of the following solutions:

#### Solution 1: Use System Python (Quick Fix) ✅ Recommended for immediate use

```bash
# Install required system packages
sudo apt update
sudo apt install -y sqlite3 libsqlite3-dev python3-venv

# Create virtual environment with system Python
/usr/bin/python3 -m venv myenv_system
source myenv_system/bin/activate

# Install dependencies
pip install django django-cors-headers graphene_django

# Run migrations and start server
python manage.py migrate
python manage.py runserver 8001
```

#### Solution 2: Reinstall Python with SQLite3 Support (Long-term fix)

If you're using `asdf`:

```bash
# Install SQLite3 development libraries FIRST
sudo apt install -y libsqlite3-dev libssl-dev zlib1g-dev \
                    libbz2-dev libreadline-dev libncurses5-dev

# Reinstall Python (will now include SQLite3)
asdf uninstall python 3.11.9
asdf install python 3.11.9

# Create virtual environment
python -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install django django-cors-headers graphene_django

# Run migrations and start server
python manage.py migrate
python manage.py runserver
```

#### Solution 3: Use Alternative Database

Modify `core/settings.py` to use PostgreSQL or MySQL:

```python
# For PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ with SQLite3 support
- pip and venv

### Installation Steps

1. **Clone and navigate to the project:**
   ```bash
   cd /path/to/graphql
   ```

2. **Create virtual environment:**
   ```bash
   # Using system Python (recommended for SQLite3 compatibility)
   /usr/bin/python3 -m venv myenv_system
   source myenv_system/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django django-cors-headers graphene_django
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Main site: http://localhost:8000
   - GraphQL endpoint: http://localhost:8000/graphql/

## 📁 Project Structure

```
graphql/
├── core/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py      # Main settings file
│   ├── urls.py          # URL routing
│   └── wsgi.py
├── books/               # Books app
│   ├── models/
│   │   └── books.py     # Book model definition
│   ├── migrations/      # Database migrations
│   ├── schema.py        # GraphQL schema definition
│   ├── urls.py          # App URL routing
│   └── views.py         # GraphQL view
├── manage.py            # Django management script
├── db.sqlite3           # SQLite database (created after migrations)
└── README.md            # This file
```

## 🔧 GraphQL API Usage

### Schema Overview

The API provides:
- **Query**: Fetch books
- **Mutation**: Create books

### Example Queries

#### Get all books:
```graphql
query {
  allBooks {
    id
    title
    author
    publishedDate
    date
  }
}
```

#### Get a specific book:
```graphql
query {
  book(id: 1) {
    id
    title
    author
    publishedDate
    date
  }
}
```

### Example Mutations

#### Create a new book:
```graphql
mutation {
  createBook(
    title: "Django for Beginners"
    author: "William S. Vincent"
    publishedDate: "2023-01-15"
    date: "2023-01-15"
  ) {
    book {
      id
      title
      author
      publishedDate
      date
    }
  }
}
```

## 🗃️ Database Model

### Books Model

```python
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    published_date = models.DateField()
```

## 🛠️ Development

### Adding New Features

1. **Create new models** in `books/models/`
2. **Update GraphQL schema** in `books/schema.py`
3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Testing

```bash
# Run tests
python manage.py test

# Check for issues
python manage.py check
```

## 🔍 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named '_sqlite3'**
   - See the "SQLite3 Issue & Solutions" section above

2. **Port already in use**
   ```bash
   # Kill process using port 8000
   sudo lsof -t -i tcp:8000 | xargs kill -9
   
   # Or use a different port
   python manage.py runserver 8001
   ```

3. **Migration errors**
   ```bash
   # Reset migrations if needed
   python manage.py migrate books zero
   python manage.py migrate
   ```

### Testing SQLite3 Support

To verify if your Python has SQLite3 support:

```bash
python -c "import sqlite3; print('SQLite3 is available')"
```

If this fails, follow Solution 1 or 2 from the SQLite3 section above.

## 🌐 CORS Configuration

The project is configured to allow all origins for development:

```python
# In settings.py
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["GET", "POST", "OPTIONS"]
```

For production, configure specific origins:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React default
    "http://127.0.0.1:3000",
]
```

## 📝 Dependencies

Current dependencies:
- `django>=4.2.24` - Web framework
- `django-cors-headers>=4.4.0` - CORS handling
- `graphene-django>=3.2.3` - GraphQL integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Note**: This README addresses the common SQLite3 compilation issue that occurs with Python version managers. Always ensure SQLite3 development libraries are installed before compiling Python for the best experience.