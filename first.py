# This code has a deliberate vulnerability: an SQL injection vulnerability.

import sqlite3

def get_user_data(username):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    
    # Vulnerable SQL query
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    
    cursor.execute(query)
    data = cursor.fetchall()
    
    conn.close()
    
    return data

if __name__ == "__main__":
    user_input = input("Enter a username: ")
    user_data = get_user_data(user_input)
    
    if user_data:
        print("User data:", user_data)
    else:
        print("User not found.")
