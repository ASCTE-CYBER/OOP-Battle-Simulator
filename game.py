from goblin import Goblin
from hero import Hero
from boss import Boss

ARENA_NAME = "The Iron Square"

def battle(hero:Hero,enemy:Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage= hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
              enemy_damage=enemy.attack()
              hero.take_damage(enemy_damage)

              if hero.is_alive():
                print(f"{hero.name} wins!")
        else:
              print(f"{enemy.name} wins!") 




def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to the spectatcular {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Yo Gabba Gabba")
    goblinTwo= Goblin("Teletubby")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")


    hero=Hero("Erenyager")
    print(f"{hero.name} enters the arena with {hero.health} health")
    battle(hero,goblin)

if __name__ == "__main__":
    main()

bossIt=Boss("Hiroshima")