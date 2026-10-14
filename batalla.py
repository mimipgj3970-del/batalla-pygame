#-------------------------------------------------------------------------------
# Name:        batalla.py
# Purpose:
#
# Author:      delfi
#
# Created:     13/10/2026
# Copyright:   (c) SSI 2026
# Licence:     <dempi>
#-------------------------------------------------------------------------------

def main(battle):
    pass

if __name__ == '__main__':
    main()

import random

# Initial health points
player = 100
monster = 100

# Function that returns random damage
def attack():
    return random.randint(5, 15)

# Battle
while player > 0 and monster > 0:

    # The player attacks the monster
    player_damage = attack()
    monster = monster - player_damage
    print("The player attacks and deals", player_damage, "damage.")
    print("Monster health:", max(0, monster))

    # If the monster is still alive, it attacks back
    if monster > 0:
        monster_damage = attack()
        player = player - monster_damage
        print("The monster attacks and deals", monster_damage, "damage.")
        print("Player health:", max(0, player))

    print("--------------------------")

# Determine who lost
if player <= 0:
    print("The player lost the battle.")
elif monster <= 0:
    print("The monster lost the battle.")
