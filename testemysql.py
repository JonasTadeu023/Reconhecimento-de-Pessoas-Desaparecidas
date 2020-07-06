import pymysql 

connect = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

db = connect.db()
db.execute("SHOW DATABASES")

for x in db:
    print(x)