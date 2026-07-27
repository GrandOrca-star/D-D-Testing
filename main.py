import random

# --- 1. ระบบทอยลูกเต๋า ---
def roll_dice(sides=20, modifier=0):
    roll = random.randint(1, sides)
    total = roll + modifier
    return total

# --- 2. ระบบตัวละคร D&D ---
class Character:
    def __init__(self, name, char_class, hp, ac, str_mod, potions=2):
        self.name = name
        self.char_class = char_class
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac             # Armor Class (ค่าเกราะ)
        self.str_mod = str_mod   # ค่า Strength Modifier
        self.potions = potions   # จำนวนน้ำยาฮีลที่มี

    def attack(self, target):
        """ฟังก์ชันโจมตีศัตรู"""
        print(f"\n⚔️ {self.name} กำลังโจมตี {target.name}!")
        attack_roll = roll_dice(20, self.str_mod)
        print(f"🎯 ผลการทอยโจมตี: {attack_roll} (เทียบกับ AC ศัตรู: {target.ac})")

        if attack_roll >= target.ac:
            damage = roll_dice(6, self.str_mod) # ความเสียหาย d6 + STR
            target.current_hp -= damage
            print(f"💥 โจมตีโดน! ทำความเสียหายได้ {damage} หน่วย")
            print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
        else:
            print(f"🛡️ โจมตีพลาด! {target.name} ป้องกันไว้ได้")

    def heal(self):
        """ฟังก์ชันดื่มยาเพิ่ม HP"""
        if self.potions > 0:
            heal_amount = roll_dice(8, 2) # ฮีล d8 + 2
            self.current_hp = min(self.max_hp, self.current_hp + heal_amount)
            self.potions -= 1
            print(f"\n🧪 {self.name} ดื่มน้ำยาฮีล! ฟื้นฟู HP {heal_amount} หน่วย")
            print(f"❤️ HP ปัจจุบัน: {self.current_hp}/{self.max_hp} (เหลือน้ำยาฮีล: {self.potions} ขวด)")
        else:
            print(f"\n❌ {self.name} ไม่มีน้ำยาฮีลเหลือแล้ว!")

# --- 3. ฟังก์ชันสุ่มศัตรู (Random Encounter) ---
def get_random_monster():
    """สร้างและคืนค่ามอนสเตอร์แบบสุ่ม"""
    monsters_data = [
        {"name": "Goblin", "class": "Goblinoid", "hp": 12, "ac": 11, "str_mod": 1},
        {"name": "Skeleton", "class": "Undead", "hp": 15, "ac": 12, "str_mod": 2},
        {"name": "Orc", "class": "Humanoid", "hp": 22, "ac": 13, "str_mod": 3}
    ]
    
    # สุ่มเลือกข้อมูลมอนสเตอร์ 1 ตัว
    data = random.choice(monsters_data)
    
    # สร้างเป็น Object ตัวละคร
    return Character(
        name=data["name"],
        char_class=data["class"],
        hp=data["hp"],
        ac=data["ac"],
        str_mod=data["str_mod"]
    )

# --- 4. เริ่มต้นการเล่น ---
print("=== D&D Interactive Game with Random Encounter ===")

# สร้างตัวละครผู้เล่น
hero = Character(name="Arthur", char_class="Fighter", hp=25, ac=14, str_mod=3, potions=2)

# สุ่มศัตรูขึ้นมา 1 ตัว!
goblin = get_random_monster() # (ใช้ตัวแปรชื่อเดิมเพื่อให้ลูปทำงานเหมือนเดิมได้)
print(f"\n⚠️ คุณเดินเข้าไปในดันเจี้ยน และเผชิญหน้ากับ **{goblin.name}** ({goblin.char_class})!")

round_num = 1
escaped = False

while hero.current_hp > 0 and goblin.current_hp > 0:
    print(f"\n==================== Round {round_num} ====================")
    print(f"👤 {hero.name} (HP: {hero.current_hp}/{hero.max_hp} | Potions: {hero.potions})")
    print(f"👹 {goblin.name} (HP: {goblin.current_hp}/{goblin.max_hp})")
    print("--------------------------------------------------")
    print("เลือกคำสั่ง:")
    print("1. ⚔️ โจมตี (Attack)")
    print("2. 🧪 ดื่มยาฮีล (Use Potion)")
    print("3. 🏃 วิ่งหนี (Run - ทอย d20 >= 10)")
    
    choice = input("กรอกหมายเลขคำสั่ง (1-3): ")

    if choice == "1":
        hero.attack(goblin)
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
    else:
        print("\n⚠️ เลือกคำสั่งไม่ถูกต้อง! เสีย lượt ฟรีในรอบนี้")

    # ถ้าศัตรูยังไม่ตาย และผู้เล่นไม่ได้หนี ให้ศัตรูสวนกลับ
    if goblin.current_hp > 0 and not escaped:
        goblin.attack(hero)

    round_num += 1

# --- 5. สรุปผลการต่อสู้ ---
print("\n==================== การต่อสู้สิ้นสุดลง ====================")
if escaped:
    print(f"💨 {hero.name} หลบหนีจากการต่อสู้ได้สำเร็จ!")
elif hero.current_hp > 0:
    print(f"🎉 {hero.name} เอาชนะ {goblin.name} ได้สำเร็จ!")
else:
    print(f"💀 {hero.name} พ่ายแพ้ในการต่อสู้...")
