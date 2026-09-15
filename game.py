from goblin import Goblin
from hero import Hero

ARENA_NAME = "Goblet of Fire"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")  

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates open ready for battle...")

    goblin = Goblin("Ron Weasley")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblintwo = Goblin("Cedric Diggory")
    
    print(f"{goblintwo.name} enters the arena with {goblintwo.health} health.")
    print("The wizard Harry Potter has been called for battle!")

    HarryPotter = Hero("Harry Potter")
    HarryPotter.battle_cry()

    goblintwo = Goblin("Cedric Diggory")
    battle(HarryPotter, goblin)

if __name__ == "__main__":
    main()

    
