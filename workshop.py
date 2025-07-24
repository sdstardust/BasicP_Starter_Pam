# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    print("\nรายชื่อหนังทั้งหทด: ")
    for i, movie in enumerate(movie_list, 1):
        print(f"{i}. {movie['movie_name']} - {movie['ticket_price']} บาท")

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    if age_restriction == 'G':
        return True
    else:
        return int(user_age) >= int(age_restriction)

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Action' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม
    if genre == 'Action':
        return base_price + 50
    else:
        return base_price

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    # 3. รับอายุผู้ใช้
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
    show_movies(movie_list)
    
    try:
        choice = int(input("\nเลือกหนังที่ต้องการ (1-5): "))
        if choice < 1 or choice > len(movie_list): #lenใช้นับสมาชิก 
            print("เลือกหนังไม่ถูกต้อง")
            return
    except:
        print("กรุณากรอกตัวเลขเท่านั้น")
        return

    selected_movie = movie_list[choice - 1]
    
    try:
        age = int(input("กรอกอายุของคุณ: "))
    except:
        print("กรุณากรอกอายุเป็นตัวเลข")
        return

    if not check_age(age, selected_movie['age_restriction']):
        print("ขออภัย อายุน้อยเกินไป ไม่สามารถดูหนังเรื่องนี้ได้")
        return

    print("เลือกเสียงพากย์:")
    print("1. พากย์ไทย")
    print("2. Soundtrack")
    lang_choice = input("เลือก (1 หรือ 2): ")

    if lang_choice == '1':
        audio = 'พากย์ไทย'
    elif lang_choice == '2':
        audio = 'Soundtrack'
    else:
        print("เลือกรูปแบบเสียงไม่ถูกต้อง")
        return

    final_price = calculate_price(selected_movie['ticket_price'], selected_movie['genre'])

    print("\n:projector: รายการตั๋วของคุณ :projector:")
    print(f"ชื่อหนัง: {selected_movie['movie_name']}")
    print(f"เสียง: {audio}")
    print(f"ราคาตั๋ว: {final_price} บาท")


def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง
    print("=== ระบบโรงหนัง SuperSigma ===")
    print("1. แสดงหนังทั้งหมด")
    print("2. ซื้อตั๋วหนัง")


    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = input("เลือกเมนู (1 หรือ 2): ")

    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

    if menu == '1':
        show_movies(movies)
    elif menu == '2':
        buy_ticket(movies)
    else:
        print("เมนูไม่ถูกต้อง")


# เรียก main เพื่อเริ่มโปรแกรม
main()