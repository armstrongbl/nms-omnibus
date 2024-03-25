# nms-omnibus

## Build Status
[![Build Status](https://jenkins-pp.viasat.com/buildStatus/icon?job=NBN-NMS/nms-omnibus)](https://jenkins-pp.viasat.com/job/NBN-NMS/view/Dockerized/job/nms-omnibus/)

## Build rpm using "fpm"

EPOCH=`date +"%s"`; fpm -n "nms-omnibus" --iteration $EPOCH --vendor "Viasat" --version 5.0.0.2 --after-install /opt/viasat/deployments/makefile_lib/utils/after-nco-install.sh --category Monitoring -s dir -t rpm /opt/viasat/deployments

Command details:  
EPOCH=`date +"%s"`;  
	Sets "EPOCH" variable and assigns the returned value of the "date" command in seconds since epoch format.

fpm 
```
	-n "nms-omnibus"  ##name of package
	--iteration $EPOCH ## Build iteration
	--vendor "Viasat"  ### Vendor
	--version 5.0.0.2 ### Build Version
	--after-install /opt/viasat/deployments/makefile_lib/utils/after-nco-install.sh ### Script to run after the rpm has been installed.  Wrapper script for installer.
	--category Monitoring ### Software / Package category 
	-s dir ### Source type for rpm package.  dir for "directory"
	-t rpm ### Output type of rpm
	/opt/viasat/deployments ### Directory to package based on -s flag above.  This must be last in the command.
```

Where to find proper install packages:
```
	There are two locations.  
		1. Windows jumpbox d01-jumpnms01.gmtl.viasat.com E:\Software\IBM\NOI
		2. The "nfs" share on the nmsfms* vm's in /opt/viasat/ibmrepo
```

Needed install packages:
```
precheck_unix_20150827.tar
TVL_NTCL_OMN_V8.1.0.19_CORE_LNX_M.zip
CN4FYEN_SYSLOG.zip
CN4FZEN_MTTRAPD_v20.zip
im-nco-g-jdbc-5_0.zip
im-nco-p-ping-7_0.zip
```
