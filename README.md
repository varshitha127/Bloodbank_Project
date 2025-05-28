# 🩸 Blood Bank Management System

A web-based Blood Bank Management System built with Django that helps users find and request blood, manage donor information, and simplify blood inventory tracking. This project aims to streamline the blood donation process by providing a user-friendly platform.

---

## 🚀 Features

- 🧑‍🤝‍🧑 Register as a Donor
- 🩸 Search Available Blood Types
- 📋 Request for Blood
- 🗃️ Admin Panel for Managing Donors and Requests
- 💻 Frontend: HTML, CSS, JavaScript
- ⚙️ Backend: Django + SQLite/PostgreSQL

## 🏗️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Django (Python)   |
| Database    | SQLite (local) / PostgreSQL (Render) |
| Deployment  | Render           |

---

## 📂 Project Structure
BBMS-github/
├── mysite/                  # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── polls/                   # App: business logic and views
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/                  # Static assets (CSS, JS, images)
├── staticfiles/             # Collected static files for deployment
├── templates/               # Shared HTML templates
├── db.sqlite3               # SQLite database (local only)
├── manage.py                # Django CLI
├── render.yaml              # Render deployment configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

---

## 🚀 Deploying on Render

1. **Fork/Clone this repository**
2. **Connect your repo to [Render](https://render.com/)**
3. Render will auto-detect the `render.yaml` and set up your web service and database
4. Set the following environment variables in Render Dashboard:
    - `CLOUDINARY_CLOUD_NAME`
    - `CLOUDINARY_API_KEY`
    - `CLOUDINARY_API_SECRET`
    - `SECRET_KEY` (auto-generated or set your own)
    - `DEBUG` (set to `False` for production)
5. Deploy! Render will run migrations and collect static files automatically.

### Local Development

1. Create a `.env` file in the project root:
    ```env
    DEBUG=True
    SECRET_KEY=your-local-secret-key
    CLOUDINARY_CLOUD_NAME=your_cloud_name
    CLOUDINARY_API_KEY=your_api_key
    CLOUDINARY_API_SECRET=your_api_secret
    DATABASE_URL=sqlite:///db.sqlite3
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run migrations and start the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## 📦 Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` in production
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`: For media storage
- `DATABASE_URL`: Provided by Render for PostgreSQL, or use SQLite locally

---

## 📄 License
MIT


