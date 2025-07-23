def calculate_price(member_type, total, day):
    if member_type == "Gold":
        discount = 0.15 if total >= 1000 else 0.10
    elif member_type == "Silver":
        discount = 0.10 if total >= 1000 else 0.05
    else:
        discount = 0

    total_after_discount = total * (1 - discount)

    if day %2 == 1 and total_after_discount > 500:
        total_after_discount *= 0.95

    if total_after_discount < 800:
        delivery_fee = 50
    else:
        delivery_fee = 0

    final_total = total_after_discount + delivery_fee

    print(f"ราคาหลังหักส่วนลด: {total_after_discount:.2f} บาท")
    print(f"ค่าจัดส่ง: {delivery_fee} บาท")
    print(f"ยอดรวมทั้งหมด: {final_total:.2f} บาท")

member_type = str(input("คุณอยู่ในสมาชิกระดับอะไร : "))
total = int(input("จำนวนเงินรวมที่สั่งอาหาร : "))
day = int(input("วันที่สั่งซื้อ : "))
if day > 31:
    print("ใส่วันที่ผิด")
else:
    calculate_price(member_type, total, day)