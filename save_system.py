import json
from character import Warrior,Mage

def save_character(character,filename):
    db = character.to_dict()
    with open(filename,"w") as f:
        json.dump(db,f,indent=2)
    print(f'Save! {filename}')

def load_char(filename):
    try:
        with open(filename,"r") as f:
            data = json.load(f)
        char = Warrior(data['class_name'],data['max_hp'],data['attack_power'])
        char.current_hp = data['current_hp']
        char.level = data['level']
        char.xp = data['xp']
        print(f"------------------------------\nloaded character \nCurrent Level:{char.level}")
        
        return char 
    except FileNotFoundError:
        print('No Files')
        return None





a = Warrior("Warriors",50,50)

if __name__ == '__main__':
    save_character(a,'database')
    char = load_char('database')
    char.gainxp(1000)
    save_character(char,'database')
