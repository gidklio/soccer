
# Roll a pair of dice
# Roll a single die the number of times indicated by the initial pair
# Each time this single die comes up "6", your team scores a goal
# Seems that on average a team ends up with 1.1-1.2 goals/game

# 2002 World Cup: 161 goals/128 team-games = 1.257 goal/team/game
# 2006 World Cup: 147 goals/128 team-games = 1.148 goal/team/game
# 2010 World Cup: 145 goals/128 team-games = 1.133 goal/team/game
# 2014 World Cup: 171 goals/128 team-games = 1.336 goal/team/game

import random

def roll():
    min = 1
    max = 6
    OneDie=random.randint(min, max)
    #print("  rolled ",OneDie,"     ")
    return OneDie

def rollpair():
    TwoDice=roll()+roll()
    #print("total: ",TwoDice)
    return TwoDice

def GotSix(roll):
    if roll == 6:
        return "1"
    return 0
    
def OneGame():
    Score=0
    NumShots=rollpair()
    for i in range(0,NumShots):
        ShotOnGoal=roll()
        if GotSix(ShotOnGoal): 
            Goal="!"
            Score=Score+1
        else: Goal=""
        #print("Shot number ",i+1,"/",NumShots," is a ",ShotOnGoal,Goal)
        #print("              Goals this game: ",Score)
    #print(Score,"/",NumShots)
    return Score

def Series(games):
    Total=0
    #print("GOALS/ATTEMPTS")
    for i in range(0,games):
        Score=OneGame()
        #print("GAMESCORE: ",Score)
        Total=Total+Score
    print(Total," goals in ",games," matches")

def main(max):
    for i in range(0,max):
        Series(1000)
        
main(100)
