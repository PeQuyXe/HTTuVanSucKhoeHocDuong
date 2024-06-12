import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='17072002',
    database='kbs_19'
)
c = conn.cursor()
#Hàm nhận thông tin người dùng
def receive_user_info():
    print("\n")
    print("Chào mừng bạn đến với Hệ thống Tư vấn Thể thao Học đường cho Học sinh!")
    print("Chúng tôi sẽ tư vấn thể thao học đường cho bạn dựa trên thông tin cá nhân bạn cung cấp.\n")
    name = input("Nhập tên của bạn: ")
    gender = input("Nhập giới tính của bạn (nam/nữ): ")
    age = int(input("Nhập tuổi của bạn (6->18): "))
    height = int(input("Nhập chiều cao của bạn (100->180) (cm): "))
    weight = int(input("Nhập cân nặng của bạn (10->80) (kg): "))
    sleep_duration = int(input("Nhập thời gian ngủ trung bình mỗi ngày (giờ): "))
    
    c.execute("INSERT INTO users (name, gender, age, height, weight, sleep_duration) VALUES (%s, %s, %s, %s, %s, %s)",
              (name, gender, age, height, weight, sleep_duration))
    conn.commit()
# Hàm lấy thông tin người dùng
def get_latest_user_info(c):
    c.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
    user_info = c.fetchall()
    user_info = user_info[0]
    name =  user_info[1]
    age = user_info[3]
    gender = user_info[2]
    height = user_info[4]
    weight = user_info[5]
    bmi = weight / ((height/100) ** 2) # type: ignore
    sleep_duration = user_info[6]
    
    return name, age, gender, height, weight, bmi, sleep_duration
# Hàm để sử dụng các trường hợp có trước để đưa ra gợi ý
def get_cbr_cases_data(c):
    c.execute("SELECT gender, age, height, weight, bmi, sleep_duration, suggestion FROM cbr_cases")
    return c.fetchall()
# Hàm tính toán độ tương đồng
def calculate_similarity(gender, age, height, weight, bmi, sleep_duration, case):
    case_gender, case_age, case_height, case_weight, case_bmi, case_sleep_duration, suggestion = case

    gender_similarity = 1 if gender == case_gender else 0
    age_similarity = 1 - abs(age - case_age) / 10.0
    height_similarity = 1 - abs(height - case_height) / 100.0
    weight_similarity = 1 - abs(weight - case_weight) / 100.0
    bmi_similarity = 1 - abs(bmi - case_bmi) / 10.0
    sleep_duration_similarity = 1 - abs(sleep_duration - case_sleep_duration) / 5.0

    total_similarity = (gender_similarity + age_similarity + height_similarity +
                        weight_similarity + bmi_similarity + sleep_duration_similarity) / 6.0

    return total_similarity, suggestion
# Hàm lấy trường hợp gần nhất và lưu trường hợp vào csdl
def get_and_insert_recommendation(c):
    name, age, gender, height, weight, bmi, sleep_duration = get_latest_user_info(c)
    cbr_cases_data = get_cbr_cases_data(c)
    similarities = []
    for case in cbr_cases_data:
        total_similarity, suggestion = calculate_similarity(gender, age, height, weight, bmi, sleep_duration, case)
        similarities.append((total_similarity, suggestion))
    # Sắp xếp các trường hợp theo độ tương đồng giảm dần
    similarities.sort(reverse=True)
    # Nhận khuyến nghị dựa trên trường hợp tương đồng nhất
    most_similar_case = similarities[0]
    recommendation = f"Với thông tin bạn cung cấp hệ thống đề xuất bạn tham gia hoạt động thể thao: {most_similar_case[1]}"
    print(f"\n{recommendation}")
    # Thêm thông tin người dùng vào cơ sở dữ liệu
    suggestion = most_similar_case[1]
    insert_recommendation_into_database(c, gender, age, height, weight, bmi, sleep_duration, suggestion)
    return suggestion
def insert_recommendation_into_database(c, gender, age, height, weight, bmi, sleep_duration, suggestion):
    c.execute('''INSERT INTO cbr_cases (gender, age, height, weight, bmi, sleep_duration, suggestion) VALUES (%s, %s, %s, %s, %s, %s, %s)''',
        (gender, age, height, weight, bmi, sleep_duration, suggestion))
    conn.commit()
