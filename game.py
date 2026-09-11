from goblin import Goblin


ARENA_NAME = "Dimensional Crack"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Beast Monarch")
    goblin2 = Goblin("Insect Monarch")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hunter has answered the call... yet.")


if __name__ == "__main__":
    main()
