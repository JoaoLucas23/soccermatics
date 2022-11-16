# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mplsoccer import Sbopen
#creating Sbopen parser
parser = Sbopen()

#opening competition data
df_competition = parser.competition()
#getting competition data structure
df_competition.info()

#opening match data
df_match = parser.match(competition_id=72, season_id=30)
#getting match data structure
df_match.info()

#opening lineup data
df_lineup = parser.lineup(69301)
#getting lineup data structure
df_lineup.info()

#opening event data
df_event, df_related, df_freeze, df_tatics = parser.event(69301)
# to get only event data use parser.envent(69301)[0]
#getting event data structure
df_event.info()

#opening 360 event data
df_frame, df_visible = parser.frame(3788741)
#getting frame data structure
df_frame.info()