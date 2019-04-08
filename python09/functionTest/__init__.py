import pymysql.cursors
 
conn = pymysql.connect(host='localhost',
        user='user',
        password=None,
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        sql = 'CREATE DATABASE test'
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()