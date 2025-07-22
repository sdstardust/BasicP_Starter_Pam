def calculate_shipping_price(distance):
    # กำหนดค่าขนส่งตามระยะทาง
    if 5 <= distance <= 50:
        price = 10
    elif 51 <= distance <= 100:
        price = 15
    elif 101 <= distance <= 300:
        price = 25
    elif 301 <= distance <= 500:
        price = 35
    elif distance > 500:
        price = 45
    else:
        return "ส่งฟรีจ้า"

    vat = price * 7 / 100
    total_price = price + vat

    return f"ระยะทางที่ขนส่ง : {distance} km\nค่าขนส่ง(ไม่รวม Vat) : {price}\nค่า Vat : {vat}\nค่าขนส่งรวม Vat : {total_price}"

# รับค่าระยะทางจากผู้ใช้
Rayatarng = int(input("Rayatarng :  "))

# เรียกใช้ฟังก์ชันเพื่อคำนวณค่าขนส่ง
result = calculate_shipping_price(Rayatarng)
print(result)


##แบบไม่ใช้ function


# +vat 7% โชว์ราคาทีละอย่างและโชว์ราคารวม

# Rayatarng = int(input("Rayatarng :  "))
# price = 0

# if Rayatarng >= 5 and Rayatarng <= 50:
#     price = 10
#     vat = price*7/100
#     print("ระยะทางที่ขนส่ง : ", Rayatarng, "km", "ค่าขนส่ง(ไม่รวม Vat): ", price, "ค่า Vat : ", vat, "ค่าขนส่งรวม Vat", price + vat)
# elif Rayatarng >= 51 and Rayatarng <= 100:
#     price = 15
#     vat = price*7/100
#     print("ระยะทางที่ขนส่ง : ", Rayatarng, "km", "ค่าขนส่ง(ไม่รวม Vat): ", price, "ค่า Vat : ", vat, "ค่าขนส่งรวม Vat", price + vat)
# elif Rayatarng >= 101 and Rayatarng <= 300:
#     price = 25
#     vat = price*7/100
#     print("ระยะทางที่ขนส่ง : ", Rayatarng, "km", "ค่าขนส่ง(ไม่รวม Vat): ", price, "ค่า Vat : ", vat, "ค่าขนส่งรวม Vat", price + vat)
# elif Rayatarng >= 301 and Rayatarng <= 500:
#     price = 35
#     vat = price*7/100
#     print("ระยะทางที่ขนส่ง : ", Rayatarng, "km", "ค่าขนส่ง(ไม่รวม Vat): ", price, "ค่า Vat : ", vat, "ค่าขนส่งรวม Vat", price + vat)
# elif Rayatarng > 500:
#     price = 45
#     vat = price*7/100
#     print("ระยะทางที่ขนส่ง : ", Rayatarng, "km", "ค่าขนส่ง(ไม่รวม Vat): ", price, "ค่า Vat : ", vat, "ค่าขนส่งรวม Vat", price + vat)
# else:
#     print("ส่งฟรีจ้า")