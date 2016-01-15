# PyXtrem
PyXtrem is a library comprising of python modules that simplifies the consumption of XtremIO REST API.

## Description
PyXtrem is a library comprising of python modules that simplifies the consumption of XtremIO REST API. The library comprises of 
- xtremHardwareLib.py – Functions wrapping REST queries to XtremIO that get details of hardware aspects of XtremIO cluster
- xtremOperationsLib.py – Functions wrapping REST queries to XtremIO that can create, delete and get details of XtremIO objects objects like volumes, snapshot, initiators and initiator groups
- xtremXenvLib.py – Functions wrapping REST query to get details of X environment. There are utility functions that leverage REST query in getting performance stats on single volume
- xtremXmsLib.py – Functions wrapping REST query that get details of XMS. It also has utility functions that leverage REST query in performance stats at the scope of entire XtremIO cluster

Users can automate workflows related to XtremIO management functions such as adding/deleting an XtremIO volume, initiator or initiator group, consistency groups, creating snapshots on volumes or consistency groups, refreshing a snapshot and many more.

## Installation
Download the python files and copy in the them in your working directory.

## Usage Instructions
In your python program that is meant to automate certain set of tasks for XtremiO, just import the necessary or all the python modules and start invoking functions defined in these. Typically, you would need to pass XtremIO IP address, username and password and other parameters
```
import xtremXenvLib
import xtremXmsLib
import xtremOperationsLib
import xtremHardwareLib

xtremOperationsLib.createVolume(""1.1.1.1","username","password","TEST-Volume","500g")
xtremOperationsLib.getVolumeDetails("1.1.1.1","username","password","TEST-Volume")
xtremOperationsLib.createSnapshot("1.1.1.1","username","password",["Test-Volume"])

xtremXmsLib.getXms("1.1.1.1","username","password")

xtremXenvLib.getXenvs("1.1.1.1","username","password")

xtremHardwareLib.getXbricks("1.1.1.1","username","password")
```

## Future
Currently, wrapper functions for critical activities related to volumes, consistency groups, snapshots, are added. In future, wrapper functions will be added for 
- ISCSI initiators
- DPG
- Schedulers
- Notifiers (SYR, SNMP, SYSLOG))

## Contribution
Create a fork of the project into your own reposity. Make all your necessary changes and create a pull request with a description on what was added or removed and details explaining the changes in lines of code. If approved, project owners will merge it.

Licensing
---------
PyXtrem is freely distributed under the [MIT License](http://emccode.github.io/sampledocs/LICENSE "LICENSE"). See LICENSE for details.


Support
-------
Please file bugs and issues on the Github issues page for this project. This is to help keep track and document everything related to this repo. For general discussions and further support you can join the [EMC {code} Community slack channel](http://community.emccode.com/). Lastly, for questions asked on [Stackoverflow.com](https://stackoverflow.com) please tag them with **EMC**. The code and documentation are released with no warranties or SLAs and are intended to be supported through a community driven process.
