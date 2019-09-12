import pymysql

def build_db_connection():
   conn = pymysql.connect(host=db0["host"],user=db0["user"],
                          password = db0["password"],database = "stock",charset = "utf-8")
   return conn


