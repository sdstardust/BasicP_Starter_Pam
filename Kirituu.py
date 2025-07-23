monsters = {
    "Dragon" : 500,
    "Fenrir" : 250,
    "Goblin" : 100
}
weapons = {
    "Scythe" : 150,
    "Greatsword" : 50,
    "Katars" : 10
}

for turn in range(10):
    print(f"\n===== เทิร์นที่ {turn + 1} =====")
    for name, hp in monsters.items():
        print(f"{name}: เลือด {hp}")

    print("คุณจะทำอะไร?")
    print("1. ต่อสู้กับมอนสเตอร์")
    print("2. ออก")
    choice = input("พิมพ์ 1 หรือ 2: ")

    if choice == "2":
        print("คุณหนีออกจากการต่อสู้...")
        break

    monster_name = input("เลือกมอนสเตอร์ที่ต้องการโจมตี (Dragon, Fenrir, Goblin): ")
    if monster_name not in monsters:
        print("ไม่มีมอนสเตอร์นี้!")
        continue

    print("อาวุธที่คุณมี:", list(weapons.keys()))
    weapon = input("เลือกอาวุธที่ใช้: ")
    if weapon not in weapons:
        print("ไม่มีอาวุธนี้!")
        continue

    atk_round = int(input("จะโจมตีกี่ครั้ง: "))

    damage = weapons[weapon] * atk_round
    monsters[monster_name] -= damage
    print(f"คุณใช้ {weapon} โจมตี {monster_name} ได้ {damage} ดาเมจ")

    if monsters[monster_name] == 0:
        print(f"{monster_name} ตายแล้ว!")
        monsters[monster_name] = 0

    elif monsters[monster_name] < 0:
        print(f"{monster_name} ดาเมจเกินทำให้มอนสเตอร์ดูดพลังเหลือเลือด 20")
        break

    if all(hp == 0 for hp in monsters.values()):
        print("คุณกำจัดมอนสเตอร์ทั้งหมดแล้ว ชนะแล้ว")
        break
else:
    print("หมดรอบการต่อสู้แล้ว มอนสเตอร์ยังไม่ตาย")