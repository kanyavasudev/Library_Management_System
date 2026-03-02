import streamlit as st
import mysql.connector
import pandas as pd

# ── DATABASE CONNECTION ──────────────────────────────────
def get_connection():
    return mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        database=st.secrets["DB_NAME"],
        port=int(st.secrets["DB_PORT"])
    )

# ── LOAD CSS ─────────────────────────────────────────────
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ── PAGE SETTINGS ────────────────────────────────────────
st.set_page_config(page_title="Library Management System", page_icon="📚", layout="wide")
st.title("📚 Library Management System")

# ── SIDEBAR LOGO ─────────────────────────────────────────
st.sidebar.image("images/logo.png", use_column_width=True)   # 👈 put logo.png in images folder
st.sidebar.title("📋 Navigation")
menu = st.sidebar.selectbox("Choose a page", [
    "📖 View Books",
    "➕ Add Book",
    "👥 View Customers",
    "➕ Add Customer",
    "📤 Issue Book",
    "📥 Return Book",
    "📊 View Issue Records",
    "📊 View Return Records"
])

# ── BANNER HELPER FUNCTION ───────────────────────────────
def show_banner(image_name):
    import os
    path = f"images/{image_name}"
    if os.path.exists(path):
        st.image(path, width=300)

# ── 1. VIEW BOOKS ────────────────────────────────────────
if menu == "📖 View Books":
    show_banner("books.png")       # 👈 put books.png in images folder
    st.header("📖 All Books")
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Books", conn)
    conn.close()
    st.dataframe(df, use_container_width=True)

# ── 2. ADD BOOK ──────────────────────────────────────────
elif menu == "➕ Add Book":
    show_banner("add_book.png")    # 👈 put add_book.png in images folder
    st.header("➕ Add New Book")
    isbn = st.text_input("ISBN")
    title = st.text_input("Book Title")
    category = st.text_input("Category")
    price = st.number_input("Rental Price", min_value=0.0)
    status = st.selectbox("Status", ["Yes", "No"])
    author = st.text_input("Author")
    publisher = st.text_input("Publisher")

    if st.button("Add Book"):
        if isbn and title and author:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT IGNORE INTO Books VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (isbn, title, category, price, status, author, publisher)
            )
            conn.commit()
            conn.close()
            st.success("✅ Book added successfully!")
        else:
            st.error("Please fill in ISBN, Title and Author!")

# ── 3. VIEW CUSTOMERS ────────────────────────────────────
elif menu == "👥 View Customers":
    show_banner("customers.png")   # 👈 put customers.png in images folder
    st.header("👥 All Customers")
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Customer", conn)
    conn.close()
    st.dataframe(df, use_container_width=True)

# ── 4. ADD CUSTOMER ──────────────────────────────────────
elif menu == "➕ Add Customer":
    show_banner("add_customer.png") # 👈 put add_customer.png in images folder
    st.header("➕ Add New Customer")
    cust_id = st.text_input("Customer ID")
    name = st.text_input("Customer Name")
    address = st.text_input("Address")
    reg_date = st.date_input("Registration Date")

    if st.button("Add Customer"):
        if cust_id and name:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT IGNORE INTO Customer VALUES (%s, %s, %s, %s)",
                (cust_id, name, address, str(reg_date))
            )
            conn.commit()
            conn.close()
            st.success("✅ Customer added successfully!")
        else:
            st.error("Please fill in Customer ID and Name!")

# ── 5. ISSUE BOOK ────────────────────────────────────────
elif menu == "📤 Issue Book":
    show_banner("issue.png")       # 👈 put issue.png in images folder
    st.header("📤 Issue a Book")
    issue_id = st.text_input("Issue ID")
    cust_id = st.text_input("Customer ID")
    book_name = st.text_input("Book Name")
    issue_date = st.date_input("Issue Date")
    isbn = st.text_input("ISBN")

    if st.button("Issue Book"):
        if issue_id and cust_id and isbn:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT IGNORE INTO Issue_Status VALUES (%s, %s, %s, %s, %s)",
                (issue_id, cust_id, book_name, str(issue_date), isbn)
            )
            conn.commit()
            conn.close()
            st.success("✅ Book issued successfully!")
        else:
            st.error("Please fill in all required fields!")

# ── 6. RETURN BOOK ───────────────────────────────────────
elif menu == "📥 Return Book":
    show_banner("return.png")      # 👈 put return.png in images folder
    st.header("📥 Return a Book")
    return_id = st.text_input("Return ID")
    cust_id = st.text_input("Customer ID")
    book_name = st.text_input("Book Name")
    return_date = st.date_input("Return Date")
    isbn = st.text_input("ISBN")

    if st.button("Return Book"):
        if return_id and cust_id and isbn:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT IGNORE INTO Return_Status VALUES (%s, %s, %s, %s, %s)",
                (return_id, cust_id, book_name, str(return_date), isbn)
            )
            conn.commit()
            conn.close()
            st.success("✅ Book returned successfully!")
        else:
            st.error("Please fill in all required fields!")

# ── 7. VIEW ISSUE RECORDS ────────────────────────────────
elif menu == "📊 View Issue Records":
    show_banner("issue_records.png") # 👈 put issue_records.png in images folder
    st.header("📊 Issue Records")
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Issue_Status", conn)
    conn.close()
    st.dataframe(df, use_container_width=True)

# ── 8. VIEW RETURN RECORDS ───────────────────────────────
elif menu == "📊 View Return Records":
    show_banner("return_records.png") # 👈 put return_records.png in images folder
    st.header("📊 Return Records")
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Return_Status", conn)
    conn.close()
    st.dataframe(df, use_container_width=True)
