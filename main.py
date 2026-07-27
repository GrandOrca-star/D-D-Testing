import random

def roll_dice(sides=20, modifier=0):
    """ฟังก์ชันทอยลูกเต๋ากำหนดจำนวนหน้า ( default คือ d20 ) พร้อมบวกค่า Modifier"""
    roll = random.randint(1, sides)
    total = roll + modifier
    print(f"🎲 ทอยได้ {roll} (Modifier: +{modifier}) -> ผลลัพธ์รวม: {total}")
    return total

# ทดสอบรันคำสั่งทอยเต๋า D&D
print("=== D&D Dice Roller Testing ===")
roll_dice(20, 3) # ทอย d20 + 3 (เช่น ค่า Attack Roll)
roll_dice(6, 2)  # ทอย d6 + 2  (เช่น ค่า Damage ของดาบ)
