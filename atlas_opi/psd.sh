#!/bin/bash

# The EPICS extensions version of caget does not support -S string
#	conversion.  Hence, we use the EPICS base version.  A linux-x86_64
#	binary has been included in the sdds directory

# Hit save button by setting save PV
caput LLRF4:FILE0:Capture 1

# Get the file save duration time as a variable
WAIT=`../../sdds/caget_v2 -t LLRF4:FILE0:FileDurTime`

# Add 2 seconds to the total wait time
TOTALWAIT=`echo "$WAIT+2" | bc`

# Wait for the necessary amount of time
sleep $TOTALWAIT

# Get the save path as a string and execute sdds using it
FILEPATH=`../../sdds/caget_v2 -St LLRF4:FILE0:FullFileName_RBV`
../../sdds/plotPSD $FILEPATH