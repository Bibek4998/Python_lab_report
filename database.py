# Write a python program to create database and insert record and display them.
import sqlite3
conn=sqlite3.connect("Database.db")
cursor=conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    semester INTEGER,
    batch INTEGER
    )
"""
)
cursor.executemany(
    "INSERT INTO students(id,name,semester,batch) VALUES(?,?,?,?)",
    [
        (1,"Jhon David",5,2021),
        (2,"David Bekham",8,2015),
        (3,"Rudra Shakya",8,2017),
        (4,"Srijan Sact",1,2025),
        (5,"Avi David",1,2024),
        (6,"Shown Crint",6,2019),
        (7,"Sujan Poudel",2,2023),
        (8,"Ram BK",5,2021),
        (9,"Shyam Sharma",5,2020),
        (10,"Spura Kantra",3,2022)
    ]
)
conn.commit()
cursor.execute("SELECT * FROM students ")
rows=cursor.fetchall()
for row in rows:
    print("ID: ",row[0],"Name: ",row[1],"Semester: ",row[2],"Batch:",row[3])
cursor.close()
conn.close()