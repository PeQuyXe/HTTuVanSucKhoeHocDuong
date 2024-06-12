def fuzzy_height(height):
    low = max(0, min(height - 90, 130 - height)) / 40
    medium = max(0, min(height - 120, 150 - height)) / 30
    high = max(0, min(height - 140, 180 - height)) / 40
    return low, medium, high

def fuzzy_weight(weight):
    light = max(0, min(weight - 30, 60 - weight)) / 30
    medium = max(0, min(weight - 25, 80 - weight)) / 35
    heavy = max(0, weight - 50) / 30
    return light, medium, heavy
def defuzzification_weighted_average(x_values, mu_values):
    numerator = sum(x * mu for x, mu in zip(x_values, mu_values))
    denominator = sum(mu_values)

    if denominator == 0:
        # Tránh chia cho 0
        return None

    defuzzified_value = numerator / denominator
    return defuzzified_value

def fuzzy_activity(height, weight):
    # Đặt giá trị nằm giữa của các tập mờ cho chiều cao và cân nặng
    height_values = [40, 30, 40]  # Tương ứng với low, medium, high
    weight_values = [30, 35, 30]  # Tương ứng với light, medium, heavy

    # Lấy giá trị hàm tập mờ tương ứng với chiều cao và cân nặng
    height_mu = fuzzy_height(height)
    weight_mu = fuzzy_weight(weight)

    # Tính giá trị giải mờ theo trung bình trọng số
    result = defuzzification_weighted_average(height_values, height_mu) + defuzzification_weighted_average(weight_values, weight_mu)

    return result

# Ví dụ sử dụng
height_input = 160  # Chiều cao đầu vào
weight_input = 40  # Cân nặng đầu vào

# Tính toán giá trị giải mờ
activity_result = fuzzy_activity(height_input, weight_input)

# Xác định mức độ vận động
if activity_result is not None:
    if 0 <= activity_result < 0.4:
        activity = "Thấp"
    elif 0.4 <= activity_result < 0.7:
        activity = "Trung bình"
    elif 0.7 <= activity_result <= 1:
        activity = "Cao"
    print(f"Mức độ vận động: {activity}")
else:
    print("Không thể tính giá trị giải mờ do tổng các trọng số bằng 0.")
