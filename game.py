import random
from goblin import Goblin
from hero import Hero
from enemy import Enemy

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Alexios")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total_damage += total_damage
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
        rounds = rounds + 1
    # Determine outcome
    if hero.is_alive():
        print(f"\nAfter "+ str(rounds) +" rounds, The hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nAfter "+ str(rounds) +" rounds, The hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")


    if hero.is_alive:
        print("Boss Fight Time!!")
        brute=Enemy("MegaKnight")
        while hero.is_alive and brute.is_alive():
            damage=hero.strike()
            brute.take_damage
            print(f"{hero.name} attacks {brute.name} for {damage} damage!")
            damage=brute.attack()
            hero.receive_damage()
            print(f"{brute.name} attacks {hero.name} for {damage} damage!")
            


if __name__ == "__main__":
    main()
