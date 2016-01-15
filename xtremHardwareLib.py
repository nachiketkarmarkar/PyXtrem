import requests, json, sys
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
#Utility Functions
def getResponseStatus(response):
    if response.status_code == 200:
        return 0
    else:
        return response.status_code

#Cluster APIs
def getClusters(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/clusters/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getClusterDetails(ip,user,name,clusterName):
    try:
        response = requests.get('https://%s/api/json/v2/types/clusters?name=%s'%(ip,clusterName),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#X-Brick APIs
def getXbricks(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/bricks/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getXbrickDetails(ip,user,name,brickId):
    try:
        response = requests.get('https://%s/api/json/v2/types/bricks?brick-id=%s'%(ip,brickId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#SSD APIs
def getSsds(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/ssds/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getSsdDetails(ip,user,pwd,ssdId):
    try:
        response = requests.get('https://%s/api/json/v2/types/ssds?ssd-id=%s'%(ip,ssdId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#slots API
def getSlots(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/slots/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getSlotDetails(ip,user,pwd,slotId):
    try:
        response = requests.get('https://%s/api/json/v2/types/slots?slot-id=%s'%(ip,slotId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#BBU API
def getBbus(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/bbus/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getBbuDetails(ip,user,pwd,bbuId):
    try:
        response = requests.get('https://%s/api/json/v2/types/bbus?bbu-id=%s'%(ip,bbuId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#IB switch API
def getIbSwitches(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/infiniband-switches/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getIbSwitchDetails(ip,user,pwd,ibId):
    try:
        response = requests.get('https://%s/api/json/v2/types/infiniband-switches?infiniband-switch-id=%s'%(ip,ibId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#DAE API
def getDaes(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/daes/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getDaeDetails(ip,user,pwd,daeId):
    try:
        response = requests.get('https://%s/api/json/v2/types/daes?dae-id=%s'%(ip,daeId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#DAE Controller API
def getDaeControllers(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/dae-controllers/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getDaeControllerDetails(ip,user,pwd,daeContollerId):
    try:
        response = requests.get('https://%s/api/json/v2/types/dae-controllers?dae-controllers-id=%s'%(ip,daeControllerId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#DAE PSU API
def getDaePsus(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/dae-psus/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getDaePsuDetails(ip,user,pwd,daePsuId):
    try:
        response = requests.get('https://%s/api/json/v2/types/dae-psus?dae-psus-id=%s'%(ip,daePsuId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#local-disks
def getLocalDisks(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/local-disks/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getLocalDiskDetails(ip,user,pwd,localDiskId):
    try:
        response = requests.get('https://%s/api/json/v2/types/local-disks?local-disk-id=%s'%(ip,ocalDiskId),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Storage controller API
def getStorageContollers(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/storage-controllers/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getStorageControllerDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/storage-controllers?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Storage controller PSUs
def getStorageContollerPsus(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/storage-controller-psus/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getStorageControllerPsuDetails(ip,user,pwd,scPsuName):
    try:
        response = requests.get('https://%s/api/json/v2/types/storage-controller-psus?name=%s'%(ip,scPsuName),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1