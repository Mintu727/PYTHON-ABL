# Project 10: Comprehensive Smart Campus Management Simulation
students = [("S101","Aarav",88,[80,85,90]),("S102","Diya",70,[72,68,75]),("S103","Kabir",92,[91,89,94])]
events = ["Tech Fest","Sports Day"]; registrations = [[],[]]
def find_student(student_id):
    for student in students:
        if student[0] == student_id: return student
    return None
choice = -1
while choice != 0:
    print("\nSMART CAMPUS MENU\n1. View student records\n2. Check attendance eligibility\n3. Register for an event\n4. Campus summary\n0. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        for sid,name,attendance,marks in students: print(sid,name,"Attendance:",attendance,"Average marks:",round(sum(marks)/len(marks),2))
    elif choice == 2:
        for sid,name,attendance,marks in students: print(sid,name,"-","Eligible" if attendance >= 75 else "Short attendance")
    elif choice == 3:
        sid = input("Enter student ID: ").strip(); print("Events:",events); event = input("Enter event name: ").strip(); student = find_student(sid)
        if student is None: print("Student ID not found.")
        elif event not in events: print("Invalid event.")
        else:
            index = events.index(event)
            if sid in registrations[index]: print("Duplicate registration rejected.")
            else: registrations[index].append(sid); print("Registration successful.")
    elif choice == 4:
        marks = [mark for student in students for mark in student[3]]
        print("Total students:",len(students),"Total event registrations:",sum(len(x) for x in registrations),"Overall marks average:",round(sum(marks)/len(marks),2))
    elif choice == 0: print("Exiting Smart Campus System.")
    else: print("Invalid choice. Try again.")