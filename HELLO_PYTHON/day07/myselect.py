# import pymysql
# conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
# cur = conn.cursor()
# sql = "select *from emp"
# cur.execute(sql)
#
# rows = cur.fetchall()
# print(rows)

import pymysql
conn = pymysql.connect(host='localhost', user='root', password='python', port=3306,
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = "select * from emp"
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)    

curs.close()
conn.close()
