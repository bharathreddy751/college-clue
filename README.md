# 🎓 College Clue – Centralized College Admission Platform

College Clue is a **centralized admission and accommodation platform** that helps students explore universities, compare colleges, register for courses, and manage accommodation (PG/Hostels). Built with **Django**, it provides a smooth admission workflow for students, colleges, and hostel providers.

---

## ✨ Features

- 🔎 **University & College Listings** – Browse detailed information about universities and colleges.
- ⚖️ **Compare Colleges** – Select multiple colleges and view a side-by-side comparison.
- 🏠 **Accommodation Management** – PGs/Hostels can list and manage their facilities.
- 📝 **Student Registration** – Register with dynamic course options from the database.
- 📩 **Email Notifications** – Students receive confirmation emails after successful registration.
- 🛠️ **Admin Dashboard** – Colleges and PGs can manage their own data through Django Admin.  
- 🎉 **Modern UI Enhancements**
  - Confetti animation on registration success
  - Progress bar during form submission
 

---

## 🛠 Tech Stack

- **Backend:** Python (Django, Django REST Framework)
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite 
- **Other Tools:** dotenv

---

## 📂 Project Structure

collegeclue/ # Main project folder
│-- core/ # Main Django app<br>
│ │-- api/ # REST API (serializers, views, urls)
│ │-- migrations/ # Database migrations
│ │-- templates/ # App-specific templates (account, core, etc.)
│ │-- templatetags/ # Custom template tags
│ │-- admin.py # Django admin configuration
│ │-- apps.py # App configuration
│ │-- forms.py # Forms used in the app
│ │-- middleware.py # Custom middleware
│ │-- models.py # Database models
│ │-- urls.py # App-level URL routes
│ │-- views.py # Business logic / views
│
│--collegeclue/ # Project configuration
│ │-- settings.py # Global settings (database, installed apps, etc.)
│ │-- urls.py # Root URL mappings
│ │-- asgi.py # ASGI entry point
│ │-- wsgi.py # WSGI entry point
│ │-- templates/ # Base/global templates
│
│-- static/
│-- templates/ # Project-level templates
│-- db.sqlite3 # Default SQLite database (dev only)
│-- manage.py # Django management script
│-- importdata.py # Script to import JSON data into DB
│-- college-clue-default-rtdb-export.json # University data file
│-- .env # Environment variables (SECRET_KEY, DB, etc.)
│-- .gitignore # Files and folders ignored by Git
