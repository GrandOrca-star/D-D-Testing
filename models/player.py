import random

def roll_dice(sides=20, modifier=0):
    return random.randint(1, sides) + modifier

class Player:
    def __init__(self, name, char_class, hp, ac, str_mod, potions=2):
        self.name = name
        self.char_class = char_class
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac
        self.str_mod = str_mod
        self.potions = potions

    def attack(self, target):
        print(f"\n⚔️ {self.name} กำลังโจมตี {target.name}!")
        attack_roll = roll_dice(20, self.str_mod)
        print(f"🎯 ผลการทอยโจมตี: {attack_roll} (เทียบกับ AC ศัตรู: {target.ac})")

        if attack_roll >= target.ac:
            damage = roll_dice(6, self.str_mod)
            target.current_hp -= damage
            # แจ้งมอนสเตอร์ว่าโดนโจมตีแล้ว (เผื่อเป็น Passive Monster)
            if hasattr(target, 'is_provoked'):
                target.is_provoked = True
            print(f"💥 โจมตีโดน! ทำความเสียหายได้ {damage} หน่วย")
            print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
        else:
            print(f"🛡️ โจมตีพลาด! {target.name} ป้องกันไว้ได้")

    def heal(self):
        if self.potions > 0:
            heal_amount = roll_dice(8, 2)
            self.current_hp = min(self.max_hp, self.current_hp + heal_amount)
            self.potions -= 1
            print(f"\n🧪 {self.name} ดื่มน้ำยาฮีล! ฟื้นฟู HP {heal_amount} หน่วย")
            print(f"❤️ HP ปัจจุบัน: {self.current_hp}/{self.max_hp} (เหลือน้ำยาฮีล: {self.potions} ขวด)")
        else:
            print(f"\n❌ {self.name} ไม่มีน้ำยาฮีลเหลือแล้ว!")
