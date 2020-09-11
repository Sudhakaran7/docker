import mysql.connector
from datetime import datetime, date, time

cnx = mysql.connector.connect(user='root', password='admin@123',
                              host='127.0.0.1',
                              database='movies', auth_plugin='mysql_native_password')
# cnx.close()

def movielist():
    cursor = cnx.cursor()
    query = ("SELECT * from movies")
    cursor.execute(query)
    records = cursor.fetchall()
    # for id,name in cursor:
    #     print("{},{}".format(id,name))
    for row in records:
        print("Movie ID= ", row[0], )
        print("Name = ", row[1])
        print('Date= ',row[2])
        print('Time',row[3])


def details():
    cursor = cnx.cursor()
    mycursor = cnx.cursor()
    val = input("Enter the movie name:")
    sql="select * from movies where name='"+val+"';"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    for i in records:
        id=i[0]
        date1 = (i[2])
        time1 = i[3]
        seats=i[4]
        print("Movie ID= ", i[0])
        print("Name = ", i[1])
        print('Date',i[2])
        print('Time',i[3])
    today = date.today()
    now = datetime.now().time()  # time object
    no1=datetime.combine(date.min, now) - datetime.min
    c=time1-no1
    minutes = c.seconds / 60
    if(today<date1 and minutes>=121):
        print("The movie is available!, Check for the seats!")
        n=int(input("Enter the number of seats:"))
        if(n<=10):
            if(seats>=n):
                m=seats-n
                sql1="""UPDATE movies SET seats=%s WHERE id=%s"""
                vall=(m,id)
                cursor.execute(sql1,vall)
                cnx.commit()
                print("Booking Confirmed!")  
            else:
                print("No seats!")
        else:
            print("Please Enter seats less or equal to 10")
            details()
    else:
        print("Sorry Movie is not available, look for some other movie!")

def exit():
    exit()


if __name__=="__main__":
    s='y'
    while(s!='no'):
        print('Enter the choice:\n 1)List of Movies!\n 2)Booking Movie from the given list!')
        n=int(input('Enter any choice:'))
        if(n==1):
            movielist()
        elif(n==2):
            details()
        else:
            exit()
        s = input("Type yes to continue and no to exit")
