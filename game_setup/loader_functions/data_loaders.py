#!/usr/bin/env python
# coding: utf-8

# In[1]:
import genericpath
import shelve
import sqlite3
import os


def sql_save_game(player, entities, game_map, message_log, game_state):
    db = sqlite3.connect(':memory.db:')
    cursor = db.cursor()
    cursor.execute(''' 
    CREATE TABLE save_data(player,entities,game_map,message_log,game_state) 
    ''')


def save_game(player, entities, game_map, message_log, game_state):
    with shelve.open('savegame') as data_file:
        data_file['player_index'] = entities.index(player)
        data_file['entities'] = entities
        data_file['game_map'] = game_map
        data_file['message_log'] = message_log
        data_file['game_state'] = game_state


def load_game():
    if not os.path.isfile('savegame.dat'):
        raise FileNotFoundError

    with shelve.open('savegame', 'r') as data_file:
        player_index = data_file['player_index']
        entities = data_file['entities']
        game_map = data_file['game_map']
        message_log = data_file['message_log']
        game_state = data_file['game_state']

    player = entities[player_index]

    return player, entities, game_map, message_log, game_state

# In[ ]:
