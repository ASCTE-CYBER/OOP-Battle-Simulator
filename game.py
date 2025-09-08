import random
from goblin import Goblin
from hero import Hero
from boss import wizard

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("fred")

    # Create goblins
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of stats
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
        total_damage += damage
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        turnG=True

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                total_damage += damage
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)  # Use take_damage for hero
                turnH=True

    # Boss fight
    if hero.is_alive():
        print("Boss fight time!")
        boss = wizard("timothee")
        while hero.is_alive() and boss.is_alive():
            damage = hero.strike()
            boss.take_damage(damage)
            if boss.is_alive():
                damage = boss.attack()
                hero.receive_damage(damage)

        # Determine outcome
        if hero.is_alive():
            print(f"\nThe hero has defeated all the goblins and the boss! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"\nThe hero has been defeated by the boss. Game Over. (｡•́︿•̀｡)")
    else:
        print(f"\nThe hero has been defeated by the goblins. Game Over. (｡•́︿•̀｡)")

    print(f"\nTotal Damage Dealt: {total_damage}")
    print(f"\nTotal Rounds Fought: {rounds}")
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
