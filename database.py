import sqlite3
con = sqlite3.connect('database.db', check_same_thread=False)

cur = con.cursor()
'''
cur.execute("""
        CREATE TABLE "User" ( 
            "Username" TEXT, 
            "Password" TEXT, 
            PRIMARY KEY("Username") 
            );""")
con.commit()

cur.execute("""
CREATE TABLE "Store" ( 
    "Store_ID" INTEGER, 
    "Store_Name" TEXT, 
    "Username" TEXT, 
   
    FOREIGN KEY("Username") REFERENCES "User"("Username"), 
    PRIMARY KEY("Store_ID" AUTOINCREMENT) );""")

con.commit()'''
cur.execute("DROP TABLE Books")

cur.execute("""
    CREATE TABLE "Books" ( 
        "Book_ID" TEXT, 
        "Book_Name" TEXT, 
        "Number_of_books" INTEGER, 
        "Store_id" INTEGER, 
        FOREIGN KEY("Store_id") REFERENCES "Store"("Store_ID") ON DELETE CASCADE,
         PRIMARY KEY("Book_ID","Store_id") );
    """)
con.commit()
