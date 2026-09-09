from goblin import Goblin


ARENA_NAME = "Goblet of Fire"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates open ready for battle...")

    goblin = Goblin("Harry Potter")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no wizard has answered the call... yet.")


if __name__ == "__main__":
    main()
