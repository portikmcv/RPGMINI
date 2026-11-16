class Item:
    def __init__(self,name,effect,value):
        self.name = name
        self.effect = effect
        self.value = value

    def use(self,target):
        if self.effect == 'heal':
            target.current_hp += self.value
            print(f'{target.class_name} ใช้ {self.name} ฟื้นฟู HP {self.value} หน่วย!')
        elif self.effect == 'attack_boost':
            target.attack_power += self.value
            print(f'{target.class_name} ใช้ {self.name} Attack Boost {self.value} หน่วย!')

    def __str__(self):
        return f"{self.name} ({self.effect} + {self.value})"
    def __repr__(self):
        return self.__str__()
