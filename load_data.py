import sqlite3
import pandas as pd

# ── DATABASE CONNECTION ──────────────────────────────────
def create_connection():
    conn = sqlite3.connect("library.db")
    print("✅ Connected to SQLite database")
    return conn

# ── LOAD EXCEL DATA ──────────────────────────────────────
def load_excel_data(conn, excel_file):
    print(f"\n📂 Loading data from {excel_file}...\n")

    cursor = conn.cursor()

    # Read all sheets
    excel_data = pd.read_excel(excel_file, sheet_name=None)

    # ── BOOKS ─────────────────────────────────────────────
    books_df = excel_data['Books'].astype(str)

    for _, row in books_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO Books 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', tuple(row))

    print(f"✅ Books loaded: {len(books_df)}")

    # ── CUSTOMERS ─────────────────────────────────────────
    customer_df = excel_data['Customer'].astype(str)

    for _, row in customer_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO Customer 
            VALUES (?, ?, ?, ?)
        ''', tuple(row))

    print(f"✅ Customers loaded: {len(customer_df)}")

    # ── ISSUE STATUS ──────────────────────────────────────
    issue_df = excel_data['Issue_Status'].astype(str)

    for _, row in issue_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO Issue_Status 
            VALUES (?, ?, ?, ?, ?)
        ''', tuple(row))

    print(f"✅ Issue records loaded: {len(issue_df)}")

    # ── RETURN STATUS ─────────────────────────────────────
    return_df = excel_data['Return_Status'].astype(str)

    for _, row in return_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO Return_Status 
            VALUES (?, ?, ?, ?, ?)
        ''', tuple(row))

    print(f"✅ Return records loaded: {len(return_df)}")

    # Commit changes
    conn.commit()
    print("\n🎉 All data loaded successfully!")

# ── VERIFY DATA ──────────────────────────────────────────
def verify_data(conn):
    cursor = conn.cursor()

    tables = ["Books", "Customer", "Issue_Status", "Return_Status"]

    print("\n📊 Data Summary:")
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"➡ {table}: {count} rows")

# ── MAIN ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("📚 LIBRARY DATA LOADER (SQLite Version)")
    print("=" * 50)

    conn = create_connection()

    try:
        load_excel_data(conn, "LibraryDataset_xlsx.xlsx")
        verify_data(conn)
    except Exception as e:
        print(f"\n❌ Error: {e}")

    conn.close()
    print("\n✅ Done!")