import random
from goblin import Goblin
from hero import Hero
from boss import mrs_wright
import hero 

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Talking Ben")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    # Battle Loop 
    round = 0
    hero_damage = 0 

    boss_beat = False

    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):

        print("\nNew Round!")
        print("Round: " + str(round + 1))
        round = round + 1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        hero_damage = hero_damage + 1 
        print(f"Talking Ben attacks {target_goblin.name} for {damage} damage!")
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

#boss loop 
    if hero.is_alive():
        print("BOSS BATTLE")
        print("\nNew Round!")
        print("Round: " + str(round + 1))
        round = round + 1
        Mrs_Wright = mrs_wright("Mrs_Wright")
        while hero.is_alive() and Mrs_Wright.is_alive():
            damage = hero.strike()
            Mrs_Wright.take_damage(damage)
            damage = Mrs_Wright.attack()
            hero.receive_damage(damage)


    if hero.is_alive():
        boss_beat = True

 # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated the boss! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")


    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("Battle Summary")
    print(f"\nTotal damage: {hero_damage}")
    print(f"\nRounds Survived: {round}")


if __name__ == "__main__":
    main()