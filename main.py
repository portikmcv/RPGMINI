from character import Character,Warrior,Mage
from battle import battle
from save_system import save_character,load_char
import random
from time import sleep




def main_main():
    player = Warrior('Hero',100,15)
    while True:
        print('--------------------\n1. สู้กับมอนสเตอร์\n2. Save\n3. load\n4. Quit\n--------------------')
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print('please INPUT 1-4')
            continue
        
        list_of_choice = [1,2,3,4]
        if choice and choice in list_of_choice:
            if choice == 1:
                Bandit = Character('Bandit',30,5)
                Goblin = Character('Goblin',50,15)
                l = [Goblin,Bandit]
                enemy = random.choice(l)
                print(f'--------------------\nคู่ต่อสู้ของคุณ:{enemy.class_name}')
                sleep(1)
                battle(player,enemy)
            elif choice == 2:
                save_character(player,'save.json')
            elif choice == 3:
                player = load_char('save.json')
            else:break
        else:print("please INPUT NUMBER 1-4")
                   
        



if __name__ == '__main__':
    main_main()

