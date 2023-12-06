import re
text = "jhony deep is a wonderfull actor"
match = r"deep"
find = re.match(match, text)
if find:
    print("jhony " + find.group())
else:
    print ("not found")
