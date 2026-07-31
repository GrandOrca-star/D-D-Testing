import random

def roll_dice(sides=20, modifier=0):
    return random.randint(1, sides) + modifier

class Monster:
    def __init__(self, name, char_class, hp, ac, str_mod, exp_reward, is_passive=False):
        self.name = name
        self.char_class = char_class
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac
        self.str_mod = str_mod
        self.exp_reward = exp_reward  # EXP ที่มอบให้เมื่อตาย
        self.is_passive = is_passive
        self.is_provoked = False

    def take_turn(self, target):
        if self.is_passive and not self.is_provoked:
            print(f"\n🕊️ {self.name} ยืนมองคุณเฉยๆ อย่างเป็นมิตร...")
        else:
            self.attack(target)

    def attack(self, target):
        print(f"\n⚔️ {self.name} โจมตี {target.name}!")
        attack_roll = roll_dice(20, self.str_mod)
        
        if attack_roll >= target.ac:
            damage = roll_dice(6, self.str_mod)
            target.current_hp -= damage
            print(f"💥 {self.name} โจมตีโดน! ทำความเสียหาย {damage} หน่วย")
            print(f"❤️ {target.name} เหลือ HP: {max(0, target.current_hp)}/{target.max_hp}")
        else:
            print(f"🛡️ {self.name} โจมตีพลาด!")

def get_random_monster():
    monsters_data = [
        {"name": "Goblin", "class": "Goblinoid", "hp": 12, "ac": 11, "str_mod": 1, "exp": 10, "is_passive": False},
        {"name": "Orc", "class": "Humanoid", "hp": 22, "ac": 13, "str_mod": 3, "exp": 25, "is_passive": False},
        {"name": "Giant Capybara", "class": "Beast", "hp": 18, "ac": 10, "str_mod": 0, "exp": 15, "is_passive": True},
        {"name": "Wandering Goat", "class": "Beast", "hp": 10, "ac": 12, "str_mod": 1, "exp": 8, "is_passive": True}
    ]
    data = random.choice(monsters_data)
    return Monster(
        name=data["name"],
        char_class=data["class"],
        hp=data["hp"],
        ac=data["ac"],
        str_mod=data["str_mod"],
        exp_reward=data["exp"],
        is_passive=data["is_passive"]
    )
