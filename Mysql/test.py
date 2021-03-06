import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root@localhost",    # 数据库用户名
  passwd="Gaoming1221"   # 数据库密码
)
 
print(mydb)