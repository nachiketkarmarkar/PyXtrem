import requests, json, sys
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

def getXenvs(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/' %(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getXenvUtil(ip,name,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/xenvs/?name=%s' %(ip,name),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['cpu-usage']

def getVolumeReadLatency(ip,name,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes/?name=%s' %(ip,name),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['rd-latency']

def getVolumeWriteLatency(ip,name,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes/?name=%s' %(ip,name),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['wr-latency']

def getVolumeIops(ip,name,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes/?name=%s' %(ip,name),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['iops']

def getVolumeReadBandwidth(ip,name,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes/?name=%s' %(ip,name),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['rd-bw']

def getVolumeWriteBandwidth(ip,name,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes/?name=%s' %(ip,name),auth=(user,pwd),verify=False)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    if response.status_code == 200:
       return json.loads(response.text)['content']['wr-bw']