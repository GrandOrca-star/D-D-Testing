import random

# --- 1. ระบบทอยลูกเต๋า ---
def roll_dice(sides=20, modifier=0):
    roll = random.randint(1, sides)
    total = roll + modifier
    return total

# --- 2. ระบบตัวละคร D&D ---
class Character:
    def __init__(self, name, char_class, hp, ac, str_mod):
        self.name = name
        self.char_class = char_class
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac             # Armor Class (ค่าเกราะ)
        self.str_mod = str_mod   # ค่า Strength Modifier (ความแรงในการโจมตี)

    def attack(self, target):
        """ฟังก์ชันโจมตีศัตรู"""
        print(f"\n⚔️ {self.name} กำลังโจมตี {target.name}!")
        
        # ทอย d20 + ค่า Strength
        attack_roll = roll_dice(20, self.str_mod)
        print(f"🎯 ผลการทอยโจมตี: {attack_roll} (เทียบกับ AC ศัตรู: {target.ac})")

        # เช็กว่าตีโดนไหม ( Attack Roll >= AC )
        if attack_roll >= target.ac:
            damage = roll_dice(6, self.str_mod) # ความเสียหาย d6 + STR
            target.current_hp -= damage
            print(f"💥 โจมตีโดน! ทำความเสียหายได้ {damage} หน่วย")
            print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
        else:
            print(f"🛡️ โจมตีพลาด! {target.name} ป้องกันไว้ได้")

# --- 3. จำลองการต่อสู้ (Testing) ---
print("=== D&D Combat Testing ===")

# สร้างตัวละครผู้เล่น และ มอนสเตอร์
hero = Character(name="Arthur", char_class="Fighter", hp=20, ac=14, str_mod=3)
goblin = Character(name="Goblin", char_class="Monster", hp=10, ac=11, str_mod=1)

# ทดสอบ Hero โจมตี Goblin
hero.attack(goblin)
# --- 3. จำลองการต่อสู้สลับรอบ (Turn-Based Battle) ---
print("=== D&D Combat Loop Testing ===")

# สร้างตัวละคร Arthur (Hero) และ Goblin
hero = Character(name="Arthur", char_class="Fighter", hp=20, ac=14, str_mod=3)
goblin = Character(name="Goblin", char_class="Monster", hp=12, ac=11, str_mod=1)

# วนลูปต่อสู้จนกว่าจะมีคน HP หมด
round_num = 1
while hero.current_hp > 0 and goblin.current_hp > 0:
    print(f"\n--- Round {round_num} ---")
    
    # รอบของ Hero โจมตี Goblin
    hero.attack(goblin)
    
    # เช็กว่า Goblin ตายหรือยัง ถ้ายังไม่ตาย ให้ Goblin สวนกลับ
    if goblin.current_hp > 0:
        goblin.attack(hero)
        
    round_num += 1

# สรุปผลการต่อสู้
print("\n=== การต่อสู้สิ้นสุดลง ===")
if hero.current_hp > 0:
    print(f"🎉 {hero.name} เป็นฝ่ายชนะ!")
else:
    print(f"💀 {hero.name} ถูกพ่ายแพ้ในการต่อสู้...")
