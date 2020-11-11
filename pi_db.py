import pymysql

con = pymysql.connect(host="",
                      user="",
                      password="",
                      db="",
                      charset="")

cur = con.cursor()

sql = "INSERT INTO urine_information (datetime, volumn) VALUES (?, ?)"
cur.execute(sql)
con.commit()


sql = "INSERT INTO urinalysis_information (blood, bilirubin, urobilinogen, ketones, protein, glucose, ph) VALUES (?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql)
con.commit()
