import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='17072002',
    database='kbs_19'
)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
            (id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            gender VARCHAR(255),
            age INT,
            height INT,
            weight INT,
            sleep_duration INT)''')

# Lưu thay đổi vào cơ sở dữ liệu
conn.commit()
conn.close()
