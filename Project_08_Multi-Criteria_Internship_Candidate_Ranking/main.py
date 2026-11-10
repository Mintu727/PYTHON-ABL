# Project 08: Multi-Criteria Internship Candidate Ranking
candidates = [("Ira",[80,85,78],88,92),("Jay",[70,68,72],75,80),("Kiran",[90,92,88],55,95),("Latha",[65,70,68],82,78),("Manoj",[60,62,64],70,85)]
eligible,rejected = [],[]
for name,marks,assessment,attendance in candidates:
    average = sum(marks)/len(marks); score = 0.5*average + 0.4*assessment + 0.1*attendance
    reasons = []
    if average < 65: reasons.append("academic average below 65")
    if assessment < 60: reasons.append("assessment below 60")
    if attendance < 75: reasons.append("attendance below 75")
    if not reasons: eligible.append((name,round(score,2),assessment))
    else: rejected.append((name,reasons))
for i in range(len(eligible)):
    best = i
    for j in range(i+1,len(eligible)):
        if eligible[j][1] > eligible[best][1] or (eligible[j][1] == eligible[best][1] and eligible[j][2] > eligible[best][2]): best = j
    eligible[i],eligible[best] = eligible[best],eligible[i]
print("INTERNSHIP MERIT LIST")
for rank,x in enumerate(eligible,1): print(rank,x[0],"Weighted score:",x[1],"Assessment:",x[2])
print("\nNOT SHORTLISTED")
for x in rejected: print(x[0],"-",", ".join(x[1]))