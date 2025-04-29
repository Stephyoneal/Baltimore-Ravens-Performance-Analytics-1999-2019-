# Project Title:
Baltimore Ravens Performance Analytics (1999–2019)

## Project Overview 
This project analyzes 20 seasons of the Baltimore Ravens’ performance (1999–2019) using a combination of Python (data preparation) and Tableau (visual analytics). The goal was to uncover trends in scoring, rushing vs. passing behavior, and top player contributions.
Insights are visualized using dynamic dashboards and a storytelling format in Tableau Public. This project simulates what an analytics department in a sports organization might use for evaluating historical data and identifying performance drivers.

## Tools & Technologies
- Python (Pandas, Scikit-Learn)
- Tableau Public (Visualization & Storytelling)
- Excel (Data Preparation)
- Logistic Regression (Supervised Learning)


## Dataset Used 
-<a href= "https://raw.githubusercontent.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/refs/heads/main/ravens_game_by_game_touchdowns.csv">Dataset</a>
 -<a href="https://raw.githubusercontent.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/refs/heads/main/ravens_points_by_quarter.csv">Dataset</a>
 -<a href="https://raw.githubusercontent.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/refs/heads/main/ravens_points_by_season.csv">Dataset</a>
-<a href="https://raw.githubusercontent.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/refs/heads/main/ravens_rushing_vs_passing_by_season.csv">Dataset</a>
-<a href="https://raw.githubusercontent.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/refs/heads/main/ravens_top_players_stats.csv">Dataset</a>
-<a href="https://github.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/blob/main/Stephy%20project.twbx">Dataset</a>


## Key KPIs Tracked
-Total Touchdowns per Season	            
-Rushing vs. Passing Yards per Season	   
-Top Players by Yards Gained	           
-Touchdowns by Quarter (Q1–Q4)	          
-High-Scoring Games (Threshold-based)   	
-Game-by-Game Touchdown Trends	          
-Dashboard interaction -<a href="https://github.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/blob/main/Screenshot%202025-04-23%20120335.png">Dataset</a>

## Machine Learning Component
- **Model**: Logistic Regression
- **Goal**: Predict game outcome (Win = 1, Loss = 0) from gameplay stats
- **Features used**: Total touchdowns per game
- **Evaluation**: Confusion Matrix, Accuracy, Precision, Recall, F1-Score


## Process 
This project followed a full-cycle data analytics workflow—starting from raw data to interactive dashboards and insights:

- Data Collection & Preparation
Imported season-wise performance data of the Baltimore Ravens from 1999 to 2019, including:
Total touchdowns by season
Touchdowns by quarter
Rushing and passing yards
Game-by-game statistics
Player performance stats
Cleaned and standardized CSV files in Excel and optionally via Python
Ensured data types (e.g., year as dimensions, scores as measures) were compatible for visualization

- Data Exploration & KPI Development
Defined core KPIs:
Total touchdowns per season
Touchdowns per game and quarter
Yards gained by top players (run/pass)
Rushing vs. passing yardage split
Calculated derived fields like “Big Touchdown Games” based on thresholds
- **Supervised Learning**: Trained a Logistic Regression model to predict win/loss outcomes based on total touchdowns.

- Data Visualization with Tableau
Created the following sheets:
Line Chart: Touchdowns across 1999–2019
Stacked Bars: Rushing vs. Passing Yards per Season
Game-by-Game Touchdowns: Line graph with highlight for top games
Top Players: Horizontal bar chart by yards gained
Quarter-wise Analysis: Touchdowns by Q1–Q4
Designed a Tableau Story to walk stakeholders through the performance narrative -<a href="https://github.com/Stephyoneal/Baltimore-Ravens-Performance-Analytics-1999-2019-/blob/main/Stephy%20project.twbx">Dataset</a>

## Dashboard 
![Screenshot 2025-04-23 120335](https://github.com/user-attachments/assets/860adf97-7d13-480f-8643-54b24ad0c71e)

## Project Insights
- Touchdown Trends
The Ravens saw consistent growth in touchdowns with notable peaks in 2012 and 2014.
Touchdowns dropped in certain seasons (e.g., 2005, 2007)—potential coaching or roster impacts.

- Quarter-by-Quarter Strength
The team scored most touchdowns in Q4, suggesting a strong closing capability.
Q1 had the fewest touchdowns, indicating slower starts.

- Offensive Strategy: Rushing vs. Passing
From 2008–2013, there was a strong balance between rushing and passing yards.
Recent seasons (2018–2019) show an increased reliance on rushing, possibly due to quarterback play style (e.g., Lamar Jackson’s era).

- Top Players
J. Lewis and R. Rice led in rushing yards.
J. Flacco dominated passing contributions across multiple seasons.
Emerging talents like L. Jackson began appearing in recent years, reflecting team evolution.

- High-Impact Games
Identified several games with 95+ touchdowns, visually highlighted using custom color legends.
These games represent strategic victories or explosive team performance.

## Final Conclusion
The Baltimore Ravens have evolved significantly between 1999 and 2019, showing patterns of strategic adaptability, strong late-game performance, and shifting offensive tactics. Tableau visualizations allowed us to uncover not just raw stats, but insights that can inform coaching, scouting, and sports analytics decisions.
This project showcases how sports data visualization can bridge raw stats with storytelling, and how combining historical performance metrics with interactive dashboards creates powerful narratives for teams, fans, and analysts alike.

## Future Work
Live SQL database integration
Machine learning to predict touchdown probabilities
Comparison across NFL teams (not just Ravens)
