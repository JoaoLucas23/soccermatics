# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:56:27 2022

@author: jllgo
"""

import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen

#getting stats bomb data
parser = Sbopen()
#getting events data from match 69301
df, related, freeze, tactics = parser.event(69301)
#filtering passes events
passes = df.loc[df['type_name'] == 'Pass'].loc[df['sub_type_name'] != 'Throw-in'].set_index('id')

#creating pitch
pitch = Pitch(line_color = "black") 
fig, ax = pitch.draw(figsize=(10, 7))

#looping over passes
for i,thepass in passes.iterrows():
    #if pass made by Lucy Bronze
    if thepass['player_name']=='Lucy Bronze':
        #gettign pass location
        x=thepass['x']
        y=thepass['y']
        dx=thepass['end_x']-x
        dy=thepass['end_y']-y
        #plot circle
        if thepass['outcome_name'] != 'Incomplete' :
            passCircle=plt.Circle((x,y),2,color="blue")
            passCircle.set_alpha(.2)
            passArrow=plt.Arrow(x,y,dx,dy,width=3,color="blue")
        else:
            passCircle=plt.Circle((x,y),2,color="red")
            passCircle.set_alpha(.2)
            passArrow=plt.Arrow(x,y,dx,dy,width=3,color="red")
        #plot circle and arrow
        ax.add_patch(passCircle)
        ax.add_patch(passArrow)

ax.set_title("Lucy Bronze passes against Sweden", fontsize = 24)
fig.set_size_inches(10, 7)
plt.show()

##############################################################################

mask_bronze = (df.type_name == 'Pass') & (df.player_name == "Lucy Bronze")
df_pass = df.loc[mask_bronze, ['x', 'y', 'end_x', 'end_y',  'outcome_name']]
mask_complete = df_pass.outcome_name.isnull()

pitch = Pitch(line_color='black')
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)

pitch.arrows(df_pass.x[mask_complete], df_pass.y[mask_complete],
            df_pass[mask_complete].end_x, df_pass[mask_complete].end_y, color = "blue", ax=ax['pitch'])

pitch.arrows(df_pass.x[~mask_complete], df_pass.y[~mask_complete],
            df_pass[~mask_complete].end_x, df_pass[~mask_complete].end_y, color = "red", ax=ax['pitch'])

pitch.scatter(df_pass[mask_complete].x, df_pass[mask_complete].y, alpha = 0.2, s = 500, color = "blue", ax=ax['pitch'])
pitch.scatter(df_pass[~mask_complete].x, df_pass[~mask_complete].y, alpha = 0.2, s = 500, color = "red", ax=ax['pitch'])

fig.suptitle("Lucy Bronze passes against Sweden", fontsize = 30)
plt.show()

##############################################################################

#prepare the dataframe of passes by England that were no-throw ins
mask_england = (df.type_name == 'Pass') & (df.team_name == "England Women's") & (df.sub_type_name != "Throw-in")
#getting passes with filter
df_passes = df.loc[mask_england, ['x', 'y', 'end_x', 'end_y', 'player_name', 'outcome_name']]
#get the list of all players who made a pass
names = df_passes['player_name'].unique()

#draw 4x4 pitches
pitch = Pitch(line_color='black', pad_top=20)
fig, axs = pitch.grid(ncols = 4, nrows = 4, grid_height=0.85, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0.04, endnote_space=0.01)

#iterate through names and pitchs
for name, ax in zip(names, axs['pitch'].flat[:len(names)]):
    #write player name over the plot
    ax.text(60, -10, name,
            ha='center', va='center', fontsize=14)
    #filter passes by player
    player_df = df_passes.loc[df_passes["player_name"] == name]
    #plot circles
    pitch.scatter(player_df.x, player_df.y, alpha = 0.2, s = 50, color = "blue", ax=ax)
    #plot arrow
    pitch.arrows(player_df.x, player_df.y,
                player_df.end_x, player_df.end_y, color = "blue", ax=ax, width=1)
   
#removing some pitches
for ax in axs['pitch'][-1, 16 - len(names):]:
    ax.remove()
    
#Another way to set title using mplsoccer
axs['title'].text(0.5, 0.5, 'England passes against Sweden', ha='center', va='center', fontsize=30)
plt.show()