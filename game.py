from monster import Monster
from hunter import Hunter

ARENA_NAME = "Dimensional Crack"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to the dungeon of the {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gate is opening...")

    monster = Monster("Beast Monarch")
    monster2 = Monster("Insect Monarch")
    monster3 = Monster("Frost Monarch")

    hunter = Hunter("Sung Jinwoo (Shadow Monarch)")

    print(f"{monster.name} enters the dungeon with {monster.health} health.")
    print(f"{monster2.name} enters the dungeon with {monster2.health} health.")
    print(f"{monster3.name} enters the dungeon with {monster3.health} health.")
    print("But no hunter has answered the call... yet.")

    print(f"{hunter.name} has answered the call and now enters the dungeon with {hunter.health} health.")

    attackedMonsterHealth = monster.take_damage(hunter.attack())
    if monster.is_alive():
        print("Since monster is still alive it attacks hunter")
        attackedHunterHealth = hunter.take_damage(monster.attack())


if __name__ == "__main__":
    main()
