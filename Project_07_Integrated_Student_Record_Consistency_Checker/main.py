# Project 07: Integrated Student Record Consistency Checker
records = [("CSE101","Arun",85,92,"CSE"),("ECE102","Meena",76,88,"ECE"),("CSE101","Ravi",67,80,"CSE"),("EEE10A","Sita",105,75,"EEE"),("CSE105","",72,101,"XYZ")]
valid_courses = {"CSE","ECE","EEE"}; seen_ids = set()
print("STUDENT RECORD VALIDATION")
for student_id,name,marks,attendance,course in records:
    errors = []
    if len(student_id) != 6 or not student_id[:3].isalpha() or not student_id[3:].isdigit(): errors.append("invalid ID format")
    if student_id in seen_ids: errors.append("duplicate ID")
    seen_ids.add(student_id)
    if name.strip() == "": errors.append("missing name")
    if not 0 <= marks <= 100: errors.append("marks out of range")
    if not 0 <= attendance <= 100: errors.append("attendance out of range")
    if course not in valid_courses: errors.append("invalid course code")
    print(student_id,"- VALID" if not errors else "- INVALID: "+", ".join(errors))