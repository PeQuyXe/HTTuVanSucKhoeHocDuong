import mysql.connector

# Thiết lập kết nối tới cơ sở dữ liệu
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="17072002",
  database="kbs_19"
)

# Tạo bảng low_activity
mycursor = mydb.cursor()

# Tạo bảng high_activity
mycursor.execute("CREATE TABLE high_activity (id INT AUTO_INCREMENT PRIMARY KEY,sport_name VARCHAR(255), exercises TEXT, nutrition TEXT)")
# Tạo bảng high_activity
mycursor.execute("CREATE TABLE low_activity (id INT AUTO_INCREMENT PRIMARY KEY,sport_name VARCHAR(255), exercises TEXT, nutrition TEXT)")
# Tạo bảng high_activity
mycursor.execute("CREATE TABLE medium_activity (id INT AUTO_INCREMENT PRIMARY KEY,sport_name VARCHAR(255), exercises TEXT, nutrition TEXT)")
mydb.commit()

# Đóng kết nối tới cơ sở dữ liệu
mycursor.close()
mydb.close()