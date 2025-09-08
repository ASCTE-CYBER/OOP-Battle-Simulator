import random
from goblin import Goblin
from hero import Hero
from boss import The_Hunter

def does_crit():
    possability = random.randint(1,999999999)
    if possability == 72:
        return True
    else:
        return False

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("CREATURE")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Wolf {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0 

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike(does_crit())
        print(f"{hero.name} attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over blaeg. (｡•́︿•̀｡)")

    print("HUNTER FOUND")
    Hunter = The_Hunter("Jeff")
    is_here = True
    while hero.is_alive() and Hunter.is_alive() and is_here == True:
        damage = Hunter.attack()
        if damage == False:
            is_here = False
        else: 
            print(f"{Hunter.name} attacks hero for {damage} damage!")
            hero.receive_damage(damage)
            damage = hero.strike(does_crit())
            print(f"{hero.name} attacks hero for {damage} damage!")
            Hunter.take_damage(damage)

    if is_here == False:
        print(f"The hunter ran")
    elif hero.is_alive:
        print("The hunter was devoured")
    else:
        print(f"{hero.name} has retreated")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
