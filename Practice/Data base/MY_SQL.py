# create Table & connect work banch with vs code or commonds connect databases
"""
1. mysql -u root -p --> Enter password --> Root@1234
2. mysql me :- SHOW DATABASES;
3. create table query :- 
4. 
5.
6.

SHOW TABLES;
SHOW TABLES FROM customers;

USE demo;
SELECT * FROM customers;
SELECT * FROM employees;

"""

# import pymysql # type: ignore

# try:
#     con = pymysql.connect(
#         host='localhost',
#         database='demo',
#         user='root',
#         password='Root@1234'
#     )
#     cursor = con.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS employees(
#         eno INT(5) PRIMARY KEY,
#         ename VARCHAR(10),
#         esal DOUBLE(10,2),
#         eaddr VARCHAR(100)
#     )
#     """)
#     print("Table Created...")

#     sql = "INSERT INTO employees (eno, ename, esal, eaddr) VALUES (%s, %s, %s, %s)"
#     records = [
#         (100, 'Sachin', 1000, 'Mumbai'),
#         (200, 'Dhoni', 2000, 'Ranchi'),
#         (300, 'Kohli', 3000, 'Delhi')
#     ]
#     try:
#         cursor.executemany(sql, records)
#         con.commit()
#         print("Records Inserted Successfully...")
#     except pymysql.MySQLError as e:
#         if con:
#             con.rollback()
#         print("There is a problem with SQL:", e)

#     cursor.execute("SELECT * FROM employees")
#     data = cursor.fetchall()
#     for row in data:
#         print("Employee Number:", row[0])
#         print("Employee Name:", row[1])
#         print("Employee Salary:", row[2])
#         print("Employee Address:", row[3])
#         print()
#         print()

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()


#----------------#------------Create Connection--------------#-----------------
# 1 step
# import pymysql

# try:
#     mydb = pymysql.connect(
#         host = "localhost",
#         database="demo",
#         user = "root",
#         password= "Root@1234" 
#     )
#     print("connection succefull",mydb)
# except pymysql.MySQLError as e:
#     print("Failed connection to the data bases Error",e)

#----------------#------------Create Table--------------#-----------------
# step 2
# import pymysql

# try:
#     mydb = pymysql.connect(
#         host = "localhost",
#         database="demo",
#         user = "root",
#         password= "Root@1234" 
#     )
#     print("connection succefull",mydb)
# except pymysql.MySQLError as e:
#     print("Failed connection to the data bases Error",e)

# mycursor = mydb.cursor()

# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS customers (
#         name VARCHAR(255),
#         address VARCHAR(255)
#     )
#     """)
# print("Table 'customers' created successfully. ")


# mycursor.execute("SHOW TABLES")


"""**
for x in mycursor:   # Ager dekhna hoto konsa table create huva 
    print(x) 
    """
#----------------#------------Insert Into Table--------------#-----------------
# step :- 3      executemany so many record will adding to use This method
# import pymysql

# try:
#     mydb = pymysql.connect(
#         host = "localhost",
#         database="demo",
#         user = "root",
#         password= "Root@1234" 
#     )
#     print("connection succefull",mydb)
# except pymysql.MySQLError as e:
#     print("Failed connection to the data bases Error",e)

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name,address) VALUES (%s, %s)"
# val = [
#     ("sanket","Highway 21"),
#     ("deepak","Road 22"),
#     ("priyank","Road 23"),
#     ("Kaushal","Highway 24"),
#     ("Ravi","Highway 25")
# ]
# mycursor.executemany(sql,val) # Note:- (executemany) bout sare add karne woh records tab ye use karenge (execute) ,Not so many) ki jagah par

# mydb.commit() # Acctuall record insert hoga..

# print(mycursor.rowcount, "record inserted")
#----------------#------------Select From a Table--------------#-----------------

# step 4 :-     Select all records from the "customers" table, and display the result

# import pymysql

# try:
#     mydb = pymysql.connect(
#         host = "localhost",
#         database="demo",
#         user = "root",
#         password= "Root@1234" 
#     )
#     print("connection succefull",mydb)
# except pymysql.MySQLError as e:
#     print("Failed connection to the data bases Error",e)

# mycursor = mydb.cursor()

# # mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT name,address FROM customers")

# myresult = mycursor.fetchall()  # fetchall se sare data hume milenge fetch hoke
 
# for x in myresult:
#     print(x)

#----------------#------------Update Table--------------#-----------------
# import pymysql

# mydb = pymysql.connect(
#     host = "localhost",
#     database="demo",
#     user = "root",
#     password= "Root@1234" 
# )
# print("connection succefull",mydb)

# mycursor = mydb.cursor()

# sql = "UPDATE customers SET name = %s WHERE name = %s"
# val = ('sunny','deepak') # right the fill this sunny is Newly updated

# mycursor.execute(sql,val)

# mydb.commit()

# print(mycursor.rowcount,"record(s) affected") # out put :- 6 record(s) affected

# commit () se permant changes jo karte hai woh save hojaye databases me...
# cursor() method through hi hum opration perform kar sakte hai... mydb.mycursor (python me hum ne object banaya uski method hai ye cursor) 
# execute() se hum apna actual sql kaa query pass kar sakte hai
# matlb ki execute karega ye aage 

#----------------#------------Delete Table--------------#---------------------#--------------#--------
import pymysql

mydb = pymysql.connect(
    host = "localhost",
    database="demo",
    user = "root",
    password= "Root@1234" 
)
mycursor = mydb.cursor()

sql = "DELETE  FROM customers WHERE name = 'priyank'"
# val = ("sunny","deepak")
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"Record delted")


