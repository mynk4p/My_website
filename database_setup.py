import sqlite3

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('/home/mynk4p/mysite/portfolio.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);
''')

# Create the transactions table with a new 'type' column
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    type TEXT NOT NULL,  -- Can be 'deposit' or 'withdrawal'
    amount REAL NOT NULL,
    units REAL NOT NULL,
    nav_at_transaction REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
''')

# Create the portfolio_log table to track total value
cursor.execute('''
CREATE TABLE IF NOT EXISTS portfolio_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    total_portfolio_value REAL NOT NULL
);
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")