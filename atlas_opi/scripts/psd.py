#!/bin/python

# Description: This is the PSD script in scripts.opi

# from org.csstudio.opibuilder.scriptUtil import PVUtil # CSS BOY tools
import subprocess # For executing command-line stuff
import time # For sleeping
import os # For working with paths
from java.lang import System # Get Java environment variables

# The EPICS extensions version of caget does not support -S string
#   output.  Hence, we use the EPICS base version.  A linux-x86_64
#   binary has been included in the sdds directory

# This script will be executed from the directory containing the css
#   binary.  All paths will be relative to this location.

# Originally this was a shell script, but I changed it to a Python script
#   because it made path finding much easier.  I can tell CSS BOY to
#   execute from $(user.dir), which is where css was executed

# Get the absolute path of the css binary
css_dir_var = System.getProperty("osgi.install.area")
css_dir = css_dir_var.split(":")[1]

# cwd=css_loc
# export PATH=/usr/local/oag/apps/bin/linux-x86:$PATH
# Get the file save duration time as a variable
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-t", "LLRF4:FILE0:FileDurTime"], stdout=subprocess.PIPE, cwd=css_dir)
wait = p.communicate()[0]

# Add 2 seconds to the total wait time and sleep for that time
time.sleep(float(wait) + 2)

# Get the welch values
welch1 = PVUtil.getLong(display.getWidget("welch1").getPV())
welch2 = PVUtil.getLong(display.getWidget("welch2").getPV())

# Get the absolute path of the plotPSD script
# This is run from the css/CSS_EPICS directory
plotpath = os.path.abspath("../../sdds/plotPSD")

# Get the data file path as a string
p = subprocess.Popen(["../../sdds/caget_v2", "-St", "LLRF4:FILE0:FullFileName_RBV"], stdout=subprocess.PIPE, cwd=css_dir)
# If this PV is given a relative path, then the IOC treats it relative to the 
#    location where the IOC was started.  I can't get this info, so I can't
#    handle relative paths.  Despite the below code, only absolute paths work
filepath = p.communicate()[0] # Get the output of the above command
# If the user defined an absolute path, then it will be unchanged.
# If the user defined a relative path, it will be made absolute relative to
#    spxrfshare
filepath = os.path.abspath(filepath)

# run plotPSD from the directory of the user's data file
runpath = os.path.split(filepath)[0] # Get just the directory of the data file
subprocess.Popen([plotpath, filepath, str(welch1), str(welch2)], cwd=runpath) # Run plotPSD on the data file