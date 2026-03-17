import streamlit as st
import sqlite3
import pandas as pd
import os

# ── DATABASE CONNECTION ──────────────────────────────────
def get_connection():
    return sqlite3.connect("library.db", check_same_thread=False)

# ── CREATE TABLES IF NOT EXISTS ──────────────────────────
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        isbn TEXT PRIMARY KEY,
        title TEXT,
        category TEXT,
        price REAL,
        status TEXT,
        author TEXT,
        publisher TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer (
        cust_id TEXT PRIMARY KEY,
        name TEXT,
        address TEXT,
        reg_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Issue_Status (
        issue_id TEXT PRIMARY KEY,
        cust_id TEXT,
        book_name TEXT,
        issue_date TEXT,
        isbn TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Return_Status (
        return_id TEXT PRIMARY KEY,
        cust_id TEXT,
        book_name TEXT,
        return_date TEXT,
        isbn TEXT
    )
    """)

    conn.commit()
    conn.close()

create_tables()

# ── LOAD CSS ─────────────────────────────────────────────
def load_css():
    if os.path.exists("style.css"):
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ── PAGE SETTINGS ────────────────────────────────────────
st.set_page_config(page_title="Library Management System", page_icon="📚", layout="wide")
st.title("📚 Library Management System")

# ── SIDEBAR ──────────────────────────────────────────────
if os.path.exists("images/logo.png"):
    st.sidebar.image("images/logo.png")

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

# ── BANNER FUNCTION ──────────────────────────────────────
def show_banner(image_name):
    path = f"images/{image_name}"
    if os.path.exists(path):
        st.image(path, width=300)

# ── VIEW BOOKS ───────────────────────────────────────────
if menu == "📖 View Books":
    show_banner("books.png")
    st.header("📖 All Books")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Books", conn)
    conn.close()

    st.dataframe(df, use_container_width=True)

# ── ADD BOOK ─────────────────────────────────────────────
elif menu == "➕ Add Book":
    show_banner("add_book.png")
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
                "INSERT OR IGNORE INTO Books VALUES (?, ?, ?, ?, ?, ?, ?)",
                (isbn, title, category, price, status, author, publisher)
            )

            conn.commit()
            conn.close()

            st.success("✅ Book added successfully!")
        else:
            st.error("Please fill ISBN, Title, Author!")

# ── VIEW CUSTOMERS ───────────────────────────────────────
elif menu == "👥 View Customers":
    show_banner("customers.png")
    st.header("👥 All Customers")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Customer", conn)
    conn.close()

    st.dataframe(df, use_container_width=True)

# ── ADD CUSTOMER ─────────────────────────────────────────
elif menu == "➕ Add Customer":
    show_banner("add_customer.png")
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
                "INSERT OR IGNORE INTO Customer VALUES (?, ?, ?, ?)",
                (cust_id, name, address, str(reg_date))
            )

            conn.commit()
            conn.close()

            st.success("✅ Customer added successfully!")
        else:
            st.error("Fill required fields!")

# ── ISSUE BOOK ───────────────────────────────────────────
elif menu == "📤 Issue Book":
    show_banner("issue.png")
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
                "INSERT OR IGNORE INTO Issue_Status VALUES (?, ?, ?, ?, ?)",
                (issue_id, cust_id, book_name, str(issue_date), isbn)
            )

            conn.commit()
            conn.close()

            st.success("✅ Book issued successfully!")
        else:
            st.error("Fill required fields!")

# ── RETURN BOOK ──────────────────────────────────────────
elif menu == "📥 Return Book":
    show_banner("return.png")
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
                "INSERT OR IGNORE INTO Return_Status VALUES (?, ?, ?, ?, ?)",
                (return_id, cust_id, book_name, str(return_date), isbn)
            )

            conn.commit()
            conn.close()

            st.success("✅ Book returned successfully!")
        else:
            st.error("Fill required fields!")

# ── VIEW ISSUE RECORDS ───────────────────────────────────
elif menu == "📊 View Issue Records":
    show_banner("issue_records.png")
    st.header("📊 Issue Records")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Issue_Status", conn)
    conn.close()

    st.dataframe(df, use_container_width=True)

# ── VIEW RETURN RECORDS ──────────────────────────────────
elif menu == "📊 View Return Records":
    show_banner("return_records.png")
    st.header("📊 Return Records")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Return_Status", conn)
    conn.close()

    st.dataframe(df, use_container_width=True)