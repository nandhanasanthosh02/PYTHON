# #rpg game with random story
import random


player = input("Enter the player name: ")


time = ['Once upon a time', 'Long ago']
venue = ['in a forest', 'in the depth of the ocean', 'in a dungeon']
print(random.choice(time))
print(random.choice(venue))


enemy_list = ['Dragon', 'Werewolf', 'Goblin', 'Hydra']
enemy = random.choice(enemy_list)


player_hp = 100
enemy_hp = 110
turn = 1


while player_hp > 0 and enemy_hp > 0:
    print(f"\n--- Turn {turn} ---")


    damage = random.randint(1, 20)
    enemy_hp -= damage
    print(f"{player} attacks {enemy} for {damage} damage!")
    print(f"{enemy}'s HP: {max(enemy_hp, 0)}")

    
    if enemy_hp <= 0:
        print(f"\n {player} defeats {enemy}!")
        break

    damage = random.randint(1, 20)
    player_hp -= damage
    print(f"{enemy} attacks {player} for {damage} damage!")
    print(f"{player}'s HP: {max(player_hp, 0)}")

   
    if player_hp <= 0:
        print(f"\n💀 {enemy} defeats {player}!")
        break

    turn += 1

