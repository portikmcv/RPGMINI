from character import Warrior,Character



import random
def battle(f1,f2):
    attacker, defender = random.choice([(f1, f2), (f2, f1)])
    while attacker.is_alive and defender.is_alive:
               attacker.attack(defender)
               
               if not defender.is_alive:
                       break
               defender.attack(attacker)
               
    check = attacker.is_alive
    if check:
            attacker.gainxp(1000)
            print(f'------------------\n{defender.class_name} has lost!')
    else:
        defender.gainxp(1000)
        print(f'------------------\n{attacker.class_name } has lost!')          
               



if __name__ == '__main__':
       print('hello')


