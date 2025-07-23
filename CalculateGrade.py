# score = float(input("คะแนน: "))
# grade = chr(70) 
# grade = (
#     chr(65) * (score >= 80)
#     or chr(66) * (score >= 70 and score < 80)
#     or chr(67) * (60 <= score < 70)
#     or chr(68) * (50 <= score < 60)
#     or grade
# )

# print("เกรดของคุณคือ:", grade[0])

score = float(input("กรุณากรอกคะแนนของคุณ: "))

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print("เกรดของคุณคือ:", grade)