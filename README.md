
# 🧒 Train-Up-A-Child – Backend (Django REST API)

### Empowering children through sponsorship

The **Train-Up-A-Child Backend** provides the secure API and data layer for the Train-Up-A-Child charity platform — connecting sponsors with children in need of educational support.

---

## 🚀 Features
- RESTful API built with **Django REST Framework**
- **JWT authentication** for secure access
- **CRUD operations** for Sponsors, Children, and Donations
- **Media uploads** for sponsor/child profiles
- **PostgreSQL** database integration
- **CORS-enabled** for seamless frontend connection
- Well-structured models, serializers, and views

---

## 🧠 Tech Stack
| Category | Tools |
|-----------|-------|
| Language | Python |
| Framework | Django, Django REST Framework |
| Database | PostgreSQL (or SQLite for dev) |
| Authentication | JWT (SimpleJWT) |
| Deployment | Render / Railway / Heroku (choose your platform) |

---

## ⚙️ Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/nkemdilimjulie/Train-Up-A-Child-Backend.git
   cd Train-Up-A-Child-Backend


Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run migrations and start the server

python manage.py migrate
python manage.py runserver


The API will be available at:

http://127.0.0.1:8000/api/

🔗 Related Repositories

Frontend (Next.js): Train-Up-A-Child-Frontend

🧪 Example API Endpoints
Endpoint	Method	Description
/api/sponsors/	GET	List all sponsors
/api/children/	GET	List all children
/api/donations/	POST	Make a donation
/api/token/	POST	Obtain JWT token
🌍 Deployment

Coming soon → Live API Link

💖 Purpose

This project is part of a real-world initiative to support educational sponsorships for children in need.
It demonstrates clean backend architecture, secure authentication, and scalable API design.

👩‍💻 Author

Julie Nkemdilim
Python Backend Developer
📧 your.email@example.com

🌐 [LinkedIn / Portfolio Link]


---
