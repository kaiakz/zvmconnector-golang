import yaml
import json

rst_path = "./source/restapi.rst"

f = open(rst_path, "r")

src = f.readlines()
f.close()
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
        data.append({'name': name})
    #Parse method with "**"
    elif s.startswith("**"):
        url = s.replace("**", "").strip()
        data[-1]['restapi'] = url
        # print(url)
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

def make_golang_func(api: str) -> str:
    return api.title().replace(" ", "")

f = open("gen.go", "w")

f.write('''package zvmconnector

import (
	"net/http"
	"os"
	"strconv"
)

''')

# uri := client.URI + "\\"
# req, _ := http.NewRequest("GET", uri, nil)
# req.Header.Add("Content-Type", "application/json")
# req.Header.Add("X-Auth-Token", client.authToken)
# res, _ := client.connect.Do(req)
# defer res.Body.Close()

def get_uri(uri: str) -> (str, str):
    return uri.split()

for i in data:
    f.write("func (client *RestClient) " + make_golang_func(i['name']) + '() {\n')
    uri = i['restapi'].split()
    f.write('\tclient.MakeRequest("{method}", "{path}", nil)'.format(method=uri[0], path=uri[1]))
    f.write('\n}\n\n')


f.close()