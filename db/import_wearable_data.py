import mysql.connector
import os

mydb = mysql.connector.connect(
  host="127.0.0.1",
  #host="centralHub",
  user="phpmyadmin@centralHub",
  passwd="fydp90640",
  #port="3306"
  database="Titan",
)


mycursor = mydb.cursor()

for filename in os.listdir('/home/pi/Desktop/wearabledata'):
    if not filename.startswith('.'):
        #print(filename)
        sql = """LOAD DATA LOCAL INFILE \'{0}\' 
        INTO TABLE WS_Data 
        FIELDS TERMINATED BY ',' 
        LINES TERMINATED BY '\n' 
        IGNORE 1 LINES 
        (@dummy, timeOfRecord, @dummy, acce_x, acce_y, acce_z);""".format("/home/pi/Desktop/wearabledata/"+filename)
        #val = ("/home/pi/Desktop/wearabledata/"+filename)
        mycursor.execute(sql)
        print(mycursor.rowcount, "record inserted.")
        
mydb.commit()
        
