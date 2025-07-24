
# 🌟 Star Events – Event Management Web App (Django)

Welcome to **Star Events**, a fully functional event management system built with **Django**. This project allows users to explore event listings, book services, manage authentication (signup/login), and more.

---

## ✨ Features

- ✅ **Responsive Homepage** with background image and intro
- 📋 **Event listing** page with image, title, and description
- 📅 **Booking system** for events with form validation
- 👤 **User Authentication** (Signup, Login, Logout)
- 🔒 **Password Reset** and manual password update option
- 📬 **Contact page** for inquiries
- 🧾 **About page** for company details
- 🖼️ Admin support for adding/editing events
- 📎 Logo, custom navbar/footer, form styling
- 📄 Styled PDF (optional use for documentation)
- 🔁 Toast/pop-up message after actions like booking

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.x (Python 3.13+)
- **Frontend**: HTML, CSS, Bootstrap 3
- **Database**: SQLite (default)
- **Other**:
  - Django Messages Framework
  - Django Template Language
  - PyMuPDF (for PDF tweaks if needed)

---

## 🧪 How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/your-username/star-events.git
cd star-events
```

2. **Create & activate a virtual environment**

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000` to explore the app!

---

## 🧑‍💻 Admin Access

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

---

## 📁 Project Structure

```
eventmanager/
│
├── eventapp/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templatetags/
│
├── manage.py
└── db.sqlite3
```

---

## 📸 Screenshots

> Include screenshots of homepage, event page, booking form, login/signup pages, and admin panel here for better presentation.

---

## 📬 Contact

Feel free to reach out for collaboration or questions:

- 📧 gowri@example.com *(replace with your email)*
- 🌐 [LinkedIn](https://www.linkedin.com/in/yourprofile) *(optional)*
- 💻 Portfolio: [your-portfolio.com](https://your-portfolio.com) *(optional)*

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).
