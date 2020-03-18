import yaml
import json

rst_path = "./source/restapi.rst"

f = open(rst_path, "r")

src = f.readlines()

i = 25

raw = []
data = []
current = ""

while i < len(src):
    s = src[i]
    i += 1
    if len(s) == 1:
        continue

    #Parse the titles above "====="
    if s.startswith("---"):
        name = raw[-1]
        data.append({name: name})
    #Parse method with "**"
    elif s.startswith("**"):
        url = s.replace("**", "").strip()
        data[-1]['url'] = url
    elif s.startswith("* "):
        current = s.replace("* ", "").replace(":", "").strip()
        data[-1][current] = []
    elif s.startswith("  - "):
        # print(current)
        data[-1][current].append(current + s.replace("  - ", "").strip())
    elif s.startswith(".. "):
        # restapi.rst line 363(Refresh Volume Bootmap Info) lacks "* Request"
        data[-1][current].append(current + s.replace(".. ", "").strip())
    else:
        raw.append(s.strip())

print(data)
