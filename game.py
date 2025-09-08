import random
from goblin import Goblin
from hero import Hero
from boss import LLorona

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
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


    #def special_ability(hero): 
    #   while rounds > 5:
    #        if hero.hp > 30: 
    #            hero.attack_power += 100
    #            print(f"New attack power: {hero.special_ability}")


    if hero.is_alive():
        print(f"\nThe hero has been defeated all the goblins1")
    else:
        print(f"\nThe hero has been defeated. Game over.")

    if hero.is_alive():
        girl = LLorona("Llorona")
        print("\Boss Round")
        while hero.is_alive() and girl.is_alive():
            damage = hero.strike()
            girl.take_damage(damage)

            damage = girl.attack()
            hero.receive_damage(damage)
        if hero.is_alive():
            print(f"\nThe hero has been defeated all the goblins1")
        else:
            print(f"\nThe hero has been defeated. Game over.")

    print("Batte Summary:")
    print(f"\nTotal Damage: {hero_damage}")
    print(f"\nRounds Survived: {rounds}")

    #if hero.is_alive():
    #    print("Bosss Time!!!")
    #    hi = LLorona("Nina")


    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()

