# Project 01: University Scholarship Allocation
applicants = [
    ("Asha", 88, 82, 91, 94, 180000),
    ("Bharat", 78, 81, 75, 90, 220000),
    ("Charan", 92, 58, 95, 96, 150000),
    ("Divya", 85, 86, 84, 82, 200000),
    ("Esha", 80, 80, 80, 92, 250000)
]
eligible, rejected = [], []
for student in applicants:
    name, m1, m2, m3, attendance, income = student
    aggregate = (m1 + m2 + m3) / 3
    reasons = []
    if aggregate < 75: reasons.append("aggregate below 75%")
    if m1 < 60 or m2 < 60 or m3 < 60: reasons.append("subject mark below 60")
    if attendance < 85: reasons.append("attendance below 85%")
    if income > 250000: reasons.append("income above limit")
    if not reasons: eligible.append((name, aggregate, attendance, income))
    else: rejected.append((name, reasons))
for i in range(len(eligible)):
    best = i
    for j in range(i + 1, len(eligible)):
        a, b = eligible[j], eligible[best]
        if a[1] > b[1] or (a[1] == b[1] and a[2] > b[2]) or (a[1] == b[1] and a[2] == b[2] and a[3] < b[3]): best = j
    eligible[i], eligible[best] = eligible[best], eligible[i]
print("SCHOLARSHIP ELIGIBILITY REPORT")
for rank, s in enumerate(eligible, 1): print(rank, s[0], "Aggregate:", round(s[1], 2), "Attendance:", s[2], "Income:", s[3])
print("\nNOT ELIGIBLE")
for name, reasons in rejected: print(name, "-", ", ".join(reasons))