import random
from goblin import Goblin
from hero import Hero
from boss import Big_Irish_Man


def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    total_damageh = 0
    total_damageg = 0
    Ginger_killed = 0
    rounds = 0
   
    

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total_damageh = total_damageh + damage
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            rounds += 1

            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                total_damageg = total_damageg + damage
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
            else:
                print("GOBLIN IS DEAD")

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
        hero.health = 150
        print("Hero has rapidly consumed 6-7 nigiri platters and health has increased to 150")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    if hero.is_alive():
        print("GINGER HAS ENTERED THE CHAT")
        boss = Big_Irish_Man("GINGER GIANT")
        while hero.is_alive() and boss.is_alive():
            damage = hero.strike()
            boss.take_damage(damage)
            print("Just a scratch")
            if boss.health == (1-50):
                print("BIG IRISH UPGRADE YOU SMALL PATHETIC CHILD")
                print("HEALTH IS NOW 50 POINTS HIGHER")
                boss.health += 50
            damage = boss.attack()
            hero.receive_damage(damage)
        
        if hero.is_alive():
            print("Hero managed to kill the GINGER")
            
        else:
            print("HERO IS DEAD")
            print("Ginger clapped the hero")
            Ginger_killed += 1
                


    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("total rounds: " + str(rounds))
    print("total damage from goblin: " + str(total_damageg))
    print("total damage from hero: " + str(total_damageh))
if __name__ == "__main__":
    main()
