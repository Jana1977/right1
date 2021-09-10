
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()


# drop_table = "DROP TABLE users "
# cursor.execute(drop_table)

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

#a tuple
#user = (1,'jana','asdf')
users = [
(1,'jana','asdf'),
(2,'kavi','asdf'),
(3,'nynei','test')

]

insert_query = "INSERT into users VALUES (?,?,?)"
#cursor.execute(insert_query , user)
cursor.executemany(insert_query , users)

select_query = "select * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()