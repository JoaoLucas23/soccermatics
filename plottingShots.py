# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:48:15 2022

@author: jllgo
"""

import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen, VerticalPitch

#define stats bomb open data parser
parser = Sbopen()
# getting event data
df, related, freeze, tactics = parser.event(69301)
#get teams names
team1, team2 = df.team_name.unique()
#get all events with type name = shots in the dataframe
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')

#draw a pitch using mplsoccer
pitch = Pitch(line_color="black")
fig, ax = pitch.draw(figsize=(10,7))
#define pitch size in yards (Stats bom pattern)
pitchLengthX = 120
pitchWidthY = 80

#plotting the shots in the pitch with a for loop
for i, shot in shots.iterrows():
    #getting the shot position
    x=shot['x']
    y=shot['y']
    #checking if shot was a goal
    goal=shot['outcome_name']=='Goal'
    #getting the team that shoted
    team_name=shot['team_name']
    #setting circle size (will represent the shot position on the field)
    circleSize=2
    #checking if team is team1 (England)
    if(team_name==team1):
        #checking if it was goal
        if goal:
            #plotting circle
            shotCircle=plt.Circle((x,y),circleSize,color="red")
            #plotting player that scored name
            plt.text(x+1, y-2, shot['player_name'])
        #if it was not goal
        else:
            #plotting circle
            shotCircle=plt.Circle((x,y),circleSize,color="red")
            #setting circle transparency
            shotCircle.set_alpha(.2)
    #checking if team is team2 (Sweden)
    else:
        if goal:
            #plotting circle
            shotCircle=plt.Circle((pitchLengthX-x,pitchWidthY-y),circleSize,color="blue")
            #plotting player that scored name
            plt.text(pitchLengthX-x+1, pitchWidthY-y-2, shot['player_name'])
        #if it was not goal
        else: 
            #plotting circle
            shotCircle=plt.Circle((pitchLengthX-x,pitchWidthY-y),circleSize,color="blue")
            #setting circle transparency
            shotCircle.set_alpha(.2)
    #add circles to plot
    ax.add_patch(shotCircle)
    
#set title of plot
fig.suptitle("England (red) and Sweden (blue) shots", fontsize=24)
#set pitch size on plot
fig.set_size_inches(10,7)
#plot
plt.show()

#drawing pitch with mplsoccer Pitch class
pitch = Pitch(line_color='black')
#setting plot configurations
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)

#setting England shots filter
mask_england = (df.type_name == 'Shot') & (df.team_name == team1)
#getting England shots from data frame
df_england = df.loc[mask_england, ['x', 'y', 'outcome_name', "player_name"]]

#iterating through England shots
for i, row in df_england.iterrows():
    #if shot was goal
    if row["outcome_name"] == 'Goal':
        #making circle
       pitch.scatter(row.x, row.y, alpha = 1, s = 500, color = "red", ax=ax['pitch'])
        #writing player name      
       pitch.annotate(row["player_name"], (row.x + 1, row.y - 2), ax=ax['pitch'], fontsize = 12)
    #if shot was not goal   
    else:
        #makig circle
       pitch.scatter(row.x, row.y, alpha = 0.2, s = 500, color = "red", ax=ax['pitch'])

#setting Sweden shots filter
mask_sweden = (df.type_name == 'Shot') & (df.team_name == team2)
#getting Sweden shots from data frame
df_sweden = df.loc[mask_sweden, ['x', 'y', 'outcome_name', "player_name"]]

#iterating through Sweden shots
for i, row in df_sweden.iterrows():
    #if shot was goal
    if row["outcome_name"] == 'Goal':
        #making circle
       pitch.scatter(120 - row.x, 80 - row.y, alpha = 1, s = 500, color = "blue", ax=ax['pitch'])
       #writing player name
       pitch.annotate(row["player_name"], (120 - row.x + 1, 80 - row.y - 2), ax=ax['pitch'], fontsize = 12)
    #if shot was not goal
    else:
        #making circle
       pitch.scatter(120 - row.x, 80 - row.y, alpha = 0.2, s = 500, color = "blue", ax=ax['pitch'])
      
#writing plot title
fig.suptitle("England (red) and Sweden (blue) shots", fontsize=24)
#plotting
plt.show()


#Plotting shots on one half
pitch = VerticalPitch(line_color='black', half = True)
#setting plot configurations
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)

#setting England shots filter
mask_england = (df.type_name == 'Shot') & (df.team_name == team1)
#getting England shots from data frame
df_england = df.loc[mask_england, ['x', 'y', 'outcome_name', "player_name"]]

#drawing shots circles
pitch.scatter(df_england.x,df_england.y, alpha=1,s=500,color="red",ax=ax['pitch'], edgecolors="black")
#seting plot title
fig.suptitle("England shots against Sweden", fontsize=30)
#ploting
plt.show()