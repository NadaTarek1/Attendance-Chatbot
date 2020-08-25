import mysql.connector as mysql



# Make sure you put the right credentials here connecting to and SQL database that uses the provided .sql file in this repository
mydb = mysql.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="attendance_chatbot"
)



def recordAttendance(user, id):
    try:
        cur = mydb.cursor()
        qry = "INSERT INTO `attendance` (`student_name`, `id`) VALUES ('{}', '{}')".format(user, id)
        cur.execute(qry)
        mydb.commit()
        print(cur.rowcount, "Attendance recorded.")
        return True
    except mysql.Error as e:
        s = str(e)
        if "Duplicate entry" in s:
            return True;
        return False;










