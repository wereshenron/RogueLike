#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tcod

from game_messages import Message
from game_states import GameStates


def kill_player(player):
    player.char = '%'
    player.color = tcod.dark_red
    return Message('You died!', tcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), tcod.orange)
    monster.char = '%'
    monster.color = tcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    return death_message
