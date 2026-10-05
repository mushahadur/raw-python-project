# Pharmacy Management System (PMS) 🚀

A lightweight, high-performance **Pharmacy Management System Web Application** built entirely from scratch using **Raw Python 3**. This project completely avoids high-level web frameworks like Django, Flask, or FastAPI to demonstrate core backend architecture, low-level socket handling, and pure relational database optimization.

---

## 📌 Core Features

- **Custom HTTP Server & Routing:** Implemented directly via Python's built-in `http.server` module, manually overriding `GET` and `POST` methods.
- **Dynamic Relational Querying:** Utilizes advanced SQL `JOIN` statements to securely link and retrieve relational data across `orders`, `customers`, and `medicines` tables.
- **User Authentication & Middleware:** Clean implementation of custom session/auth management via dedicated middleware and service layers.
- **Secure Data Mutations:** Server-side URL and form data parsing utilizing `urllib.parse`, completely sanitized against common vulnerabilities.
- **PRG Pattern Compliance:** Strict adherence to the **Post/Redirect/Get** workflow using `HTTP 303 See Other` redirects to mitigate duplicate form submissions.
- **Modular MVC-like Architecture:** A production-grade directory structure separating models, views (layouts), routes, and services for high maintainability.

---

## 📁 Project Structure

```text
PMS/
├── data/
│   └── schema.sql          # Complete MySQL database schema and tables
├── layouts/
│   ├── base.py             # Base HTML template rendering engine wrapper
│   ├── footer.py           # Reusable Footer view component
│   └── header.py           # Reusable Header/Navbar view component
├── middleware/
│   └── auth.py             # Request-level authentication interceptor
├── models/
│   ├── customer.py         # Customer data model class
│   ├── medicine.py         # Medicine data model class
│   ├── order.py            # Order data model class
│   └── user.py             # User data model class
├── routes/
│   ├── auth/
│   │   ├── login.py        # Login logic & request handling
│   │   ├── logout.py       # Session termination logic
│   │   └── register.py     # New user registration workflow
│   ├── customers.py        # Customer management routing
│   ├── home.py             # Dashboard / Main landing routing
│   ├── medicines.py        # Inventory / Medicine management routing
│   ├── orders.py           # Order lifecycle and sales routing
│   └── users.py            # User profile/system users routing
├── services/
│   ├── auth_service.py     # Authentication logic business rules
│   ├── db_connection.py    # Pure MySQL connector & raw query engine
│   └── pharmacy.py         # Central system service layer
├── utils/                  # Helper utilities and shared functions
└── index.py                # Main entry point (Custom HTTPServer & Master Router)
```

---

## 🛠️ Tech Stack & Concepts Covered

- **Language:** Python 3.x (Core Standard Libraries Only)
- **Networking/Web:** `http.server` (`BaseHTTPRequestHandler`, `HTTPServer`), `urllib.parse`
- **Database:** MySQL / MariaDB (Native driver interfacing without heavy ORMs)
- **Architecture:** Custom Model-View-Controller (MVC) with specialized Service and Middleware layers.

---

## 🚀 Installation & Setup Guide

Follow these sequential steps to clone, configure, and execute the application in your local development environment:

### 1. Prerequisites
Ensure you have the following dependencies natively installed on your system:
* **Python 3.10+**
* **MySQL Server** 

### 2. Clone the Repository
Open your terminal or command prompt and clone the workspace:
```bash
git clone https://github.com[your-github-username]/PMS.git
cd PMS
```

### 3. Install Required Database Driver
While the project is framework-free, Python requires a low-level native driver to communicate with the MySQL server. Install the official package using pip:
```bash
pip install mysql-connector-python
```

### 4. Database Schema Setup
* Log into your local MySQL CLI or GUI client (e.g., phpMyAdmin, DBeaver) and create an empty database named `pms_db` (or a name of your choice).
* Import and execute the SQL script located at `data/schema.sql` to generate all transactional and relationship configurations, including the relational integrity keys for the orders flow:

```sql
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    medicine_id INT NOT NULL,
    customer_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (medicine_id) REFERENCES medicines(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

### 5. Configure Credentials
Navigate to `services/db_connection.py` and modify the environment configuration variables (`host`, `user`, `password`, `database`) to match your local database authentication credentials.

### 6. Launch the Local Web Server
With the configuration complete, boot the multi-threaded custom server instance:
```bash
python3 index.py
```
Once initialized, open any standard web browser and proceed to the following address:
👉 `http://127.0.0.1:8000` *(or the custom port value configured inside your index.py).*

---

## 💡 What I Learned from Building the "Raw Wheel"

Building a web app without an abstraction framework forces you to understand **how things actually work under the hood**. Key takeaways from this project include:
1. **Network Primitives:** Understanding how raw TCP socket streams translate into readable, stateful HTTP context streams.
2. **State Contexts & Middleware:** Structuring stateless HTTP request lifecycles to systematically parse and validate user authentication bounds before routing execution blocks.
3. **Data Integrity:** Managing exact raw tuple indexing data properties (`o[0]`, `o[1]`) extracted from low-level database operations straight into explicit modular model parameters.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
