import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'akam41',
    passwd = '41_dolPHIN'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrm_db")

print("All Done!")