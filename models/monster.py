import random

def roll_dice(sides=20, modifier=0):
    return random.randint(1, sides) + modifier

class Monster:
    def __init__(self, name, char_class, hp, ac, str_mod, is_passive=False):
        self.name = name
        self.char_class = char_class
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac
        self.str_mod = str_mod
        self.is_passive = is_passive
        self.is_provoked = False  # โดนยั่วยุ/โดนโจมตีหรือยัง

    def take_turn(self, target):
        """จัดการ Action ในรอบของมอนสเตอร์"""
        if self.is_passive and not self.is_provoked:
            print(f"\n🕊️ {self.name} ยืนมองคุณเฉยๆ อย่างเป็นมิตร (ยังไม่โจมตี)...")
        else:
            self.attack(target)

    def attack(self, target):
        print(f"\n⚔️ {self.name} กำลังโจมตี {target.name}!")
        attack_roll = roll_dice(20, self.str_mod)
        
        if attack_roll >= target.ac:
            damage = roll_dice(6, self.str_mod)
            target.current_hp -= damage
            print(f"💥 {self.name} โจมตีโดน! ทำความเสียหายได้ {damage} หน่วย")
            print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
        else:
            print(f"🛡️ {self.name} โจมตีพลาด!")

def get_random_monster():
    """สุ่มมอนสเตอร์ที่มีทั้งแบบสายบวก และ Passive"""
    monsters_data = [
        {"name": "Goblin", "class": "Goblinoid", "hp": 12, "ac": 11, "str_mod": 1, "is_passive": False},
        {"name": "Orc", "class": "Humanoid", "hp": 22, "ac": 13, "str_mod": 3, "is_passive": False},
        {"name": "Giant Capybara", "class": "Beast", "hp": 18, "ac": 10, "str_mod": 0, "is_passive": True},
        {"name": "Wandering Merchant Goat", "class": "Beast", "hp": 10, "ac": 12, "str_mod": 1, "is_passive": True}
    ]
    data = random.choice(monsters_data)
    return Monster(
        name=data["name"],
        char_class=data["class"],
        hp=data["hp"],
        ac=data["ac"],
        str_mod=data["str_mod"],
        is_passive=data["is_passive"]
    )