# Hàm tư vấn khác cho người dùng dựa trên  rbr
def analyze_user_info():
    name, age, gender, height, weight, bmi, sleep_duration = get_latest_user_info(c)
    # Phân tích thông tin người dùng dựa trên các tập luật
    recommendations = []
    # Luật về thể trạng
    if 18.5 <= bmi < 25:
        recommendations.append("Thể trạng của bạn ở mức bình thường ==> Đề xuất các hoạt động vận động có độ khó trung bình để duy trì mức bình thường.")
    elif bmi >= 25:
        recommendations.append("Thể trạng của bạn ở mức trên bình thường ==> Đề xuất các hoạt động vận động có độ khó cao để trở lại mức bình thường .")
    elif bmi < 18.5:
        recommendations.append("Thể trạng của bạn ở mức dưới bình thường ==> Đề xuất các hoạt động như tăng cường dinh dưỡng và các hoạt động vận động đơn giản có tác đụng trở về trạng thái bình thường.")
    # Luật về thời gian ngủ
    if sleep_duration < 7: # type: ignore
        recommendations.append("Bạn chưa có thời gian nghỉ ngơi chuẩn ==> Hãy để thời gian ngủ ở mức 7-9 h môĩ ngày")
    elif 7 <= sleep_duration <= 9: # type: ignore
        recommendations.append("Bạn đã có thời gian nghỉ ngơi chuẩn ==> Hãy tiếp tục với thời gian ngủ 7-9h mỗi ngày")
    elif sleep_duration > 9 : # type: ignore
        recommendations.append("Bạn chưa có thời gian nghỉ ngơi chuẩn ==> Hãy để thời gian ngủ ở mức 7-9 h môĩ ngày")
    print("\nVới một số thông tin bạn đã cung cấp hệ thống xin đưa ra tư vấn cho bạn: ")
    for recommendation in recommendations:
        print("- " + recommendation)
# Hàm cung cấp chi tiết về các môn thể thao hệ thống tư vấn   
def sport_details(c, suggestion):
    c.execute("SELECT * FROM sports_advice WHERE sport_title = %s", (suggestion,))
    sport_data = c.fetchone()
    if sport_data:
        print(f"\nThông tin chi tiết về môn thể thao '{suggestion}':")
        print("1. Giới Thiệu:")
        print(sport_data[2])
        print("\n2. Quy Tắc Cơ Bản:")
        print(sport_data[3])
        print("\n3. Lợi Ích:")
        print(sport_data[4])
        print("\n4. Thông Tin Khác:")
        print(sport_data[7])
    else:
        print("Lỗi vui lòng thử lại.")
    analyze_user_info()
    provide_details()
# Hàm cung cấp thông tin môn thế thao khác phù hợp
def provide_details():
    name, age, gender, height, weight, bmi, sleep_duration = get_latest_user_info(c)
    sport_title = None
    print("\nCác môn thể thao khác mà bạn có thể quan tâm: ")
    if gender == "nam":
        print("1. Bóng đá")
        print("2. Bơi lội")
        print("3. Bóng rổ")
        choice = input("\nNhập số tương ứng với môn thể thao bạn muốn xem: ")
        if choice == '1':
            sport_title = 'Bóng đá'
        elif choice == '2':
            sport_title = 'Bơi lội'
        elif choice == '3':
            sport_title = 'Bóng rổ'
    elif gender == "nữ":
        print("1. Cầu lông ")
        print("2. Bóng chuyền")
        print("3. Điền kinh")
        # Lấy lựa chọn từ người dùng
        choice = input("\nNhập số tương ứng với môn thể thao bạn muốn xem: ")
        if choice == '1':
            sport_title = 'Cầu lông'
        elif choice == '2':
            sport_title = 'Bóng chuyền'
        elif choice == '3':
            sport_title = 'Điền kinh'
    else:
        print("Lựa chọn không hợp lệ.")
    # Lấy dữ liệu từ cơ sở dữ liệu
    c.execute("SELECT * FROM sports_advice WHERE sport_title = %s", (sport_title,))
    sport_data = c.fetchone()
    # Hiển thị thông tin nếu dữ liệu tồn tại
    if sport_data:
        print(f"\nThông tin chi tiết về môn thể thao '{sport_title}':")
        print("1. Giới Thiệu:")
        print(sport_data[2])
        print("\n2. Quy Tắc Cơ Bản:")
        print(sport_data[3])
        print("\n3. Lợi Ích:")
        print(sport_data[4])
        print("\n4. Bài Tập và Kỹ Thuật:")
        print(sport_data[5])
        print("\n5. Dinh Dưỡng và Sức Khỏe:")
        print(sport_data[6])
        print("\n6. Thông Tin Khác:")
        print(sport_data[7])
    else:
        print("Không tìm thấy dữ liệu cho môn thể thao.")
    ask_show_alternatives()

