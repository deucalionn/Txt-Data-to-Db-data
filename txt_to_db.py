import sqlite3
import os
import sys


def GoToDb(fichier, Table, FichierBdd):
    try:
        connectb = sqlite3.connect(FichierBdd)
        cursor = connectb.cursor()
    except:
        print("Error, please check if the file is correct.")
        quit()
    try:
        f = open(fichier, "r")
        for line in f.readlines(): 
            PartOne = line.split(":")[0]
            PartTwo = line.split(":")[1]
            #PartThree = line.split(":")[3] [!] -> If you have more data to add you can add this line that will retrieve the next data. You can repeat this action as you see fit.
            ToAdd = (PartOne, PartTwo)
            cursor.execute('INSERT INTO '+ Table +' VALUES(?,?)',ToAdd)
            connectb.commit()
        print("All data has been added")
    except:
        print("Error, data could not be added.")

def main():
    try:        
        fichier = sys.argv[1]
        FichierBdd = sys.argv[2]
        Table = sys.argv[3]
        print("Txt to db script.")
        print("By Deucalion\n")
        print("The data of {} will be added in {} in the table {}.".format(fichier, FichierBdd, Table))
        GoToDb(fichier, Table, FichierBdd)
    except:
        print("Error, for using this program you have to specifie : ")
        print("python txt_to_db.py <file.txt> <file.db> <name_of_the_table>")


main()