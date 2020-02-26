import re
string = "88tT"
patterns = [ r"[A-Z]{1}", r"[a-z]{1}", r"\W"]

for pattern in patterns:
    match = re.search(pattern,string)
    if match == None:
        print("Password must contain Uppercase or lower case and Special Characters")
        break
    else:
        pass
