#!/bin/python

# Description: Automatically turn on or off the frequency offset
#    based on the frequency offset value

from org.csstudio.opibuilder.scriptUtil import PVUtil

# pvs[0] = $(TS)$(LLRF):DRV0:sel2_phstep_ao
# pvs[1] = $(TS)$(LLRF):DRV0:sel2_dds_bo

# Get the PVs
get_pv = display.getWidget("sel2_phstep").getPV()
set_pv = display.getWidget("sel2_dds").getPV()

# Get the scalar value
val = PVUtil.getLong(get_pv)

# Set the boolean value based on this:
if val != 0:
    set_pv.setValue(1) # Turn it on
elif val == 0:
    set_pv.setValue(0) # Turn it off