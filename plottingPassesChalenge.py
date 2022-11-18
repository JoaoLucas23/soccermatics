# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 21:22:55 2022

@author: jllgo
"""

import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen

parser = Sbopen()
df, related, freeze, tatics = parser.event(69301)
team1, team2 = df.team_name.unique()
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')
passes.info()

#Plotting shots on one half
pitch = Pitch(line_color='black')
#setting plot configurations
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)

#setting Sweden passes filter
mask_sweden = (df.type_name == 'Pass') & (df.team_name == team2)
#getting Sweden passes from data frame
df_sweden = df.loc[mask_sweden, ['x', 'y', 'outcome_name', "player_name"]]

#drawing shots circles
#pitch.scatter(df_sweden.x,df_sweden.y, alpha=1,s=500,color="blue",ax=ax['pitch'], edgecolors="black")
#seting plot title
#fig.suptitle("Sweden passess against England", fontsize=30)
#ploting
#plt.show()


#setting Caroline Seger passes filter
mask_Seger = (df.type_name == 'Pass') & (df.player_name == 'Sara Caroline Seger')
#getting Caroline Seger passes from data frame
#df_Seger = df.loc[mask_Seger, ['x', 'y', 'outcome_name', "player_name"]]
#drawing shots circles
#pitch.scatter(df_Seger.x,df_Seger.y, alpha=1,s=500,color="blue",ax=ax['pitch'], edgecolors="black")
#seting plot title
#fig.suptitle("Caroline Seger passess against England", fontsize=30)
#ploting
#plt.show()


df_Seger2 = df.loc[mask_Seger, ['x', 'y', 'end_x', 'end_y', 'outcome_name', "player_name"]]
mask_complete = df_Seger2.outcome_name.isnull()


pitch.scatter(df_Seger2[mask_complete].x,df_Seger2[mask_complete].y, alpha=1,s=250,color="blue",ax=ax['pitch'], edgecolors="black")
pitch.arrows(df_Seger2[mask_complete].x, df_Seger2[mask_complete].y,
             df_Seger2[mask_complete].end_x, df_Seger2[mask_complete].end_y,
             width=2,headwidth=10,headlength=10,color="blue",ax=ax['pitch'],
             label='completed passes')

pitch.scatter(df_Seger2[~mask_complete].x,df_Seger2[~mask_complete].y, alpha=1,s=250,color="yellow",ax=ax['pitch'], edgecolors="black")
pitch.arrows(df_Seger2[~mask_complete].x, df_Seger2[~mask_complete].y,
             df_Seger2[~mask_complete].end_x, df_Seger2[~mask_complete].end_y,
             width=2,headwidth=10,headlength=10,color="yellow",ax=ax['pitch'],
             label='not completed passes')

legend = ax['pitch'].legend(facecolor='#22312b', handlelength=5, edgecolor='None',
                            loc='upper left')
for text in legend.get_texts():
    text.set_fontsize(25)

fig.suptitle("Caroline Seger passess against England", fontsize=30)
plt.show()
