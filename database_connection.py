import mysql.connector
import pandas as pd

def create_connection():
    """Connect to MySQL database"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kanya#005",  # ⚠️ CHANGE THIS
            database="library_management"
        )
        print("✅ Connected to database successfully!")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None

def load_excel_data(conn, excel_file):
    """Load data from Excel into MySQL"""
    
    print(f"\nLoading data from {excel_file}...")
    cursor = conn.cursor()
    
    # Read Excel file (all sheets)
    excel_data = pd.read_excel(excel_file, sheet_name=None)
    
    # Load Books
    books_df = excel_data['Books']
    for _, row in books_df.iterrows():
        cursor.execute('''
            INSERT IGNORE INTO Books 
            (ISBN, Book_title, Category, Rental_Price, Status, Author, Publisher)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', tuple(row))
    print(f"  ✅ Loaded {len(books_df)} books")
    
    # Load Customers
    customer_df = excel_data['Customer']
    for _, row in customer_df.iterrows():
        cursor.execute('''
            INSERT IGNORE INTO Customer 
            (Customer_Id, Customer_name, Customer_address, Reg_date)
            VALUES (%s, %s, %s, %s)
        ''', tuple(row))
    print(f"  ✅ Loaded {len(customer_df)} customers")
    
    # Load Branches (MUST load before Employees)
    branch_df = excel_data['Branch']
    for _, row in branch_df.iterrows():
        cursor.execute('''
            INSERT IGNORE INTO Branch 
            (Branch_no, Manager_id, Branch_address, Contact_no)
            VALUES (%s, %s, %s, %s)
        ''', tuple(row))
    print(f"  ✅ Loaded {len(branch_df)} branches")
    
    # Load Employees
    employee_df = excel_data['Employee']
    for _, row in employee_df.iterrows():
        cursor.execute('''
            INSERT IGNORE INTO Employee 
            (Emp_id, Emp_name, Position, Salary, branch_no)
            VALUES (%s, %s, %s, %s, %s)
        ''', tuple(row))
    print(f"  ✅ Loaded {len(employee_df)} employees")
    
    # Load Issue_Status
    issue_df = excel_data['Issue_Status']
    for _, row in issue_df.iterrows():
        cursor.execute('''
            INSERT IGNORE INTO Issue_Status 
            (Issue_Id, Issued_cust, Issued_book_name, Issue_date, Isbn_book)
            VALUES (%s, %s, %s, %s, %s)
        ''', tuple(row))
    print(f"  ✅ Loaded {len(issue_df)} issue records")
    
    # Load Return_Status
    return_df = excel_data['Return_Status']
    for _, row in return_df.iterrows():
        cursor.execute('''
            INSERT IGNORE INTO Return_Status 
            (Return_id, Return_cust, Return_book_name, Return_date, isbn_book2)
            VALUES (%s, %s, %s, %s, %s)
        ''', tuple(row))
    print(f"  ✅ Loaded {len(return_df)} return records")
    
    conn.commit()
    print("\n✅ All data loaded successfully!")

if __name__ == "__main__":
    print("="*50)
    print("LIBRARY MANAGEMENT SYSTEM - DATA LOADER")
    print("="*50)
    
    # Connect to database
    conn = create_connection()
    
    if conn:
        # Load data from Excel
        excel_file = 'LibraryDataset_xlsx.xlsx'
        load_excel_data(conn, excel_file)
        
        # Verify data
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Books")
        print(f"\nTotal books in database: {cursor.fetchone()[0]}")
        
        conn.close()
        print("\n✅ Data loading complete!")
    else:
        print("❌ Failed to connect to database")