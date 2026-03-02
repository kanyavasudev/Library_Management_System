# 📚 Library Management System

A web-based Library Management System built with **Python**, **Streamlit**, and **MySQL**. This app allows you to manage books, customers, employees, branches, and track book issues and returns through an interactive UI.

---

## 🚀 Live Demo

🔗 [View the App](https://library-management-kanya.streamlit.app)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Backend logic |
| Streamlit | Web UI |
| MySQL | Database |
| Railway | Cloud database hosting |
| Streamlit Cloud | App deployment |

---

## ✨ Features

- 📖 View all books
- ➕ Add new books and customers
- 👥 View all customers
- 📤 Issue books to customers
- 📥 Return books
- 📊 View issue and return records

---

## 🗄️ Database Tables

The system uses the following MySQL tables:

### Books
| Column | Type |
|--------|------|
| ISBN | VARCHAR(20) PK |
| Title | VARCHAR(100) |
| Category | VARCHAR(50) |
| Rental_Price | DECIMAL(10,2) |
| Status | VARCHAR(5) |
| Author | VARCHAR(100) |
| Publisher | VARCHAR(100) |

### Customer
| Column | Type |
|--------|------|
| Customer_Id | VARCHAR(20) PK |
| Customer_Name | VARCHAR(100) |
| Customer_Address | VARCHAR(200) |
| Reg_Date | DATE |

### Branch
| Column | Type |
|--------|------|
| Branch_no | VARCHAR(10) PK |
| Manager_id | VARCHAR(10) |
| Branch_address | VARCHAR(100) |
| Contact_no | BIGINT |

### Employee
| Column | Type |
|--------|------|
| Emp_id | VARCHAR(10) PK |
| Emp_name | VARCHAR(100) |
| Position | VARCHAR(50) |
| Salary | DECIMAL(10,2) |
| Branch_no | VARCHAR(10) |

### Issue_Status
| Column | Type |
|--------|------|
| Issue_Id | VARCHAR(20) PK |
| Issued_Cust | VARCHAR(20) |
| Issued_Book_Name | VARCHAR(100) |
| Issue_Date | DATE |
| Isbn_Book | VARCHAR(20) |

### Return_Status
| Column | Type |
|--------|------|
| Return_Id | VARCHAR(20) PK |
| Return_Cust | VARCHAR(20) |
| Return_Book_Name | VARCHAR(100) |
| Return_Date | DATE |
| Isbn_Book2 | VARCHAR(20) |

---

## ☁️ Cloud Database Setup (Railway)

1. Go to [railway.app](https://railway.app) and sign up with GitHub
2. Create a new project → **Database** → **MySQL**
3. Once deployed, go to **Variables** tab to get your credentials
4. Connect using **MySQL Workbench**:
   - Host: `your-railway-host`
   - Port: `your-railway-port`
   - Username: `root`
   - Password: `your-railway-password`
5. Create all tables and insert your data using MySQL Workbench

---

## 💻 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/kanyavasudev/Library_Management_System.git
cd Library_Management_System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Update database connection in `library_app.py`
```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="library_management"
    )
```

### 4. Run the app
```bash
streamlit run library_app.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Go to **Settings → Secrets** and add:

```
DB_HOST = "your-railway-host"
DB_USER = "root"
DB_PASSWORD = "your-railway-password"
DB_NAME = "railway"
DB_PORT = "your-port"
```

4. Update `get_connection()` to use secrets:

```python
def get_connection():
    return mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        database=st.secrets["DB_NAME"],
        port=int(st.secrets["DB_PORT"])
    )
```

---

## 📁 Project Structure

```
Library_Management_System/
│
├── library_app.py        # Main Streamlit application
├── style.css             # Custom CSS styling
├── requirements.txt      # Python dependencies
└── images/               # Banner images for UI
```

---

## 📦 Requirements

```
streamlit
mysql-connector-python
pandas
```

---

## 👩‍💻 Author 
GitHub: [@kanyavasudev](https://github.com/kanyavasudev)