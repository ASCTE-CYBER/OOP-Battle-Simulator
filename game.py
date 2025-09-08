import random
from goblin import Goblin
from hero import Hero
from boss import Boss

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]


    # Keep track of how many goblins were defeated
    defeated_goblins = 0
<<<<<<< Updated upstream

    # Battle Loop 
=======
    total_damage = 0
    rounds_survived = 0

    # Battle Loop
>>>>>>> Stashed changes
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
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
<<<<<<< Updated upstream
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
=======
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ Time for the boss fight!")
        boss = Boss("Super hard boss")
        hero.health = 150
        while hero.is_alive() and boss.is_alive():
            damage = hero.strike()
            boss.take_damage(damage)
            damage = boss.attack()
            defense = random.randint(1,5)
            hero.receive_damage(damage, defense)
        if hero.is_alive():
            print("The hero defeated the boss! How noble.")
        else:
            print("The hero was defeated by the boss. womp womp")
>>>>>>> Stashed changes
    else:
        print(f"\nThe hero has been defeated by goblins. Embarrassing!")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
