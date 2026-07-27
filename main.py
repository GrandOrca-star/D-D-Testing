import random
# 1. ดึง Class และฟังก์ชันจากไฟล์ที่เราแยกไว้มาใช้งาน
from player import Player, roll_dice
from monster import get_random_monster

# --- เริ่มต้นการเล่น ---
print("=== D&D Game: Refactored Edition ===")

# สร้างตัวละครผู้เล่น
hero = Player(name="Arthur", char_class="Fighter", hp=25, ac=14, str_mod=3, potions=2)

# สุ่มศัตรูขึ้นมา 1 ตัว (มีโอกาสเจอทั้งแบบ Aggressive และ Passive)
monster = get_random_monster()

if monster.is_passive:
    print(f"\n🌿 คุณพบกับ **{monster.name}** ({monster.char_class}) มันดูสงบและไม่มีท่าทีคุกคาม")
else:
    print(f"\n⚠️ คุณเผชิญหน้ากับ **{monster.name}** ({monster.char_class}) มันแยกเขี้ยวใส่คุณ!")

round_num = 1
escaped = False

# --- Game Loop ---
while hero.current_hp > 0 and monster.current_hp > 0:
    print(f"\n==================== Round {round_num} ====================")
    print(f"👤 {hero.name} (HP: {hero.current_hp}/{hero.max_hp} | Potions: {hero.potions})")
    print(f"👹 {monster.name} (HP: {monster.current_hp}/{monster.max_hp})")
    print("--------------------------------------------------")
    print("เลือกคำสั่ง:")
    print("1. ⚔️ โจมตี (Attack)")
    print("2. 🧪 ดื่มยาฮีล (Use Potion)")
    print("3. 🏃 วิ่งหนี (Run)")
    
    choice = input("กรอกหมายเลขคำสั่ง (1-3): ")

    if choice == "1":
        hero.attack(monster)
    elif choice == "2":
        hero.heal()
    elif choice == "3":
        print(f"\n🏃 {hero.name} พยายามวิ่งหนี!")
        run_roll = roll_dice(20, 0)
        if run_roll >= 10:
            print(f"💨 ทอยได้ {run_roll} (>=10)! หนีสำเร็จ!")
            escaped = True
            break
        else:
            print(f"🚫 ทอยได้ {run_roll} (<10)! หนีไม่พ้น!")
            # ถ้าพยายามหนี มอนสเตอร์ Passive จะเริ่มสงสัยและมองว่าเราเป็นศัตรูทันที!
            monster.is_provoked = True
    else:
        print("\n⚠️ เลือกคำสั่งไม่ถูกต้อง! เสีย lượt ฟรีในรอบนี้")

    # เทิร์นของมอนสเตอร์ (ถ้าเป็น Passive และยังไม่โดนเปิด มันจะไม่ตี)
    if monster.current_hp > 0 and not escaped:
        monster.take_turn(hero)

    round_num += 1

# --- สรุปผลการต่อสู้ ---
print("\n==================== การต่อสู้สิ้นสุดลง ====================")
if escaped:
    print(f"💨 {hero.name} หลบหนีจากการต่อสู้ได้สำเร็จ!")
elif hero.current_hp > 0:
    print(f"🎉 {hero.name} เอาชนะ {monster.name} ได้สำเร็จ!")
else:
    print(f"💀 {hero.name} พ่ายแพ้ในการต่อสู้...")
