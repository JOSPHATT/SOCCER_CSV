import selenium_betpawa_engine

Upcoming_Games=selenium_betpawa_engine.upcoming_games()
print(Upcoming_Games)
import csv
import pandas as pd
from itertools import pairwise
from datetime import datetime
d=datetime.now()

weekday=d.strftime("%a")

vals_Dct={}
C=0
#print(Upcoming_Games.items())
for key, vals in Upcoming_Games.items():
    Vals=str(vals)
    l=len(Vals)
    if weekday in Vals:
        vals_Dct[str(C)]=vals
        break
    else:
        continue
    C=C+1
print(vals_Dct.values())
vals_list=list(vals_Dct.values())
#print(vals_list)
games_data=vals_list[0].split("\n")
#print(games_data)

grouped_games={}
positions=[]
for pos,data in enumerate(games_data):
    if weekday in data:
        positions.append(pos)
    else:
        continue

K=0
for first, last in zip(positions, positions[1:]):
    grouped_games[str(K)]=[games_data[first:last]]
    K=K+1

#print(positions)
#print(games_data[38:59])

grouped_games_vals=[]
for i in grouped_games.values():
    for j in i:
        no_empty_string=[l for l in j if l]
        nn_empty_string=[g for g in no_empty_string if "+" not in g]

        grouped_games_vals.append(nn_empty_string)

game_vals=[]
for i in grouped_games_vals:

    l=[i[0:4],i[4:]]
    if l:
        game_vals.append(l)

#print(game_vals)
n_game_vals=[]
All_pairs=[]

V=0
for i in game_vals:
   # title=game_vals[i][0]
    p=pairwise(i[1])
    J=[]
    for h in p:
        if "Under" in h[0] or "Over" in h[0]:
            J.append(h)
    game_vals[V][1]=J
    All_pairs.append(J)
    V=V+1
print(game_vals)

List_of_dictionaries=[]
for i in game_vals:
    d={'time':i[0][0],'home':i[0][1],'away':i[0][2],'league':i[0][3]}
    odds=i[1]
    for odd in odds:
        d[odd[0]]=odd[1]
    List_of_dictionaries.append(d)
#print(List_of_dictionaries)

Df=pd.DataFrame(List_of_dictionaries)

# if file does not exist write header
if not os.path.isfile('soccer_over_under_odds.csv'):
    Df.to_csv('soccer_over_under_odds.csv', header='column_names')
else:
# else it exists so append without writing the header
    Df.to_csv('soccer_over_under_odds.csv', mode='a', header=False)
#df=pd.read_csv("/content/drive/MyDrive/2024/soccer_over_under_odds.csv")
df = pd.read_csv('soccer_over_under_odds.csv').drop_duplicates(keep='first')
df
