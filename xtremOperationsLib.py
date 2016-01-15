import requests, json, sys
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
#Utility Functions
def getResponseStatus(response):
    if response.status_code == 200:
        return 0
    else:
        return response.status_code

#Volume APIs
def getVolumes(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    
def getVolumeDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/volumes?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def createVolume(ip,user,pwd,volname,volsize):
    try:
        data = {'vol-name':volname,'vol-size':volsize}
        response = requests.post('https://%s/api/json/v2/types/volumes/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def extendVolume(ip,user,pwd,volname,volsize):
    try:
        data = {'vol-size':volsize}
        response = requests.put('https://%s/api/json/v2/types/volumes/?name=%s'%(ip,volname),data=json.dumps(data),auth=(user,pwd),verify=False)
        if response.status_code == 200:
            return 0
        else:
            return response.status_code
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def deleteVolume(ip,user,pwd,volname):
    try:
        response = requests.delete('https://%s/api/json/v2/types/volumes?name=%s'%(ip,volname),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    
#Initiator and Initiator Group APIs
def getInitiatorGroups(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/initiator-groups/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getInitiatorGroupDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/initiator-groups?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1
    
def createInitiatorGroup(ip,user,pwd,igname):
    try:
        data = {'ig-name':igname}
        response = requests.post('https://%s/api/json/v2/types/initiator-groups/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def deleteInitiatorGroup(ip,user,pwd,igname):
    try:
        response = requests.delete('https://%s/api/json/v2/types/initiator-groups?name=%s'%(ip,igname),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getInitiators(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/initiators/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getInitiatorDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/initiators?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def createInitiator(ip,user,pwd,igname,name,address):
    try:
        data = {'ig-name':igname,'initiator-name':name,'port-address':address}
        response = requests.post('https://%s/api/json/v2/types/initiator-groups/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def deleteInitiator(ip,user,pwd,name):
    try:
        response = requests.delete('https://%s/api/json/v2/types/initiators?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Snapshot API
def createSnapshotOnVolume(ip,user,pwd,vollist=None):
    try:
        data = {'volume-list':vollist}
        response = requests.post('https://%s/api/json/v2/types/snapshots/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def createSnapshotOnCG(ip,user,pwd,cgname):
    try:
        data = {'consistency-group-id':int(getConsistencyGroupDetails(ip,user,pwd,cgname)['content']['index'])}
        response = requests.post('https://%s/api/json/v2/types/snapshots/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getSnapshots(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/snapshots/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def deleteSnapshot(ip,user,pwd,name):
    try:
        response = requests.delete('https://%s/api/json/v2/types/snapshots?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Snapshot set API
def getSnapshotSets(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/snapshot-sets/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getSnapshotSetDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/snapshot-sets?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def deleteSnapshotSet(ip,user,pwd,name):
    try:
        response = requests.delete('https://%s/api/json/v2/types/snapshot-sets?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Consistency Group API
def deleteConsistencyGroup(ip,user,pwd,name):
    try:
        response = requests.delete('https://%s/api/json/v2/types/consistency-groups?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getConsistencyGroups(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/consistency-groups/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getConsistencyGroupDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/consistency-groups?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def createConsistencyGroup(ip,user,pwd,cgname):
    try:
        data = {'consistency-group-name':cgname}
        response = requests.post('https://%s/api/json/v2/types/consistency-groups/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def addVolumeToCG(ip,user,pwd,cgname,volname):
    try:
        data = {'cg-id':cgname,'vol-id':volname}
        response = requests.post('https://%s/api/json/v2/types/consistency-group-volumes/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def removeVolumeFromCG(ip,user,pwd,cgname,volname):
    try:
        data = {'cg-id':cgname,'vol-id':volname}
        response = requests.delete('https://%s/api/json/v2/types/consistency-group-volumes?name=%s'%(ip,cgname),data=json.dumps(data),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#lunmapping API

def addLunMapping(ip,user,pwd,volname,igname):
    try:
        data = {'vol-id':volname,'ig-id':igname}
        response = requests.post('https://%s/api/json/v2/types/lun-maps/'%(ip),data=json.dumps(data),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getLunMappings(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/lun-maps/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getLunMappingDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/lun-maps?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Tags API
def deleteTag(ip,user,pwd,name):
    try:
        response = requests.delete('https://%s/api/json/v2/types/tags?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getTags(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/tags/'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Targets and Target groups
def getTargetGroups(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/target-groups'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getTargetGroupDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/target-groups?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getTargets(ip,user,pwd):
    try:
        response = requests.get('https://%s/api/json/v2/types/targets'%(ip),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

def getTargetDetails(ip,user,pwd,name):
    try:
        response = requests.get('https://%s/api/json/v2/types/targets?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1

#Scheduler API
def deleteScheduler(ip,user,pwd,name):
    try:
        response = requests.delete('https://%s/api/json/v2/types/schedulers?name=%s'%(ip,name),auth=(user,pwd),verify=False)
        return getResponseStatus(response)
    except requests.exceptions.RequestException as e:
        print "Error:",e
        return 1