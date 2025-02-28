# database connection 
import mysql.connector
#from datetime import datetime

#connect to the database
try:
    mydb = mysql.connector.connect(
    host="Localhost",
    port=3306,
    user="root",
    password="" ,
    # database="my_calculator"
    database="world"
    )
    print("kkjhjkhjkhjk")
    print(mydb)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM my_calculator.history")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
except mysql.connector.Error as err:
    print('Error', format(err))
    


# def History_filed():
#     global calculation
#     calculation = mycursor.execute()
#     text_result.delete(1.0, "end")
#     text_result.insert(1.0, calculation)


# btn_colan = tk.Button(root, text=":", command=History_filed , width=11, font= ("arial",14),background="orange")
# btn_clear.grid(row=7, column=2)

# # sql query to create column 
# sql = "INSERT INTO history (expression,result) VALUES (%s, %s)"
# val = ("5+3","8")

# mycursor.execute(sql, val)
# mydb.commit()
# print("Record inserted successfully!")  
