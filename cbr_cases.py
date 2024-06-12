import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='17072002',
    database='kbs_19'
)
c = conn.cursor()

# Tạo bảng để lưu trữ thông tin của các case
c.execute('''CREATE TABLE IF NOT EXISTS cbr_cases
            (id INT AUTO_INCREMENT PRIMARY KEY,
            gender VARCHAR(255),
            age INT,
            height FLOAT,
            weight FLOAT,
            bmi FLOAT,
            sleep_duration INT,
            suggestion VARCHAR(255))''')

# Chèn dữ liệu của các case vào bảng cbr_cases
cbr_cases_data = [
    ('nam', 11, 140, 35, 18.0, 8, 'Bóng đá'),
    ('nữ', 14, 155, 50, 20.8, 7, 'Bóng chuyền'),
    ('nam', 15, 165, 55, 16.5, 9, 'Bóng rổ'),
    ('nữ', 12, 150, 40, 17.8, 7, 'Điền kinh'),
    ('nam', 13, 155,  45, 18.7, 8, 'Bơi lội'),
    ('nữ', 16, 160, 52, 20.3, 7, 'Bóng chuyền'),
    ('nam', 14, 145, 38, 18.0, 9, 'Bơi lội'),
    ('nữ', 15, 165, 48, 22.2, 8, 'Bóng chuyền'),
    ('nam', 12, 138, 32, 16.9, 7, 'Bơi lội'),
    ('nữ', 13, 152, 42, 18.2, 8, 'Bơi lội'),
    ('nam', 14, 150, 48, 19.5, 8, 'Bóng rổ'),
    ('nữ', 13, 158, 46, 21.0, 7, 'Bơi lội'),
    ('nam', 16, 170, 60, 17.3, 9, 'Bóng đá'),
    ('nữ', 15, 145, 42, 20.0, 8, 'Bóng chuyền'),
    ('nam', 11, 136, 30, 15.5, 7, 'Bơi lội'),
    ('nữ', 14, 155, 52, 19.8, 8, 'Điền kinh'),
    ('nam', 15, 160, 56, 18.2, 9, 'Bóng rổ'),
    ('nữ', 13, 148, 38, 17.5, 7, 'Điền kinh'),
    ('nam', 12, 142, 36, 16.0, 8, 'cầu lông'),
    ('nữ', 16, 165, 55, 22.5, 9, 'Bóng chuyền'),
    ('nam', 14, 155, 50, 19.0, 8, 'Bóng rổ'),
    ('nữ', 12, 140, 38, 16.2, 7, 'Bơi lội'),
    ('nam', 15, 165, 58, 20.1, 9, 'Bóng đá'),
    ('nữ', 13, 150, 45, 18.8, 8, 'Bóng chuyền'),
    ('nam', 11, 142, 36, 16.5, 7, 'Cầu lông'),
    ('nữ', 14, 160, 55, 20.5, 8, 'Điền kinh'),
    ('nam', 16, 168, 62, 18.9, 9, 'Bóng rổ'),
    ('nữ', 15, 147, 40, 17.2, 7, 'Cầu lông'),
    ('nam', 12, 136, 32, 15.8, 8, 'Cầu lông'),
    ('nữ', 13, 155, 48, 19.2, 8, 'Bóng chuyền'),

]

c.executemany('''INSERT INTO cbr_cases (gender, age,height, weight, bmi, sleep_duration, suggestion)
                VALUES (%s, %s, %s, %s, %s, %s, %s)''', cbr_cases_data)

# Lưu thay đổi vào cơ sở dữ liệu
conn.commit() 