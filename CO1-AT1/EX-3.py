import re

register_no = "22A81A0001"
email = "samanvi@university.edu"
course_code = "AIML101"
semester = "6"
mobile = "9876543210"

valid = True

if re.fullmatch(r'\d{2}[A-Z]{2}\d[A-Z]\d{4}', register_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    valid = False

if re.fullmatch(r'[a-zA-Z0-9._%+-]+@university\.edu', email):
    print("Email           : Valid")
else:
    print("Email           : Invalid")
    valid = False

if re.fullmatch(r'[A-Z]{4}\d{3}', course_code):
    print("Course Code     : Valid")
else:
    print("Course Code     : Invalid")
    valid = False

if re.fullmatch(r'[1-8]', semester):
    print("Semester        : Valid")
else:
    print("Semester        : Invalid")
    valid = False

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Mobile Number   : Valid")
else:
    print("Mobile Number   : Invalid")
    valid = False

print("\n----- REGISTRATION STATUS -----")

if valid:
    print("Registration Successful")
else:
    print("Registration Failed")
