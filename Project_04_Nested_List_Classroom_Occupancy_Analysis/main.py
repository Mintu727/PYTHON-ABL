# Project 04: Nested List Classroom Occupancy Analysis
classroom = [[0,0,"RESERVED",0],[0,0,0,0],[0,"RESERVED",0,0]]
students = ["R101","R102","R103","R104","R105","R102","R106","R107"]
allocated, duplicates, unallocated = set(), [], []
for roll in students:
    if roll in allocated: duplicates.append(roll); continue
    seat_found = False
    for row in range(len(classroom)):
        for col in range(len(classroom[row])):
            if classroom[row][col] == 0 and not seat_found:
                classroom[row][col] = roll; allocated.add(roll); seat_found = True
    if not seat_found: unallocated.append(roll)
occupied = reserved = vacant = 0
print("CLASSROOM SEATING MATRIX")
for row in classroom:
    print(row)
    for seat in row:
        if seat == "RESERVED": reserved += 1
        elif seat == 0: vacant += 1
        else: occupied += 1
print("\nOccupied seats:",occupied,"Reserved seats:",reserved,"Vacant seats:",vacant)
print("Duplicate roll numbers:",duplicates)
print("Unallocated students:",unallocated)