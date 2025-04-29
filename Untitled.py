#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Import necessary libraries
import pandas as pd
import os


# Define the folder path where all NFL play-by-play CSVs are stored
data_folder = "C:\\Users\\fletc\\Downloads\\nfl_data"


# Dynamically gather all CSV files from the folder
all_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]


# Load and combine all play-by-play CSVs into a single DataFrame for processing
plays = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)


# Quick check on data load: total rows and column names
print(f"Total number of plays loaded: {plays.shape[0]}")
print(f"Available columns: {plays.columns.tolist()}")


# Filter all plays involving the Baltimore Ravens (either offense or defense)
ravens_plays = plays[(plays['posteam'] == 'BAL') | (plays['defteam'] == 'BAL')]
print(f"Ravens-related plays: {ravens_plays.shape[0]}")


# --- 1. TOUCHDOWNS BY SEASON ---
# Group touchdowns by season and count them
points_by_season = ravens_plays.groupby('season')['td_team'].count().reset_index()
points_by_season.rename(columns={'td_team': 'total_touchdowns'}, inplace=True)

print(points_by_season)


# --- 2. TOUCHDOWNS BY QUARTER ---
# Focus on Ravens' offensive plays only
ravens_offense = ravens_plays[ravens_plays['posteam'] == 'BAL']



# Count touchdowns scored in each quarte
points_by_quarter = ravens_offense.groupby('qtr')['td_team'].count().reset_index()
points_by_quarter.rename(columns={'td_team': 'touchdowns'}, inplace=True)
print(points_by_quarter)


# Export season and quarter-level touchdowns to CSVs for Tableau use
points_by_season.to_csv('ravens_points_by_season.csv', index=False)
points_by_quarter.to_csv('ravens_points_by_quarter.csv', index=False)

print("\nStarter files exported! You can now use them in Tableau for initial dashboards.")


# --- 3. YARDAGE ANALYSIS: RUSHING vs PASSING ---
# Re-define offensive plays for clarity
ravens_offense = ravens_plays[ravens_plays['posteam'] == 'BAL']


# Separate rushing and passing plays
rushing_plays = ravens_offense[ravens_offense['play_type'] == 'run']
passing_plays = ravens_offense[ravens_offense['play_type'] == 'pass']


# Total rushing yards per season
rushing_by_season = rushing_plays.groupby('season')['yards_gained'].sum().reset_index()
rushing_by_season.rename(columns={'yards_gained': 'total_rushing_yards'}, inplace=True)


# Total passing yards per season
passing_by_season = passing_plays.groupby('season')['yards_gained'].sum().reset_index()
passing_by_season.rename(columns={'yards_gained': 'total_passing_yards'}, inplace=True)


# Merge rushing and passing yard totals
yards_breakdown = pd.merge(rushing_by_season, passing_by_season, on='season')
print(yards_breakdown)


# Export rushing vs passing comparison for visualization
yards_breakdown.to_csv('ravens_rushing_vs_passing_by_season.csv', index=False)
print("\\nRushing vs Passing breakdown exported!")


# --- 4. GAME-BY-GAME TOUCHDOWNS ---
# Count total touchdowns per game, grouped by season and game ID
ravens_games = ravens_offense.groupby(['season', 'game_id'])['touchdown'].count().reset_index()
ravens_games.rename(columns={'touchdown': 'total_touchdowns'}, inplace=True)
ravens_games.to_csv('ravens_game_by_game_touchdowns.csv', index=False)
print("\nGame-by-game touchdowns exported!")


# --- 5. TOP PERFORMERS BY YARDS GAINED ---
# Display available columns for player insights:
print("\nAvailable columns in ravens_offense:")
print(ravens_offense.columns.tolist())



# Combine player name from passer, rusher, and receiver fields
ravens_offense = ravens_offense.copy()
ravens_offense['player_name'] = ravens_offense['passer_player_name'].fillna('') + \
                                ravens_offense['rusher_player_name'].fillna('') + \
                                ravens_offense['receiver_player_name'].fillna('')
ravens_offense['player_name'] = ravens_offense['player_name'].replace('', pd.NA)



# Filter plays with a valid player name
player_stats = ravens_offense[ravens_offense['player_name'].notnull()]


# Summarize total yards gained by each player, broken down by play type
player_summary = player_stats.groupby(['season', 'player_name', 'play_type'])['yards_gained'].sum().reset_index()

# Export player performance summary
player_summary.to_csv('ravens_top_players_stats.csv', index=False)
print("\nTop players stats exported!")


# Import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the game-by-game touchdowns data (you already created it)
ravens_games = pd.read_csv('ravens_game_by_game_touchdowns.csv')

# (Optional) Create a dummy Win/Loss target for now (for demo)
import numpy as np
np.random.seed(42)
ravens_games['win'] = np.random.choice([0, 1], size=len(ravens_games))

# Select features and target
X = ravens_games[['total_touchdowns']]  # Use more features later
y = ravens_games['win']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and Evaluate
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


