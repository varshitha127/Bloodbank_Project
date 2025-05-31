# 🩸 Blood Bank Management System

[![Django](https://img.shields.io/badge/Django-3.2-brightgreen.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy on Render](https://img.shields.io/badge/Deploy%20on-Render-00AD9C)](https://render.com)

A web–based Blood Bank Management System built with Django that helps users find and request blood, manage donor information, and simplify blood inventory tracking. This project aims to streamline the blood donation process by providing a user–friendly platform.

---

## 📋 Demo

**Demo (Live):** [Demo Link (https://bloodbank-project.onrender.com/
)]

*(Demo screenshot)*
 ![Screenshot 2025-05-31 111909](https://github.com/user-attachments/assets/22870603-94f4-47ec-af75-c205659ca706)
 
![Screenshot 2025-05-31 111933](https://github.com/user-attachments/assets/cb067d05-ac21-4d9e-86c4-d7372adf666d)

![Screenshot 2025-05-31 111944](https://github.com/user-attachments/assets/a827ccb1-2ac6-4b18-8a51-cfb6ac8594d0)

![Screenshot 2025-05-31 112005](https://github.com/user-attachments/assets/4af1fd09-5a6b-419a-84da-34fa1ac99ba6)

![Screenshot 2025-05-31 112029](https://github.com/user-attachments/assets/eedb93e9-c7d1-4521-9785-535d84c44601)

---

## 🚀 Features

- 🧑‍🤝‍🧑 Register as a Donor
- 🩸 Search Available Blood Types
- 📋 Request for Blood
- 🗃️ Admin Panel for Managing Donors and Requests
- 💻 Frontend: HTML, CSS, JavaScript
- ⚙️ Backend: Django (Python) + SQLite (local) / PostgreSQL (Render)

---

## 🏗️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Django (Python)   |
| Database    | SQLite (local) / PostgreSQL (Render) |
| Deployment  | Render (via render.yaml) |

---

## 📂 Project Structure

```
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
```

---

## 🚀 Deploying on Render

1. **Fork/Clone this repository**
2. **Connect your repo to [Render](https://render.com/)**
3. Render will auto–detect the `render.yaml` and set up your web service and database.
4. Set the following environment variables in Render Dashboard:
    - `CLOUDINARY_CLOUD_NAME`
    - `CLOUDINARY_API_KEY`
    - `CLOUDINARY_API_SECRET`
    - `SECRET_KEY` (auto–generated or set your own)
    – `DEBUG` (set to `False` for production)
5. Deploy! Render will run migrations and collect static files automatically.

---

## 🛠️ Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/varshitha127/Bloodbank_Project.git
   cd Bloodbank_Project
   ```
2. **Create a `.env` file in the project root (for local environment variables):**
   ```env
   DEBUG=True
   SECRET_KEY=your-local-secret-key
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret
   DATABASE_URL=sqlite:///db.sqlite3
   ```
3. **Install dependencies:**
   ```bash
   pip install –r requirements.txt
   ```
4. **Run migrations and start the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## 📦 Environment Variables

- **SECRET_KEY:** Django secret key (auto–generated on Render or set locally)
- **DEBUG:** Set to `False` in production (Render) or `True` locally
- **CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET:** For media storage (Cloudinary)
- **DATABASE_URL:** Provided by Render (PostgreSQL) or use SQLite locally

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a new branch (e.g., `git checkout –b feature/your-feature`), commit your changes, and then push your branch (e.g., `git push origin feature/your-feature`). Then, open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.


