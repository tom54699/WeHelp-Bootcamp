import mysql.connector
from mysql.connector import errors

try:

    # create connection pool and fetch the first connection
    db1 = mysql.connector.connect(
                                host = "localhost",
                                database = "website",
                                user = "root",
                                password = "1m2o3o4n",
                                charset = "utf-8",
                                pool_name='my_connection_pool',
                                pool_size=3)
    #db2 = mysql.connector.connect(pool_name='my_connection_pool')   
    db3 = mysql.connector.connect(pool_name='my_connection_pool')                         
    cursor = db3.cursor()
    print("Pool name:", db3.pool_name)
    print("Connection ID:", db3.connection_id)

    cursor.execute('select member.name,message.id,message.member_id,message.content from member inner join message on member.id = message.member_id;')

    print("\nResult: ")

    for row in cursor:
        print(row)

except errors.Error as e:
    print(e)

finally:
    db3.close()

