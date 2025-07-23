"""
    for <var> in range(<num>):
        ...code...

    รับตัวเลขจากผู้ใช้
    วนตั้งแต่ครั้งแรก จนถึงครั้งที่ผู้ใช้กรอกมา
    แล้วบวก 5 เรื่อยๆ
    และแสดงผลของการบวก 5 เรื่อยๆ ออกมา
"""
#  number = int(input("enter your number : "))
# sum = 0
# for i in range(1, number+1):
#     sum = sum + 5
#     print(f"ครั้งที่ {i} ได้ผลเป็น", sum)

number = int(input("enter your number : "))
i = 1
sum = 0
while i < number + 1 :
    i = i + 1
    sum = sum + 5
    print(f"ครั้งที่ {i} ได้ผลเป็น {sum}")