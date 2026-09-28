# University Management System API

A robust backend API built with Django and Django REST Framework (DRF) designed to solve real-world scalability and concurrency challenges in academic systems. 

Unlike standard CRUD applications, this project focuses on high-traffic read optimizations and transaction safety during concurrent write operations.

## 🚀 Key Features

*   **Role-Based Access Control (RBAC):** Custom user models supporting distinct roles (`Admin`, `Professor`, `Student`) with tailored permission classes across different API endpoints.
*   **Result Day Crash Prevention (Caching):** Integrates **Redis** caching to serve student results instantly. This prevents database overload and server crashes during massive spikes in read-heavy traffic on result announcement days.
*   **Concurrent Enrollment Safety (Pessimistic Locking):** Solves the "race condition" problem where multiple students attempt to claim the last available seat in a class simultaneously. Uses database row-level locking (`select_for_update`) and atomic transactions to ensure capacity limits are strictly respected.
*   **Secure Authentication:** Token-based or session-based authentication securing all student and staff endpoints.

## 🛠️ Technology Stack

*   **Framework:** Django & Django REST Framework (DRF)
*   **Database:** PostgreSQL (Recommended for robust `select_for_update` row-locking support)
*   **Caching:** Redis
*   **Language:** Python 3.x

## 🗄️ Database Schema Overview

The database is kept intentionally simple to focus on architectural scaling. Core entities include:

1.  **User:** Inherits from Django's `AbstractUser`, adding a `role` field.
2.  **Course:** Tracks course details, assigned professor, and strict capacity limits (enforced via Django Validators).
3.  **Enrollment:** Bridge table managing the Many-to-Many relationship between Students and Courses.
4.  **Result:** Stores final grades, which are pre-loaded into the Redis cache prior to Result Day.

## ⚙️ Local Setup & Installation

### Prerequisites
*   Python 3.8+
*   Redis server running locally

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/university-management-api.git
   cd university-management-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your database and Redis credentials.

5. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## 📝 Usage

*   **Admin:** Can create courses, assign professors, and manage users.
*   **Professor:** Can view their assigned courses and publish results.
*   **Student:** Can browse courses, enroll (safely limited by capacity), and view cached results.
