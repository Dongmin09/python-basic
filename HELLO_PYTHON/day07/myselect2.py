import pymysql
conn = pymysql.connect(host='localhost', user='root', password='python', port=3306,
                       db='python', charset='utf8')
 
# 연관배열, JSON = 자바스크립트, DictCursor = 파이썬
curs = conn.cursor(pymysql.cursors.DictCursor)
 
sql = "select * from emp"
curs.execute(sql)
rows = curs.fetchall()

print(rows)    

curs.close()
conn.close()
