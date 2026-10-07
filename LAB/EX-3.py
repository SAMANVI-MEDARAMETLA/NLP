#Experiment 3: Regular Expression Operations
import re

text = "call me on 12/10/2026 at 9876543210 or email test@gmail.com. Also call 9123456789."

# 1. Find first date
print("First date:", re.search(r'\d{2}/\d{2}/\d{4}', text).group())

# 2. Find all mobile numbers
print("Mobile numbers:", re.findall(r'\b[6-9]\d{9}\b', text))

# 3. Find all email IDs
print("Email IDs:", re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text))

# 4. Check whether text starts with "call"
print("Starts with call:", text.lower().startswith("call"))

# 5. Change date format DD/MM/YYYY → YYYY-MM-DD
text = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text)
print("Changed date:", text)

# 6. Hide phone numbers
text = re.sub(r'\b[6-9]\d{9}\b', 'XXXXXXXXXX', text)
print("Hidden numbers:", text)
