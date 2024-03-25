#!/bin/bash
set -e # Make whole script fail if anything fails

LOG=/tmp/nms_omnibus_uninstall.log
BASEDIR=/opt/viasat/deployments/makefile_lib

echo "Uninstalling Netcool Omnibus"
make -f $BASEDIR/products/omnibus_core_8_1_0_19.mk uninstall NETCOOL_PA_NAME=${PA_NAME} >> $LOG
