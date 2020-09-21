from cs50 import SQL
from sys import argv , exit

db = SQL("sqlite:///students.db")

def check_input_files(argv):
    
    if(len(argv) != 2):
        print("Wrong number of files")
        exit()
    else:
        query_students(argv[1])

def query_students(house):
    
    query = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", house)
    for i in query:
        if i['middle'] == None:
            print(f'{i["first"]} {i["last"]}, born {i["birth"]}')
        else:
            print(f'{i["first"]} {i["middle"]} {i["last"]}, born {i["birth"]}')
        

check_input_files(argv)        
        