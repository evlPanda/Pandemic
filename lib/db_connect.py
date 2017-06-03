import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='pandemic',
                             password='password',
                             db='pandemic',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

    with connection.cursor() as cursor:
    
        sql = "SELECT cubes FROM virus where colour = %s"
        cursor.execute(sql, ('red',))
        #result = cursor.fetchone()
        #print(result)
        print('DB Connection: OK')

except:
    print('DB Connection: FAILED')

finally:
    connection.close()