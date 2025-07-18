# 🧠 Online Test App

> A powerful and secure **Online Test Platform** built using the **Django** framework.  
> Designed to help students assess their knowledge, track performance, and enhance skills across a versatile set of domains.  
> Admins can efficiently manage tests, users, and results through a built-in dashboard.

🗓️ Duration: **Jan 2024 – Mar 2024**

---

## 📌 Features

### 🔐 Login Authentication
- Secure user login using Django's authentication system.
- Ensures role-based access for students and admins.

### 🔍 Plagiarism Detection
- Detects **tab switching** and monitors suspicious activities during the test.
- Helps maintain test integrity.

### 🧊 Freeze Window During Test
- Disables user navigation and interactions outside the test window once the test starts.

### 📈 Performance Tracking
- Stores and displays performance history of each user.
- Helps users monitor their improvement over time.

### 📊 Recent Activity Table
- Shows a detailed **table of recent scores and test attempts**.
- Useful for both users and admins.

### 🧪 Domain Versatility
- Wide variety of test domains (e.g., Data Structures, Aptitude, Web, DBMS, etc.).
- Allows users to focus and improve on a specific topic.

### 🗂️ Easy Data Management
- Built-in support for database models with Django ORM.
- Simplifies data handling, updates, and queries.

### ⚙️ Admin Panel
- Django's built-in **admin interface** for:
  - Managing users
  - Uploading questions
  - Viewing results
  - Domain and category management

---

## ⚙️ Tech Stack

| Technology      | Description                           |
|-----------------|---------------------------------------|
| **Python**      | Programming Language                  |
| **Django**      | Web Framework                         |
| **SQLite**      | Default Django database               |
| **HTML/CSS**    | Frontend Markup & Styling             |
| **JavaScript**  | For dynamic tab-switch detection      |
| **Bootstrap**   | For responsive UI (optional)          |

---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/online-test-app.git
cd online-test-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver
