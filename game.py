import random
from goblin import Goblin
from hero import Hero
from boss import Boss
def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Golden Knight")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "orange") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1

        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        total_damage += damage

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
                total_damage += damage
    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
        hero.health=hero.health+200
        print(f"\nThe hero has drank a health potion, and is back at full health")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"Total rounds fought: {rounds}")
    print(f"\nTotal damage dealt: {total_damage}")

    if hero.is_alive():
        print("The deadly Smaug has flew into the arena!")
        boss=Boss("Smaug")
        rounds=0
        while hero.is_alive() and boss.is_alive():
            damage=boss.attack()
            hero.health-=damage
            if rounds > 10:
                boss.health=0
                print("Smaug has been struck in the heart!")
            else:rounds=rounds+1
    if hero.is_alive():
        print(f"\nThe hero has defeated SMAUG!!! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has lost to the legendary SMAUG :(")    

    print(f"Total rounds fought: {rounds}")    
    # Final tally of goblins defeated


if __name__ == "__main__":
    main()
