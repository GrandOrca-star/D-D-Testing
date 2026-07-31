import random
from models.player import Player, roll_dice
from models.monster import get_random_monster

print("=== D&D Game: Skill & EXP Update ===")

hero = Player(name="Arthur", char_class="Fighter", hp=25, ac=14, str_mod=3)
monster = get_random_monster()

if monster.is_passive:
    print(f"\n🌿 คุณพบกับ **{monster.name}** ({monster.char_class}) มันดูสงบและไม่มีท่าทีคุกคาม")
else:
    print(f"\n⚠️ คุณเผชิญหน้ากับ **{monster.name}** ({monster.char_class}) มันแยกเขี้ยวใส่คุณ!")

round_num = 1
escaped = False

while hero.current_hp > 0 and monster.current_hp > 0:
    print(f"\n==================== Round {round_num} ====================")
    print(f"👤 {hero.name} (Lv.{hero.level}) | HP: {hero.current_hp}/{hero.max_hp} | MP: {hero.mp}/{hero.max_mp}")
    print(f"👹 {monster.name} | HP: {monster.current_hp}/{monster.max_hp}")
    print("--------------------------------------------------")
    print("เลือกคำสั่ง:")
    print("1. ⚔️ โจมตีธรรมดา (Attack)")
    print("2. 🔥 ใช้สกิล [Power Strike] (ใช้ 4 MP)")
    print("3. 🎒 เปิดกระเป๋าใช้ไอเท็ม (Item)")
    print("4. 🏃 วิ่งหนี (Run)")
    
    choice = input("กรอกหมายเลขคำสั่ง (1-4): ")
    action_taken = True

    if choice == "1":
        hero.attack(monster)
    elif choice == "2":
        action_taken = hero.use_skill(monster)
    elif choice == "3":
        action_taken = hero.use_item()
    elif choice == "4":
        print(f"\n🏃 {hero.name} พยายามวิ่งหนี!")
        run_roll = roll_dice(20, 0)
        if run_roll >= 10:
            print(f"💨 ทอยได้ {run_roll} (>=10)! หนีสำเร็จ!")
            escaped = True
            break
        else:
            print(f"🚫 ทอยได้ {run_roll} (<10)! หนีไม่พ้น!")
            monster.is_provoked = True
    else:
        print("\n⚠️ เลือกคำสั่งไม่ถูกต้อง!")
        action_taken = False

    # ถ้าแอ็กชันสำเร็จ ศัตรูถึงจะตอบโต้ในเทิร์นของมัน
    if action_taken and monster.current_hp > 0 and not escaped:
        monster.take_turn(hero)

    round_num += 1

print("\n==================== การต่อสู้สิ้นสุดลง ====================")
if escaped:
    print(f"💨 {hero.name} หลบหนีสำเร็จ!")
elif hero.current_hp > 0:
    print(f"🎉 {hero.name} เอาชนะ {monster.name} ได้สำเร็จ!")
    # แจก EXP เมื่อชนะ!
    hero.gain_exp(monster.exp_reward)
else:
    print(f"💀 {hero.name} พ่ายแพ้ในการต่อสู้...")
