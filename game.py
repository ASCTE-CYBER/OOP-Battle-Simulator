import random
from goblin import Goblin
from hero import Hero
from Boss import Dragon

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Nightwing")
   

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}" ,"green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    rounds= 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds +=1
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
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
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    print(f"total rounds fought:{rounds}")
    # Final tally of goblins defeated
    if hero.is_alive():
        print("King dragon fight time")
        king=Dragon("Dragon")
        while hero.is_alive() and king.is_alive:
            damage=hero.strike()
            king.take_damage(damage)
            damage=king.attack()
            hero.receive_damage(damage)
    if hero.is_alive:
        print(f"\nFor centuries the dragon king and his goblin minions have plundered many towns, and those who try to stop them have failed , until now.")
        print(f"\nThank you kind warrior and may your quest bring you much luck.")
    else:
        print(f"\nThe dragon won you.For shame.")

    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("Mr speak was here 😎")
if __name__ == "__main__":
    main()
