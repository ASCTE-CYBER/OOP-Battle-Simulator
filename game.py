import random
from goblin import Goblin
from hero import Hero
from boss_toji import Boss_Toji


def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Gojo")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # track total rounds
    total_rounds = 1

    # track total damage dealt
    total_damage = 0

    # Battle Loop
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print(f"\nRound {total_rounds}")
        total_rounds += 1

        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total_damage += damage
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
                total_damage += damage
                print(f"{goblin.name} attacks {hero.name} for {damage} damage!")
                hero.receive_damage(damage)
                if hero.health == 0:
                    hero.reversed_cursed_technique()

    boss = Boss_Toji("Toji Fushiguro")
    boss_rounds = 0

    print("Toji is approaching")
    while hero.is_alive() and boss.is_alive():
        print("\nNew Round!")
        boss_rounds += 1
        total_rounds += 1
        print(boss_rounds)
        if boss_rounds == 10:
            damage = boss.inverted_spear_of_heaven()
            total_damage += damage
            print(f"{boss.name} attacks {hero.name} for {damage} damage!")
            hero.receive_damage(damage)
            if hero.health == 0:
                hero.reversed_cursed_technique()
        else:
            damage = hero.strike()
            total_damage += damage
            print(f"{hero.name} attacks {boss.name} for {damage} damage!")
            boss.take_damage(damage)
            if boss.is_alive():
                damage = boss.attack()
                total_damage += damage
                print(f"{boss.name} attacks {hero.name} for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the enemies!!!!")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"total rounds: {total_rounds}")
    print(f"total damage: {total_damage}")


if __name__ == "__main__":
    main()
