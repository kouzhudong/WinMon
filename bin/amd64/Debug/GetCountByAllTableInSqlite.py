import sqlite3

key = dict()

con = sqlite3.connect("D:\\test\\test.db")
cur = con.cursor()
sql = "select name from sqlite_master where type='table'"
res = cur.execute(sql)
for r in res.fetchall():
    sql = "SELECT COUNT(*) FROM " + r[0]
    for t in cur.execute(sql):
        #print(f"{r[0]:19} {t[0]:<9}")
        key[r[0]] = t[0]

list = sorted(key.items(), key = lambda k:(k[1], k[0]), reverse = True) 
for it in list:
    print(f"{it[0]:19} {it[1]:<9}")

cur.close()
con.close()
