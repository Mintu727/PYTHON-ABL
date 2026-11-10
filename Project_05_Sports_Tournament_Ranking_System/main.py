# Project 05: Sports Tournament Ranking System
teams = ["Falcons","Tigers","Eagles","Sharks"]
matches = [("Falcons","Tigers",2,1),("Eagles","Sharks",1,1),("Falcons","Eagles",0,2),("Tigers","Sharks",3,1),("Falcons","Sharks",2,2),("Tigers","Eagles",0,1)]
stats = [[0,0,0] for team in teams]
for home,away,hg,ag in matches:
    hi,ai = teams.index(home),teams.index(away)
    stats[hi][1] += hg; stats[hi][2] += ag
    stats[ai][1] += ag; stats[ai][2] += hg
    if hg > ag: stats[hi][0] += 3
    elif ag > hg: stats[ai][0] += 3
    else: stats[hi][0] += 1; stats[ai][0] += 1
table = []
for i in range(len(teams)):
    points,gf,ga = stats[i]; table.append((teams[i],points,gf-ga,gf))
for i in range(len(table)):
    best = i
    for j in range(i+1,len(table)):
        a,b = table[j],table[best]
        if a[1] > b[1] or (a[1] == b[1] and a[2] > b[2]) or (a[1] == b[1] and a[2] == b[2] and a[3] > b[3]): best = j
    table[i],table[best] = table[best],table[i]
print("TOURNAMENT POINTS TABLE\nRank Team Points GD Goals")
for rank,x in enumerate(table,1): print(rank,x[0],x[1],x[2],x[3])