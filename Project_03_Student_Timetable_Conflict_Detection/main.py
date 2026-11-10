# Project 03: Student Timetable Conflict Detection
timetable = [("Python","Monday",540,600,"Lab-1"),("Mathematics","Monday",585,645,"Room-2"),("Physics","Monday",650,710,"Lab-1"),("English","Tuesday",540,600,"Room-2"),("Chemistry","Monday",550,590,"Lab-1")]
def show_time(value): return str(value//60).zfill(2) + ":" + str(value%60).zfill(2)
student_clashes = room_clashes = 0
print("TIMETABLE CONFLICT REPORT")
for i in range(len(timetable)):
    c1,d1,s1,e1,r1 = timetable[i]
    for j in range(i+1,len(timetable)):
        c2,d2,s2,e2,r2 = timetable[j]
        if d1 == d2 and s1 < e2 and s2 < e1:
            student_clashes += 1
            print("Student clash:",c1,"and",c2,"on",d1,show_time(max(s1,s2)),"to",show_time(min(e1,e2)))
            if r1 == r2: room_clashes += 1; print(" Room clash in",r1)
if student_clashes == 0: print("No student timetable clashes found.")
print("Total student clashes:",student_clashes)
print("Total room clashes:",room_clashes)