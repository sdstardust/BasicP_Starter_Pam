#function ที่ return ค่าเกรดออกมา
# def grade (score):
#     if score >= 80:
#         print("grade = A")
#     elif score >= 70:
#         print("grade = B")
#     elif score >= 60:
#         print("grade = C")
#     elif score >= 50:
#         print("grade = D")
#     else:
#         print("grade = F")

# score = float(input("กรุณากรอกคะแนนของคุณ: "))
# grade(score)

# def ui_multiply(x, y):
#     for i in range(1, y + 1):
#         print(f"{x} * {i} = { x * 1 }")
# # result = multiply(2, 2)
# ui_multiply(2, 12)

def bl_multiply(x, y):
    return x * y

print(bl_multiply(2,3))