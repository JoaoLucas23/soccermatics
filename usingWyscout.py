# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:20:04 2022

@author: jllgo
"""
# importing libraries
import os
import pandas as pd
import json

#getting data path
competitions_path = 'H:\Documentos\SaLab\Soccermatics\Wyscout Data\competitions.json'
#asserting file exists
assert os.path.isfile(competitions_path)

#opening file
with open(competitions_path, "r") as f:
    #transforming data in json
    data = json.load(f)
    
#creating pandas data frame
df_competitions = pd.DataFrame(data)
#getting competitions data structure
df_competitions.info()

#getting data path
matches_path = 'H:\Documentos\SaLab\Soccermatics\Wyscout Data\matches_England.json'
#asserting file exists
assert os.path.isfile(matches_path)

#opening file
with open(matches_path, "r") as f:
    #transforming data in json
    data = json.load(f)
    
#creating pandas data frame
df_matches = pd.DataFrame(data)
#getting matches data structure
df_matches.info()

#getting data path
players_path = 'H:\Documentos\SaLab\Soccermatics\Wyscout Data\players.json'
#asserting file exists
assert os.path.isfile(players_path)

#opening file
with open(players_path, "r") as f:
    #transforming data in json
    data = json.load(f)
   
#creating pandas data frame
df_players = pd.DataFrame(data)
#getting players data structure
df_players.info()

#getting data path
events_path = 'H:\Documentos\SaLab\Soccermatics\Wyscout Data\events_England.json'
#asserting file exists
assert os.path.isfile(events_path)

#opening file
with open(events_path, "r") as f:
    #transforming data in json
    data = json.load(f)

#creating pandas data frame
df_events = pd.DataFrame(data)
#getting events data structure
df_events.info()
