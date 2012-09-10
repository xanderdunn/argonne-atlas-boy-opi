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

# Get the absolute path of the plotPSD script
# This is run from the css/CSS_EPICS directory
plotpath = os.path.abspath("../../sdds/plotPSD")

# Move into the spxrfshare directory, which is what the data file paths are
#    relative to
os.chdir("../../../../")

# Get the data file path as a string
p = subprocess.Popen(["../../sdds/caget_v2", "-St", "LLRF4:FILE0:FullFileName_RBV"], stdout=subprocess.PIPE)
filepath = p.communicate()[0] # Get the output of the above command
# If the user defined an absolute path, then it will be unchanged.
# If the user defined a relative path, it will be made absolute relative to
#    spxrfshare
filepath = os.path.abspath(filepath)

# run plotPSD from the directory of the user's data file
runpath = os.path.split(filepath)[0] # Get just the directory of the data file
subprocess.Popen([plotpath, filepath], cwd=runpath) # Run plotPSD on the data file