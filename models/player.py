import random

def roll_dice(sides=20, modifier=0):
    return random.randint(1, sides) + modifier

class Player:
    def __init__(self, name, char_class, hp, ac, str_mod):
        self.name = name
        self.char_class = char_class
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac
        self.str_mod = str_mod
        
        # --- ระบบ Level & EXP ---
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 20
        
        # --- ระบบ กระเป๋าไอเท็ม (Inventory) ---
        self.inventory = {
            "Potion": 2  # เริ่มต้นมียาฮีล 2 ขวด
        }
        
        # --- ระบบ สกิล ---
        self.mp = 10
        self.max_mp = 10

    def gain_exp(self, amount):
        """รับ EXP และเช็กการเลเวลอัป"""
        self.exp += amount
        print(f"\n✨ {self.name} ได้รับ EXP +{amount} (ปัจจุบัน: {self.exp}/{self.exp_to_next_level})")
        
        if self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        """การอัปเลเวล"""
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5) # เพิ่มเกณฑ์ EXP ชั้นถัดไป
        
        hp_increase = roll_dice(6, 2)
        self.max_hp += hp_increase
        self.current_hp = self.max_hp  # ฮีลเต็มเมื่อเลเวลอัป
        self.max_mp += 5
        self.mp = self.max_mp
        self.str_mod += 1

        print(f"\n🎉🎉🎉 LEVEL UP! {self.name} บรรลุ เลเวล {self.level}! 🎉🎉🎉")
        print(f"❤️ Max HP +{hp_increase} (เป็น {self.max_hp}) | 🗡️ STR +1 (เป็น {self.str_mod}) | 💧 Max MP +5")

    def attack(self, target):
        """การโจมตีธรรมดา"""
        print(f"\n⚔️ {self.name} ฟัน {target.name}!")
        attack_roll = roll_dice(20, self.str_mod)
        print(f"🎯 ผลทอยโจมตี: {attack_roll} (AC ศัตรู: {target.ac})")

        if attack_roll >= target.ac:
            damage = roll_dice(6, self.str_mod)
            target.current_hp -= damage
            if hasattr(target, 'is_provoked'):
                target.is_provoked = True
            print(f"💥 โจมตีโดน! ทำความเสียหาย {damage} หน่วย")
            print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
        else:
            print(f"🛡️ โจมตีพลาด!")

    def use_skill(self, target):
        """ระบบใช้สกิลพิเศษ (Power Strike)"""
        cost = 4
        if self.mp >= cost:
            self.mp -= cost
            print(f"\n🔥 {self.name} ใช้สกิล [Power Strike]! (ใช้ MP {cost})")
            attack_roll = roll_dice(20, self.str_mod + 2) # สกิลทอยโดนง่ายขึ้น
            
            if attack_roll >= target.ac:
                damage = roll_dice(8, self.str_mod * 2) # สกิลตีแรงขึ้น (d8 + STR*2)
                target.current_hp -= damage
                if hasattr(target, 'is_provoked'):
                    target.is_provoked = True
                print(f"💥💥 รุนแรงมาก! ทำความเสียหายหนัก {damage} หน่วย!")
                print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
            else:
                print(f"🛡️ ศัตรูกลิ่นตัวทัน หลบสกิลได้!")
        else:
            print(f"\n❌ MP ไม่พอ! (ต้องการ {cost} MP | มีอยู่ {self.mp} MP)")
            return False
        return True

    def use_item(self):
        """ระบบใช้ไอเท็มจาก Inventory"""
        print("\n🎒 --- กระเป๋าไอเท็ม ---")
        items = list(self.inventory.keys())
        for idx, item_name in enumerate(items, 1):
            print(f"{idx}. {item_name} (เหลือ: {self.inventory[item_name]})")
        print("0. ย้อนกลับ")
        
        choice = input("เลือกไอเท็มที่จะใช้: ")
        if choice == "1" and self.inventory.get("Potion", 0) > 0:
            heal_amount = roll_dice(8, 2)
            self.current_hp = min(self.max_hp, self.current_hp + heal_amount)
            self.inventory["Potion"] -= 1
            print(f"\n🧪 ดื่ม Potion! ฟื้นฟู HP {heal_amount} หน่วย")
            print(f"❤️ HP ปัจจุบัน: {self.current_hp}/{self.max_hp}")
            return True
        elif choice == "0":
            return False
        else:
            print("\n❌ ไอเท็มหมดหรือไม่ถูกต้อง!")
            return False
