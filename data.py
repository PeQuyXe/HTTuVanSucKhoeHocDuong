import mysql.connector

# Kết nối đến cơ sở dữ liệu
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='17072002',
    database='kbs_19'
)
c = conn.cursor()

# Tạo bảng để lưu trữ thông tin tư vấn cho các môn thể thao
c.execute('''
CREATE TABLE IF NOT EXISTS sports_advice (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_title VARCHAR(255) NOT NULL,
    introduction TEXT,
    basic_rules TEXT,
    benefits TEXT,
    exercises_and_techniques TEXT,
    nutrition_and_health TEXT,
    additional_information TEXT
)
''')

# Thêm dữ liệu cho môn thể thao Bóng đá vào bảng
c.execute('''
INSERT INTO sports_advice (sport_title, introduction, basic_rules, benefits, exercises_and_techniques, nutrition_and_health, additional_information)
VALUES (
    'Bóng đá',
    '-  Bóng đá là một môn thể thao đội hình phổ biến trên toàn thế giới.
     -  Trận đấu diễn ra giữa hai đội, mỗi đội cố gắng đưa bóng vào lưới đối phương để ghi bàn',
    '-  Trận đấu kéo dài 90 phút, chia thành hai hiệp.
     -  Mỗi đội có 11 cầu thủ trên sân.
     -	Ngoài thời gian chính thức, có thêm thời gian bù giờ nếu cần.
     -	Có nhiều luật lệ về việc sử dụng tay, việc chơi thô bạo, và việc việt bàn.',
    '-  Phát triển thể chất: Bóng đá giúp cải thiện sức mạnh, sự linh hoạt và sự nhạy bén.
     -	Tính Đồng Đội: Cầu thủ học cách làm việc nhóm và giao tiếp hiệu quả.
     -	Khả năng Chiến Thuật: Bóng đá yêu cầu sự tư duy chiến thuật và quyết định nhanh chóng.
     -	Sức Khỏe Tâm Lý: Giúp giảm căng thẳng và cải thiện tâm trạng',
    '•	Bài Tập Vận Động:
        -	Chạy: Bài tập chạy giúp cải thiện sức mạnh cơ tim, tăng cường khả năng chịu đựng và nâng cao sức bền.
        -	Nhảy: Bài tập nhảy, như nhảy dây hoặc nhảy lên cao, tăng cường sức mạnh chân và khả năng nhảy.
        -	Xoay Người: Các bài tập xoay người cũng quan trọng để tăng cường sự linh hoạt và giảm nguy cơ chấn thương.
    •	Bài Tập Kỹ Thuật:
        -	Kỹ Thuật Chuyền Bóng: Tập trung vào việc sử dụng chân và cơ bắp để chuyền bóng một cách chính xác và hiệu quả.
        -	Kỹ Thuật Sút Bóng: Học cách sút bóng với độ chính xác và sức mạnh, bao gồm cả sút từ xa và sút tầm gần.
        -	Kiểm Soát Bóng: Bài tập tập trung vào việc kiểm soát và giữ bóng trong tình huống khác nhau.',
    '•	Chế Độ Dinh Dưỡng:
        -	Cân Đối Protein, Carbohydrate, và Chất Béo: Cung cấp năng lượng và dưỡng chất cần thiết cho cả hoạt động cường độ cao và phục hồi cơ bắp.
        -	Cân Nước Đủ: Dụng đủ nước để tránh sự mất nước quá mức, giúp duy trì cơ bắp linh hoạt.
     •	Lịch trình Nghỉ Ngơi:
        -	Ngủ Đủ Giấc: Kế hoạch ngủ đủ giấc giúp cơ bắp phục hồi và tăng cường tinh thần.',
    '-	Giải Đấu Nổi Tiếng: Các giải đấu như World Cup, UEFA Champions League.')
''')
# Thêm dữ liệu cho môn thể thao Bóng chuyền vào bảng
c.execute('''
INSERT INTO sports_advice (sport_title, introduction, basic_rules, benefits, exercises_and_techniques, nutrition_and_health, additional_information)
VALUES (
    'Bóng chuyền',
    ' - Bóng chuyền là một môn thể thao đội hình chơi trong một không gian hẹp, giữa hai đội với mục tiêu chuyển bóng qua một mạng cao đặt ở giữa sân để ghi điểm.
      -	Có hai loại chính: bóng chuyền trong nhà và bóng chuyền bãi biển.',
    ' -	Trận đấu chia thành 3-5 set, mỗi set kéo dài đến 25 điểm (phải thắng cách nhau ít nhất 2 điểm).
      -	Mỗi đội có 6 người cùng tham gia trên sân.
      -	Mỗi lượt đội được phép chạm bóng tối đa ba lần trước khi chuyển bóng sang đội bạn.',
    '-	Tăng Cường Thể Chất: Bóng chuyền cần sự nhảy cao, nhanh nhẹn và sức mạnh cơ bắp.
     -	Phát Triển Kỹ Thuật: Kỹ thuật chuyền, tấn công và phòng ngự được cải thiện thông qua việc luyện tập.
     -	Tính Đồng Đội và Giao Tiếp: Quan trọng trong việc xây dựng tinh thần đồng đội và giao tiếp hiệu quả.',
    'Bài Tập:
    •	Cơ Bắp Chân:
        -	Squat Jumps: Kết hợp squat với nhảy để tăng cường sức mạnh cơ bắp chân và khả năng nhảy.
        -	Leg Press: Bài tập tập trung vào cơ đùi và cơ mông.
    •	Cơ Bắp Tay:
        -	Push Jerk: Kết hợp sự nhảy với đẩy tạ để tăng cường cơ trên cơ bắp vai và cơ triceps.
        -	Dumbbell Rows: Tăng cường cơ lưng và cơ bắp cánh tay.
    Kỹ Thuật:
    •	Chuyền Bóng:
        -     Overhead Pass (Set): Kỹ thuật chuyền bóng từ trên đầu, tập trung vào độ chính xác và độ nhanh nhẹn.
        -     Bump Pass (Forearm Pass): Chuyền bóng bằng cánh tay dưới, tập trung vào sự linh hoạt và phản xạ.
    •	Phòng Ngự:
        -	Block Jump: Bài tập nhảy cao để cản trở đường bóng của đối phương.
        -	Footwork Drills: Tập trung vào độ linh hoạt và chuyển động nhanh chóng để phòng ngự hiệu quả.',
    '•	Chế Độ Ăn Uống Cân Đối:
        -	Protein-rich Diet: Ăn uống giàu protein từ thực phẩm như thịt, cá, đậu nành để hỗ trợ sự phục hồi cơ bắp.
        -	Carbohydrates: Cung cấp năng lượng cho hoạt động cường độ cao.
        -	Chất Béo Khỏe Mạnh: Chọn chất béo không no từ nguồn như hạt, dầu cá hồi.
    •	Nghỉ Ngơi Đủ:
        -	Ngủ Đủ Giấc: Duy trì giấc ngủ đủ giấc giúp phục hồi cơ bắp và cải thiện tinh thần.
        -	Nghỉ Ngơi Hợp Lý: Lên kế hoạch cho những buổi tập nhẹ và ngày nghỉ để tránh chấn thương do quá tải.',
    'Giải Đấu Quốc Tế: Bóng chuyền thường tham gia các sự kiện quốc tế như Olympic và các giải đấu thế giới. Đội Tuyển Bóng Chuyền: Đội tuyển quốc gia thường là niềm tự hào và tham gia nhiều giải đấu lớn...'
)
''')
#Thêm dữ liệu cho môn thể thao Bóng rổ vào bảng
c.execute('''
INSERT INTO sports_advice (sport_title, introduction, basic_rules, benefits, exercises_and_techniques, nutrition_and_health, additional_information)
VALUES (
    'Bóng rổ',
    '   -	Bóng rổ là một môn thể thao nơi hai đội thi đấu để đưa bóng vào rổ đối phương để ghi điểm. 
        -	Đội có số điểm cao hơn sau khi kết thúc thời gian thi đấu sẽ giành chiến thắng.',
    '   -	Mỗi đội có năm cầu thủ trên sân.
        -	Mục tiêu là đưa bóng vào rổ đối phương để ghi điểm.
        -	Bóng rổ có thời gian thi đấu chia thành các hiệp, mỗi hiệp thường kéo dài 12 phút.
        -	Các quy tắc như việc tránh chạm vào đối thủ, việc giữ bóng quá thời gian quy định, và việc điều khiển không chính xác bóng được áp dụng.',
        
    '   -	Phát Triển Physical Fitness: Tham gia bóng rổ giúp cải thiện sức khỏe tim mạch, tăng sức mạnh cơ bắp, và cải thiện sự linh hoạt.
        -	Phát Triển Kỹ Năng Giao Tiếp: Bóng rổ đòi hỏi sự tương tác và giao tiếp liên tục giữa các thành viên trong đội.
        -	Học Hỏi Kỹ Năng Lãnh Đạo: Việc làm đội trưởng hoặc tham gia vào các quyết định chiến thuật có thể phát triển kỹ năng lãnh đạo.
',
    '   -	Bài Tập Vận Động: Bài tập như chạy nhanh, nhảy dây, và tập luyện cardio giúp cải thiện sức bền và nhanh nhẹn.
        -	Kỹ Thuật Điều Khiển Bóng: Bài tập tập trung vào cách điều khiển bóng, chuyển động, và ném bóng có thể được thực hiện để nâng cao kỹ thuật.',
    '   -	Chế Độ Dinh Dưỡng: Người chơi cần duy trì một chế độ ăn lành mạnh, chủ yếu là protein, carbohydrate, và chất béo tốt để cung cấp năng lượng và hỗ trợ phục hồi cơ bắp.
        -	Nghỉ Ngơi và Phục Hồi: Thời gian nghỉ đủ và kỹ thuật phục hồi, như massage và tập luyện ném bóng nhẹ, là quan trọng để tránh chấn thương và duy trì sức khỏe tốt.',
    'Các Giải Đấu Quan Trọng: Bóng rổ là môn thể thao phổ biến trên toàn thế giới và có nhiều giải đấu quan trọng như NBA (Hoa Kỳ), EuroLeague (Châu Âu), và giải đấu Olympic.'
)
''')
# Thêm dữ liệu cho môn thể thao cầu lông vào bảng
c.execute('''
INSERT INTO sports_advice (sport_title, introduction, basic_rules, benefits, exercises_and_techniques, nutrition_and_health, additional_information)
VALUES (
    'Cầu lông',
    '  -	Cầu lông là một môn thể thao trong đó hai hoặc bốn người chơi sử dụng rackets để đánh bóng qua mạng, cố gắng khiến đối thủ không thể trả lời cú đánh.
       -	Trận đấu có thể diễn ra giữa đội đơn hoặc đội đôi.',
    '   -	Mỗi đội có năm cầu thủ trên sân.
        -	Mục tiêu là đưa bóng vào rổ đối phương để ghi điểm.
        -	Bóng rổ có thời gian thi đấu chia thành các hiệp, mỗi hiệp thường kéo dài 12 phút.
        -	Các quy tắc như việc tránh chạm vào đối thủ, việc giữ bóng quá thời gian quy định, và việc điều khiển không chính xác bóng được áp dụng.',
    '   -	Tăng Cường Sức Khỏe Cardiovascular: Cầu lông đòi hỏi sự chuyển động nhanh chóng và liên tục, giúp tăng cường sức khỏe tim mạch và hệ thống tuần hoàn.
        -	Phát Triển Sự Linh Hoạt và Tăng Cường Sức Mạnh: Những cú đánh và di chuyển trong cầu lông giúp phát triển sự linh hoạt và tăng cường cơ bắp.
        -	Phát Triển Kỹ Năng Tư Duy Chiến Thuật: Cầu lông đòi hỏi sự chiến thuật và kỹ năng quan sát để dự đoán động tác của đối thủ.',
    '   -	Bài Tập Nâng Cao Nhanh Nhẹn: Bài tập như chạy nhanh, nhảy dây và bài tập tăng cường cơ bắp giúp nâng cao khả năng di chuyển nhanh nhẹn.
        -	Kỹ Thuật Đánh Cầu: Bài tập tập trung vào kỹ thuật đánh cầu, bao gồm cả cú đánh lông, đánh ngắn, và đánh đường giữa sân.',
    '   -	Dinh Dưỡng Đúng Cách: Người chơi cần duy trì chế độ ăn cân đối với đủ năng lượng từ carbohydrate, đạm từ protein, và chất béo tốt để hỗ trợ sức khỏe và phục hồi sau các buổi tập và trận đấu.
        -	Nghỉ Ngơi và Phục Hồi: Việc có đủ thời gian nghỉ giữa các buổi tập và trận đấu là quan trọng để tránh chấn thương và duy trì sức khỏe tốt.',
    'Các Giải Đấu Quan Trọng: Cúp Thomas và Uber (đội đội), giải đấu All England (đơn nam và đơn nữ), và cầu lông Olympic.'
)
''')
# Thêm dữ liệu cho môn thể thao bơi lội vào bảng
c.execute('''
INSERT INTO sports_advice (sport_title, introduction, basic_rules, benefits, exercises_and_techniques, nutrition_and_health, additional_information)
VALUES (
    'Bơi lội',
    '  -	Bơi lội là một hoạt động thể thao dưới nước( aquatic ) trong đó người chơi sử dụng các kỹ thuật đặc biệt để tiến triển qua mặt nước.
       -	Có nhiều loại bơi lội khác nhau, bao gồm bơi lội tự do, bơi lội bướm, bơi lội ngửa, và bơi lội hỗn hợp.',
    '  -	Người bơi cần phải nằm yên trên bờ hoặc nước trước khi nổi cờ bắt đầu đua.
        -	Mọi người bơi cần phải giữ vững tư thế cho đến khi tín hiệu bắt đầu được kích hoạt.
        -	Người bơi không được phép sử dụng tường biên hoặc đáy bể để có ưu thế trong việc tiến triển.
        -	Trong các đua đội, việc chuyển giao dải đền phải diễn ra trong khu vực quy định mà không làm mất tốc độ.
        -	Bước chân phải được giữ trong nước, và việc đạp hoặc chạm vào đối thủ không được phép.
        -	Người bơi được phép nghỉ ngơi trong lúc bơi, nhưng họ không được được hỗ trợ bởi bất kỳ người nào khác
        -	Người bơi phải tuân theo các luật lệ và biển báo trong khu vực bơi, và không được phép làm các hành động mạo hiểm hoặc nguy hiểm.
        -	Người bơi phải áp dụng các luật phục hồi, bao gồm cách giữ người đuối nước và thực hiện thủ thuật hồi sức.',
    '   -	Tăng Cường Sức Khỏe Toàn Diện: Bơi lội là hoạt động cardio tuyệt vời, giúp cải thiện sức khỏe tim mạch, tăng sức mạnh cơ bắp, và nâng cao sự linh hoạt.
        -	Giảm Áp Lực Cơ Bắp và Khớp: Do nước mang lại sự hỗ trợ, bơi lội giúp giảm áp lực lên cơ bắp và khớp, làm giảm rủi ro chấn thương.
        -	Đốt Cháy Năng Lượng và Giảm Cân: Bơi lội là hoạt động giảm áp lực ',
    '   -	Bơi Lội Tự Do: Kỹ thuật này bao gồm cú đẩy chân và cú quay tay để tiến triển qua nước.
        -	Bơi Lội Bướm: Kỹ thuật đặc biệt với cú đẩy chân và cú đánh tay hình chữ Y, tạo ra sự đồng đều và mạnh mẽ.
        -	Bơi Lội Ngửa: Bơi lội trên lưng, thường đi kèm với cú quay tay và đẩy chân.',
    '   -	Chế Độ Dinh Dưỡng: Người chơi bơi lội cần duy trì một chế độ ăn đủ dưỡng chất, bao gồm carbohydrate, protein, chất béo, và nhiều nước để duy trì năng lượng và sức khỏe.
        -	Phục Hồi Sau Tập Luyện: Việc nghỉ ngơi và phục hồi là quan trọng để giảm cảm giác mệt mỏi và tránh chấn thương.',
    'Các Giải Đấu Quan Trọng: Bơi lội là một phần quan trọng của nhiều sự kiện thể thao, bao gồm cả Olympic và các giải đấu quốc tế như FINA World Championships.'
)
''')

