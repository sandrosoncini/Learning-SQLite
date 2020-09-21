from cs50 import SQL
from sys import argv , exit
import csv

db = SQL("sqlite:///students.db")

def check_input_files(argv):
    if(len(argv) != 2):
        print("Wrong number of files")
        exit()
    else:
        open_files()
        
def open_files():
    try:
        houses = open(argv[1], "r")
        read_file(houses)
        
    except FileNotFoundError:
        print("File Not Found ")

def read_file(file):
    reader = csv.DictReader(file)
    
    for row in reader:
        write_db(row)


def write_db(row):
    d = row["name"].split(' ')
    first = None
    middle = None
    last = None
    house = row['house']
    birth = row['birth']

    if len(d) == 2:
        first = d[0]
        middle = None
        last = d[1]  
    else:
        first = d[0]
        middle = d[1]
        last = d[2]
        
    db.execute("INSERT INTO students (first,middle, last ,house, birth) VALUES(?,?,?,?,?)", first, middle, last, house, birth)
    
check_input_files(argv)