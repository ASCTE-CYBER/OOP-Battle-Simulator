import random
from goblin import Goblin
from hero import Hero
from BOSS import MegaKnight
from babyelf import BabyElf

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Tachanka")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    defeated_goblins = 0
    rounds = 0
    total_damage = 0
    boss = True
    # Keep track of how many goblins were defeated

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        

        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total_damage += damage
        rounds += 1
            

        
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
    if hero.is_alive():
        print("Boss time!")
        megaKnight = MegaKnight("Mega Knight", "black")
        while hero.is_alive() and megaKnight.is_alive():
            damage = hero.strike()
            megaKnight.take_damage(damage)

            damage = megaKnight.attack()
            hero.receive_damage(damage)
        if hero.is_alive():
            print(f"\nThe hero has defeated the Boss! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("Battle Summary:")
    print(f"Total rounds fought: {rounds}")
    print(f"Total damage dealt: {total_damage}")

if __name__ == "__main__":
    main()
