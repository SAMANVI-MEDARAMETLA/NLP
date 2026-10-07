import re

resume = """
Samanvi Medarametla
Email: samanvi@gmail.com
Mobile: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

name = re.search(r'^([A-Za-z ]+)', resume.strip()).group(1)
email = re.search(r'[\w.-]+@[\w.-]+\.\w+', resume).group()
mobile = re.search(r'\b\d{10}\b', resume).group()

skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = [s for s in skills
                if re.search(r'\b' + re.escape(s) + r'\b',
                             resume, re.IGNORECASE)]

experience = int(re.search(r'(\d+)\s*years?', resume,
                           re.IGNORECASE).group(1))

eligible = experience >= 2 and "Python" in found_skills

print("----- CANDIDATE PROFILE -----")
print("Name       :", name)
print("Email      :", email)
print("Mobile     :", mobile)
print("Skills     :", ", ".join(found_skills))
print("Experience :", experience, "years")
print("Eligible   :", "YES" if eligible else "NO")