# Hỏi xem người dùng đã biết thông tin cơ bản về môn thể thao này chưa
def ask_info_sport(c, suggestion):
    show_question = input("\nBạn có biết thông tin về môn thể thao này không? (yes/no): ")
    if show_question.lower() == 'no':
        sport_details(c, suggestion)
    elif show_question.lower() == 'yes':
        analyze_user_info()
        provide_details()
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 'yes' hoặc 'no'.")
# Hỏi xem người dùng có muốn xem thông tin về các môn thể thao khác không
def ask_show_alternatives():
    
    show_alternatives = input("Bạn có muốn xem thông tin về các môn thể thao khác không? (yes/no): ")
    
    if show_alternatives.lower() == 'yes':
        provide_details()
    elif show_alternatives.lower() == 'no':
        # analyze_user_info()
        print("\nCảm ơn bạn đã tìm hiểu về các môn thể thao.\n")
        print("Trên đây là nội dung tư vấn cho bạn. Cảm ơn bạn đã tham gia hệ thống. Hẹn Gặp Lại! ")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 'yes' hoặc 'no'.") 
# Sử dụng hệ mờ để đưa ra mức độ vận động về môn thể thao đã tư vấn
# Hàm thành viên cho chiều cao
def fuzzy_height(height):
    low = max(0, min(height - 100, 150 - height)) / 50
    medium = max(0, min(height - 100, 180 - height)) / 50
    high = max(0, height - 150) / 30
    return low, medium, high

# Hàm thành viên cho cân nặng
def fuzzy_weight(weight):
    light = max(0, min(weight - 10, 40 - weight)) / 30
    medium = max(0, min(weight - 10, 80 - weight)) / 30
    heavy = max(0, weight - 40) / 40
    return light, medium, heavy

# Hàm thành viên cho mức độ vận động
def fuzzy_activity(height, weight):
    height_low, height_medium, height_high = fuzzy_height(height)
    weight_light, weight_medium, weight_heavy = fuzzy_weight(weight)

    # Xác định giả thiết cho mức độ vận động
    activity_low = min(height_low, weight_heavy)
    activity_medium = min(height_medium, weight_medium)
    activity_high = min(height_high, weight_light)

    return activity_low, activity_medium, activity_high

def defuzzification(result):
    weights = [0, 1 , 2]  
    # giải mờ bằng trung bình trọng số
    weighted_sum = sum(value * weight for value, weight in zip(result, weights))
    sum_of_weights = sum(weights)
    defuzzified_value = weighted_sum / sum_of_weights
    return defuzzified_value
def process_and_display_info(c, suggestion):
    name, age, gender, height, weight, bmi, sleep_duration = get_latest_user_info(c)
    # Tính toán giá trị mờ
    result = fuzzy_activity(height, weight)
    activity = None
    table = None
    # Giải mờ và hiển thị kết quả giải mờ
    defuzzified_result = defuzzification(result)

    if 0 < defuzzified_result < 0.4:
        activity = "Thấp"
        table = "low_activity"
    elif 0.4 <= defuzzified_result < 0.7:
        activity = "Trung bình"
        table = "medium_activity"
    elif 0.7<= defuzzified_result  :
        activity = "Cao"
        table = "high_activity"

    print(f"\nMức độ vận động trong môn thể thao này của {name} là: {activity}")
    c.execute(f"SELECT * FROM {table} WHERE sport_name = %s", (suggestion,))
    sport_data2 = c.fetchone()
    if sport_data2:
        print(f"\nGợi ý về bài tập và chế độ dinh dưỡng dành cho {name}:")
        print("1. Bài Tập: ")
        print(sport_data2[2])
        print("\n2. Chế độ dinh dưỡng :")
        print(sport_data2[3])
    else:
        print("Không tìm thấy dữ liệu cho môn thể thao.")
def main():
    receive_user_info()
    suggestion = get_and_insert_recommendation(c)
    process_and_display_info(c, suggestion)
    ask_info_sport(c, suggestion)
if __name__ == '__main__':
    main()
