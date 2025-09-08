import random
from goblin import Goblin
from hero import Hero
from boss import Giant


def main():
    rounds=0
    totdamage=0

    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("bob")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", 'green') for i in range(10)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        #print("\nNew Round!")
        rounds+=1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        #print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        totdamage+=damage

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                #print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
        print("You survived "+str(rounds)+" rounds.")
        print("You hit for a total of "+str(totdamage)+" damage.")

    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
        print("You survived "+str(rounds)+" rounds.")
        print("You hit for a total of "+str(totdamage)+" damage.")
        
    if hero.is_alive():      
        fred=Giant('fred')

        print("Boss time")
        while hero.is_alive() and fred.is_alive():
            rounds+=1
            #print("New Round!")
            damage=hero.strike()
            fred.take_damage(damage)
            damage=fred.attack()
            hero.receive_damage(damage)
            
            
        if hero.is_alive():
            print('fred is dead') 
        else:
            print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
            print("You survived "+str(rounds)+" rounds.")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
