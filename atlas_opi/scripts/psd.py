#!/bin/python

# Description: This is the PSD script in scripts.opi

# from org.csstudio.opibuilder.scriptUtil import PVUtil # CSS BOY tools
import subprocess # For executing command-line stuff
import time # For sleeping
import os # For working with paths

# The EPICS extensions version of caget does not support -S string
#   output.  Hence, we use the EPICS base version.  A linux-x86_64
#   binary has been included in the sdds directory

# This script will be executed from the directory containing the css
#   binary.  All paths will be relative to this location.

# Originally this was a shell script, but I changed it to a Python script
#   because it made path finding much easier.  I can tell CSS BOY to
#   execute from $(user.dir), which is where css was executed

# Hit save button by setting save PV
subprocess.Popen(["caput", "LLRF4:FILE0:Capture", "1"])

# Get the file save duration time as a variable
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-t", "LLRF4:FILE0:FileDurTime"], stdout=subprocess.PIPE)
wait = p.communicate()[0]

# Add 2 seconds to the total wait time and sleep for that time
time.sleep(float(wait) + 2)

# Get the file path as a string
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-St", "LLRF4:FILE0:FullFileName_RBV"], stdout=subprocess.PIPE)
filepath = p.communicate()[0] # Get the output of the above command
filepath = os.path.abspath(filepath) # Make it an absolute path
# If the given path is relative, make it absolute relative to the spxrfshare directory
plotpath = os.path.abspath(["../../sdds/plotPSD"], cwd="../../../../") # Get absolute path of plotPSD
# The following is run from the directory of the user's save file
# runpath = os.path.split(filepath)[0] # Get just the directory of the save file
runpath = os.path.split(plotpath)[0] # Get just the directory of the plotter location
subprocess.Popen([plotpath, filepath], cwd=runpath) # Run plotPSD on the saved file
