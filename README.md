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
- ❤️ **University Wishlist** – Save favorite universities to a personal list for easy access and future reference.
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

collegeclue/ # Main project folder<br>
│-- core/ # Main Django app<br>
│ │-- api/ # REST API (serializers, views, urls)<br>
│ │-- migrations/ # Database migrations<br>
│ │-- templates/ # App-specific templates (account, core, etc.)<br>
│ │-- templatetags/ # Custom template tags<br>
│ │-- admin.py # Django admin configuration<br>
│ │-- apps.py # App configuration<br>
│ │-- forms.py # Forms used in the app<br>
│ │-- middleware.py # Custom middleware<br>
│ │-- models.py # Database models<br>
│ │-- urls.py # App-level URL routes<br>
│ │-- views.py # Business logic / views<br>
│<br>
│--collegeclue/ # Project configuration<br>
│ │-- settings.py # Global settings (database, installed apps, etc.)<br>
│ │-- urls.py # Root URL mappings<br>
│ │-- asgi.py # ASGI entry point<br>
│ │-- wsgi.py # WSGI entry point<br>
│ │-- templates/ # Base/global templates<br>
│<br>
│-- static/<br>
│-- templates/ # Project-level templates<br>
│-- db.sqlite3 # Default SQLite database (dev only)<br>
│-- manage.py # Django management script<br>
│-- importdata.py # Script to import JSON data into DB<br>
│-- college-clue-default-rtdb-export.json # University data file<br>
│-- .env # Environment variables (SECRET_KEY, DB, etc.)<br>
│-- .gitignore # Files and folders ignored by Git<br>
