from sqlite3 import * 
con = None 
try: 
    con = connect("winners.db") 
    sql = "create table if not exists student(name text, college text)" 
    cursor = con.cursor() 
    cursor.execute(sql) 
    con.commit() 
except Exception as e: 
     print("issue", e) 
finally: 
     if con is not None:
        con.close() 


while True: 
    try:
        op = int(input("1 create, 2 view and 3 exit: \n")) 
    except ValueError:
        print("Please enter a valid number")
        continue

    if op == 1: 
        con = None 
        try: 
            con = connect("winners.db") 
            sql = "insert into student values(?, ?)"
            name = input("enter name: ") 
            college = input("enter college name: ") 
            cursor = con.cursor() 
            cursor.execute(sql, (name, college))
            con.commit() 
            print("record created") 
        except Exception as e: 
            if con: con.rollback() 
            print("issue", e) 
        finally: 
            if con: con.close() 

    elif op == 2: 
        con = None 
        try: 
            con = connect("winners.db") 
            sql = "select * from student" 
            cursor = con.cursor() 
            cursor.execute(sql) 
            data = cursor.fetchall() 
            for d in data: 
                print(f"Name: {d[0]}, College: {d[1]}") 
        except Exception as e: 
            print("issue", e) 
        finally: 
            if con: con.close() 

    elif op == 3: 
        break 
    else: 
        print("invalid option")