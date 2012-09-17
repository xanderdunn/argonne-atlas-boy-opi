#!/bin/python

# Description: This is the script for the "Plot Last File" on front.opi

from org.csstudio.opibuilder.scriptUtil import PVUtil # CSS BOY tools
import subprocess

# The EPICS extensions version of caget does not support -S string
#   output.  Hence, we use the EPICS base version.  A linux-x86_64
#   binary has been included in the sdds directory

# This script will be executed from the directory containing the css
#   binary.  All paths will be relative to this location.

# Get macros
ts = display.getMacroValue("TS")
llrf = display.getMacroValue("LLRF")
fullpv = ts + llrf + ":FILE0:FullFileName_RBV" # concat

# Get the last saved data file full path
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-St", fullpv], stdout=subprocess.PIPE)
filepath = p.communicate()[0]

# Execute the plotIQ script using the data file path
p = subprocess.Popen(["../../sdds/plotIQ", filepath])