#!/bin/bash
caput LLRF4:FILE0:Capture 1
WAIT=`caget -t LLRF4:FILE0:FileDurTime`
TOTALWAIT=`echo "$WAIT+2" | bc`
sleep $TOTALWAIT
FILEPATH=`caget -t LLRF4:FILE0:FullFileName_RBV`
