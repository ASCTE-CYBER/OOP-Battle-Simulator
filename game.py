import random
from goblin import Goblin
from hero import Hero
from boss import Grim_reaper

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Link")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "Green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop (Goblins)
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        input("Press [Enter] to continue")

        # Hero's turn: choose ability
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        print(f"Choose Link's ability (Stamina: {hero.stamina}/5):")
        print("1. Strike (normal attack, takes 1 stamina)")
        print("2. Power Slash (costs 3 stamina, strong, high miss rate)")
        print("3. Recovery (heal HP, regain stamina)")
        choice = input("Enter 1, 2, or 3: ")
        if choice == "2":
            damage = hero.power_slash()
        elif choice == "3":
            damage = hero.recovery()
        else:
            damage = hero.strike()
        if choice != "3":
            # Ensure damage is an integer if a tuple is returned
            if isinstance(damage, tuple):
                damage = damage[0]
            print(f"Link attacks {target_goblin.name} for {damage} damage!")
            target_goblin.take_damage(damage)
        input("Press [Enter] to continue")

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")
            input("Press [Enter] to continue")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                if isinstance(damage, tuple):
                    damage = damage[0]
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                input("Press [Enter] to continue")

    if hero.is_alive():
        grim_reaper = Grim_reaper("Grim Reaper")
        print("\nA dark presence descends The Grim Reaper appears!")
        input("Press [Enter] to face the Grim Reaper")
        while hero.is_alive() and grim_reaper.is_alive():
            print("\nBoss Round!")
            input("Press [Enter] to continue...")
            print(f"Choose Link's ability (Stamina: {hero.stamina}/5):")
            print("1. Strike (normal attack, takes 1 stamina)")
            print("2. Power Slash (costs 3 stamina, strong, high miss rate)")
            print("3. Recovery (heal HP, regain stamina)")
            choice = input("Enter 1, 2, or 3: ")
            if choice == "2":
                # Ensure damage is an integer if a tuple is returned
                if isinstance(damage, tuple):
                    damage = damage[0]
                print(f"Link attacks Grim Reaper for {damage} damage!")
                grim_reaper.take_damage(damage)
                input("Press [Enter] to continue")
            else:
                damage = hero.strike()
            if choice != "3":
                print(f"Link attacks Grim Reaper for {damage} damage!")
                grim_reaper.take_damage(damage)
            input("Press [Enter] to continue")
            if not grim_reaper.is_alive():
                print("The Grim Reaper has been defeated!")
            if isinstance(damage, tuple):
                damage = damage[0]
            print(f"Grim Reaper attacks hero for {damage} damage!")
            hero.receive_damage(damage)
            input("Press [Enter] to continue")
            # Randomly determine Grim Reaper's attack choice
            attack_choice = random.randint(1, 100)
            if attack_choice <= 95:
                damage = grim_reaper.super_attack()
            elif attack_choice > 95:
                damage = grim_reaper.soul_harvest()
            else:
                damage = grim_reaper.attack()
            print(f"Grim Reaper attacks hero for {damage} damage!")
            hero.receive_damage(damage)
            input("Press [Enter] to continue")

    # Determine outcome
    if hero.is_alive():
        print(f"\nLink has triumphed over all enemies, including the Grim Reaper! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nLink has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
