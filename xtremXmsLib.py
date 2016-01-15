import requests, json, sys
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

def getXms(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xms/?name=xms' %(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getXmsReadlatency(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['rd-latency']

def getXmsWritelatency(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['wr-latency']

def getXmsReadBandwidth(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return float(json.loads(response.text)['content']['rd-bw'])/1000

def getXmsWriteBandwidth(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return float(json.loads(response.text)['content']['wr-bw'])/1000

def getXmsBandwidth(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return float(json.loads(response.text)['content']['bw'])/1000

def getXmsReadIops(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['rd-iops']

def getXmsWriteIops(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['wr-iops']

def getXmsIops(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=xms' %(ip),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['iops']