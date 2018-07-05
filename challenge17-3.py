import re

line = "The ghose that says boo haunts the loo"
m = re.findall(".oo", line)
print(m)
