# 📝 Django Blog App

A full-featured blogging platform with user authentication, category-based content management, comments, and a custom admin dashboard. Built with Django and Bootstrap.

---

## 📌 Overview

This project is a complete, monolithic web application that provides:

- A public blog portal for readers to browse, search, and comment on articles.
- A custom admin dashboard for content creators to manage posts, categories, and site settings.
- Built-in deployment support (Procfile, Gunicorn, Whitenoise) for production hosting.

---

## ✨ Features

- **User Authentication:** Registration, login, logout, and role-based access.
- **Blog & Content Management:** Create, edit, draft/publish posts, attach featured images, and organize by categories.
- **Interactivity:** User comment system and live search (by title & content).
- **Admin Dashboard:** Custom dashboard (`/dashboard/`) to manage posts, categories, comments, and social links.
- **Responsive UI:** Clean Bootstrap-based interface.

---

## 🛠️ Tech Stack

- **Framework:** Django 6.0
- **Frontend:** HTML5, CSS3, Bootstrap 4, Django Crispy Forms
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Static & Media Handling:** Whitenoise, Pillow
- **WSGI Server:** Gunicorn

---

## 📂 Project Structure

```text
Blog app/
├── blog_main/        # Core project settings & global routes
├── blogs/            # Blog posts, categories, and comments app
├── dashboards/       # Admin dashboard app
├── assignments/      # Site info & social links app
├── templates/        # HTML templates (base, blogs, dashboard)
├── static/           # Static assets (CSS, JS, images)
├── media/            # User-uploaded images
├── requirements.txt  # Project dependencies
├── Procfile          # Deployment configuration
└── manage.py         # Django CLI tool

1.Clone & Activate Environment

# Navigate to directory
cd "Blog app"

# Create virtual environment
python -m venv env

# Activate environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

2. Install Dependencies & Database Setup
# Install required packages
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

3. Run Application

python manage.py runserver

# Environment Configuration
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```
