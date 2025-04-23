#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import os


# In[5]:


data_folder = "C:\\Users\\fletc\\Downloads\\nfl_data"


# In[6]:


all_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]


# In[7]:


plays = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)


# In[8]:


print(f"Total number of plays loaded: {plays.shape[0]}")
print(f"Available columns: {plays.columns.tolist()}")


# In[9]:


ravens_plays = plays[(plays['posteam'] == 'BAL') | (plays['defteam'] == 'BAL')]
print(f"Ravens-related plays: {ravens_plays.shape[0]}")


# In[10]:


points_by_season = ravens_plays.groupby('season')['td_team'].count().reset_index()
points_by_season.rename(columns={'td_team': 'total_touchdowns'}, inplace=True)

print(points_by_season)


# In[12]:


ravens_offense = ravens_plays[ravens_plays['posteam'] == 'BAL']
points_by_quarter = ravens_offense.groupby('qtr')['td_team'].count().reset_index()
points_by_quarter.rename(columns={'td_team': 'touchdowns'}, inplace=True)
print(points_by_quarter)


# In[13]:


points_by_season.to_csv('ravens_points_by_season.csv', index=False)
points_by_quarter.to_csv('ravens_points_by_quarter.csv', index=False)

print("\nStarter files exported! You can now use them in Tableau for initial dashboards.")


# In[14]:


ravens_offense = ravens_plays[ravens_plays['posteam'] == 'BAL']


# In[15]:


rushing_plays = ravens_offense[ravens_offense['play_type'] == 'run']
passing_plays = ravens_offense[ravens_offense['play_type'] == 'pass']


# In[16]:


rushing_by_season = rushing_plays.groupby('season')['yards_gained'].sum().reset_index()
rushing_by_season.rename(columns={'yards_gained': 'total_rushing_yards'}, inplace=True)


# In[17]:


passing_by_season = passing_plays.groupby('season')['yards_gained'].sum().reset_index()
passing_by_season.rename(columns={'yards_gained': 'total_passing_yards'}, inplace=True)


# In[19]:


yards_breakdown = pd.merge(rushing_by_season, passing_by_season, on='season')
print(yards_breakdown)


# In[20]:


yards_breakdown.to_csv('ravens_rushing_vs_passing_by_season.csv', index=False)

print("\\nRushing vs Passing breakdown exported!")


# In[23]:


ravens_games = ravens_offense.groupby(['season', 'game_id'])['touchdown'].count().reset_index()
ravens_games.rename(columns={'touchdown': 'total_touchdowns'}, inplace=True)
ravens_games.to_csv('ravens_game_by_game_touchdowns.csv', index=False)
print("\nGame-by-game touchdowns exported!")


# In[25]:


print("\nAvailable columns in ravens_offense:")
print(ravens_offense.columns.tolist())


# In[26]:


ravens_offense = ravens_offense.copy()

ravens_offense['player_name'] = ravens_offense['passer_player_name'].fillna('') + \
                                ravens_offense['rusher_player_name'].fillna('') + \
                                ravens_offense['receiver_player_name'].fillna('')

ravens_offense['player_name'] = ravens_offense['player_name'].replace('', pd.NA)


# In[27]:


player_stats = ravens_offense[ravens_offense['player_name'].notnull()]


# In[28]:


player_summary = player_stats.groupby(['season', 'player_name', 'play_type'])['yards_gained'].sum().reset_index()
player_summary.to_csv('ravens_top_players_stats.csv', index=False)
print("\nTop players stats exported!")


# In[ ]:




