# Project 02: University Admission Decision Engine
applicants = [("Anil","Engineering",92,80,78),("Bhavana","Science",70,88,82),("Chandu","Engineering",76,85,80),("Deepa","Science",84,72,86),("Farhan","Engineering",68,90,88)]
engineering, science, rejected = [], [], []
for name, course, maths, science_mark, english in applicants:
    aggregate = (maths + science_mark + english) / 3
    if course == "Engineering":
        if maths >= 75 and aggregate >= 80: engineering.append((name, aggregate, maths))
        else: rejected.append((name, "Engineering criteria not met"))
    elif course == "Science":
        if science_mark >= 70 and aggregate >= 75: science.append((name, aggregate, maths))
        else: rejected.append((name, "Science criteria not met"))
    else: rejected.append((name, "Invalid course"))
for group in (engineering, science):
    for i in range(len(group)):
        best = i
        for j in range(i + 1, len(group)):
            if group[j][1] > group[best][1] or (group[j][1] == group[best][1] and group[j][2] > group[best][2]): best = j
        group[i], group[best] = group[best], group[i]
print("ENGINEERING MERIT LIST")
for rank, x in enumerate(engineering, 1): print(rank, x[0], "Aggregate:", round(x[1],2), "Maths:", x[2])
print("\nSCIENCE MERIT LIST")
for rank, x in enumerate(science, 1): print(rank, x[0], "Aggregate:", round(x[1],2), "Maths:", x[2])
print("\nREJECTED")
for x in rejected: print(x[0], "-", x[1])