#Experiment 6: Regular Expression Matching and Searching

import re

text = "My email is student@gmail.com and my number is 9876543210."

print("Email:", re.search(r'\w+@\w+\.\w+', text).group())
print("Phone:", re.search(r'\d{10}', text).group())
print("All digits:", re.findall(r'\d+', text))
