from item import Item
class Character:
    def __init__(self,class_name,max_hp,attack_power):
        self.class_name = class_name
        #BASE STATUS
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_power = attack_power
        #BASE XP
        self.level = 1
        self.xp = 0
        self.xp_tolvlup = 100
        #ITEM
        self.inventory = []

    #TODICT
    def to_dict(self):
        """แปลงเป็น dict เพื่อ save ข้อมูล"""
        return {
            'class_name':self.class_name,
            'max_hp':self.max_hp,
            'current_hp':self.current_hp,
            'attack_power':self.attack_power,
            'level':self.level,
            'xp':self.xp
        }
    #ITEM SECTION
    def add_item(self,item):
        self.inventory.append(item)
        print(f"ได้รับ{item.name}")

    def use_item(self,item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.use(self)
                self.inventory.remove(item)
        else:
            print(f'ไม่พบ Item ชื่อ {item_name}')

        
    #XP SYSTEM
    def gainxp(self,amount):
        self.xp += amount
        a = self.level
        while self.xp >= self.xp_tolvlup:
            self.xp -= self.xp_tolvlup
            self.lvlup()
        b = self.level
        if a != b:
            print(f'---level up---\n',f'You are now level {a} -> {b}')
            

    def lvlup(self):
        self.level += 1
        self.max_hp += 20
        self.current_hp += 20
        self.attack_power +=5
        self.xp_tolvlup += 50
        


        
        
        
    #Attack กับ TAKE DAMAGE ---
    def attack(self,target):
        target.take_damage(self.attack_power)

    def take_damage(self,amount):
        self.current_hp-=amount

    #OTHER MTHOD CAN CHANGE THIS SO WE USE PROPERTY AND SETTER
    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self,value):
        if value <= 0:
            value = 0
        elif value > self.max_hp:
            value = self.max_hp
        self._current_hp = value

    @property
    def is_alive(self):
        return self.current_hp > 0

class Warrior(Character):
    def __init__(self, class_name, max_hp, attack_power):
        super().__init__(class_name, max_hp, attack_power)
        self.power_strike_count = 3

    #SPECIAL SKILL
    def power_strike(self,target):
        if self.power_strike_count > 0:
            dmg = self.attack_power*2
            target.take_damage(dmg)
            self.power_strike_count -= 1
        else:print('ใช้ไม่ได้แล้ว')

class Mage(Character):
    def __init__(self, class_name, max_hp, attack_power,max_mana):
        super().__init__(class_name, max_hp, attack_power)
        self.max_mana = max_mana
        self.current_mana = max_mana

    #SPECIAL SKILL
    def fireball(self,target):
        if self.current_mana >= 20:
            dmg = self.attack_power*3
            target.take_damage(dmg)
            self.current_mana-=20
        else:
            print('No mana left!')
            
if __name__ == "__main__":
    warrior = Warrior('Warrior',200,10)
    mage = Mage('Mage',50,20,100)
    potion = Item('ยาฮีล','heal',30)
    warrior.add_item(potion)
    warrior.add_item(potion)
    print(warrior.inventory)

    