# Thêm dữ liệu cho môn thể thao điền kinh vào bảng
c.execute('''
INSERT INTO sports_advice (sport_title, introduction, basic_rules, benefits, exercises_and_techniques, nutrition_and_health, additional_information)
VALUES (
    'Điền kinh',
    '  •	Mục Tiêu:
        -	Điền kinh là một môn thể thao trong đó các vận động viên cạnh tranh để đạt được thành tích tốt nhất trong một loạt các bài thi thể thao khác nhau.
       •	Các Bài Thi Chính:
        -	Bao gồm các bài thi như chạy nhanh, nhảy xa, nhảy cao, ném lao, và chạy bền.',
    '   •	Chạy Nhanh:
        -	Người chạy phải duy trì tốc độ cao và vượt qua đường đua trong thời gian ngắn nhất có thể.
        -	Quy tắc chính là không bắt đầu trước tín hiệu bắt đầu.
        •	Nhảy Xa và Nhảy Cao:
        -	Người thí sinh phải nhảy xa hoặc nhảy cao vượt qua một đường dài hoặc một thanh cố định.
        -	Quy tắc chính liên quan đến kỹ thuật nhảy và vùng rơi.
        •	Ném Lao:
        -	Bài thi này yêu cầu người chơi ném một cây lao càng xa càng tốt.
        -	Quy tắc chính liên quan đến kỹ thuật ném và kỹ thuật xoay.
        •	Chạy Bền:
        -	Người chạy phải duy trì một tốc độ ổn định trong quãng đường dài.
        -	Quy tắc chính bao gồm việc giữ cho một chân luôn tiếp xúc với mặt đất và giữ cho cơ thể không chấm dứt sự chuyển động.
',
    '   •	Tăng Cường Sức Mạnh và Sức Bền:
        -	Chạy nhanh, nhảy xa và cao, và chạy bền đều đặn giúp tăng cường sức mạnh cơ bắp và sức bền.
        •	Phát Triển Kỹ Năng Tư Duy Chiến Thuật:
        -	Ném lao và nhảy đòi hỏi sự tư duy chiến thuật để đạt được kết quả tốt nhất.
',
    '   •	Bài Tập Tăng Cường Sức Mạnh:
        -	Bài tập như nâng tạ và tập luyện chạy tốc độ giúp tăng cường sức mạnh.
        •	Kỹ Thuật Chạy:
        -	Bài tập tập trung vào kỹ thuật chạy, bao gồm cả việc duy trì đúng tư thế và bước chạy hiệu quả.
',
    '•	Chế Độ Ăn Đúng:
    -	Vận động viên cần duy trì chế độ ăn lành mạnh với đủ năng lượng từ carbohydrate, protein, và chất béo.
    •	Nghỉ Ngơi và Phục Hồi:
    -	Thời gian nghỉ ngơi đủ là quan trọng để phục hồi cơ bắp và tránh chấn thương.',
    'Điền kinh là một phần quan trọng của các sự kiện thể thao lớn như Olympic và các giải đấu thế giới như World Athletics Championships.'
)
''')
# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
