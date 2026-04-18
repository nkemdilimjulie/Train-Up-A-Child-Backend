
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

# In Development Stage:
Because of Stripe Payment, **RUN** the code in three terminals or use frontend to test:

1) Start Backend code using **python manage.py runserver** and let it run
2) Start Stripe CLI using **stripe listen --forward-to localhost:8000/api/donations/webhook/**
3) Test Stripe payment using **stripe trigger checkout.session.completed**

> Then check python/backend terminal, no. 1 above, for EXPECTED RESULT

You should now see:

✔ no server crash
✔ webhook 200 OK
✔ Donation created in DB
✔ correct amount stored

Or, use frontend:
Do this:

Open your frontend
Enter amount
Click donate
Complete Stripe checkout (test card)
---
      As of today (18.04.2026)
🎉 BIG milestone (don’t underestimate this)

You now have:

✔ Real Stripe Checkout
✔ Secure webhook handling
✔ No fake donations
✔ No crashes
✔ Backend ready for real payments

👉 This is already production-level payment architecture

⚠️ One thing still missing (important)

Right now:

user = None
sponsor = None

Because:

👉 Stripe test trigger does NOT include metadata

🚀 NEXT UPGRADE (this is the real one)

Now we connect:

👉 your frontend donation → Stripe → webhook → correct user/sponsor
---
## NEXT STEP
+ chatGPT: Turning AI into expert --> 4 — Backend endpoint (Django view, caching + DB logic)

## AI FAQs - project data
> see FAQs items in app_faq