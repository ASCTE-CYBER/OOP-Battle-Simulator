import random
from goblin import Goblin
from hero import Hero
from boss import Basilisk

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]


    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    #keep track of rounds
    rounds = 0
    hero_damage = 0
    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        hero_damage += damage
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


    if hero.is_alive():
        basilisk = Basilisk("Basilisk")
        print("boss battle")
        while hero.is_alive() and basilisk.is_alive():
            damage = hero.strike()
            basilisk.take_damage(damage)
            damage = basilisk.attack()
            hero.receive_damage(damage)
        if hero.is_alive():
            print(f"\nThe hero has defeated the boss! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    if hero.is_alive():
        print("boss time")
        basilisk = Basilisk("Basilisk")
        while hero.is_alive() and basilisk.is_alive():
            damage = hero.strike()
            basilisk.take_damage(damage)
            damage = basilisk.attack()
            hero.receive_damage(damage)
        if hero.is_alive():
            print("yay you defeated the boss")
        else:
            print("you lost to the boss")
    print("Mr speak was here")

    print("Total rounds: " +  str(rounds))
    print("Total damage by hero: " + str(hero_damage))
    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")



if __name__ == "__main__":
    main()
