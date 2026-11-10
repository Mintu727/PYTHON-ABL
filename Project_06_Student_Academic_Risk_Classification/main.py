# Project 06: Student Academic Risk Classification
students = [("Akhil",[42,48,45],60,35),("Bina",[62,68,64],72,48),("Charu",[82,78,88],91,85),("Dinesh",[55,52,58],80,65),("Eman",[70,72,68],60,75)]
high_count = medium_count = low_count = 0
print("STUDENT ACADEMIC RISK REPORT")
for name,marks,attendance,lab in students:
    average = sum(marks)/len(marks); factors = []
    if average < 50: factors.append("low marks")
    if attendance < 65: factors.append("poor attendance")
    if lab < 40: factors.append("low laboratory score")
    if average < 50 or attendance < 65 or lab < 40: category="HIGH RISK"; high_count += 1
    elif average < 65 or attendance < 75 or lab < 50: category="MEDIUM RISK"; medium_count += 1
    else: category="LOW RISK"; low_count += 1
    if not factors: factors.append("no high-risk factor")
    print(name,"| Average:",round(average,2),"|",category,"|",", ".join(factors))
print("\nSUMMARY\nHigh risk:",high_count,"Medium risk:",medium_count,"Low risk:",low_count)