#!/bin/python

# Description: This is the PSD script in scripts.opi

from org.csstudio.opibuilder.scriptUtil import PVUtil # for CSS BOY tools
import subprocess # for executing command-line stuff
import time # for sleeping
import os # for working with paths
from java.lang import System # for getting Java environment variables
import string # for replacing characters
from defs import * # local file with directory definitions

# The EPICS extensions version of caget does not support -S string
#   output.  Hence, we use the EPICS base version.  A linux-x86_64
#   binary named caget_v2 has been included in the sdds directory

# This script will be executed from the directory containing the css
#   binary.  All paths will be relative to this location.

# Originally this was a shell script, but I changed it to a Python script
#   because it made path finding much easier.  I can tell CSS BOY to
#   execute from $(user.dir), which is where css was executed

# Get the file save duration time as a variable
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-t", "LLRF4:FILE0:FileDurTime"], stdout=subprocess.PIPE, cwd=css_dir)
wait = p.communicate()[0]

# Add 2 seconds to the total wait time and sleep for that time
time.sleep(float(wait) + 2)

# Get the local welch values
welch1 = str(PVUtil.getLong(display.getWidget("welch1").getPV()))
welch2 = str(PVUtil.getLong(display.getWidget("welch2").getPV()))

# Get the absolute path of the plotPSD script
# This is run from the css/CSS_EPICS directory
plotpath = os.path.normpath(os.path.join(css_dir, "../../sdds/plotPSD"))

# Get the data file path as a string
p = subprocess.Popen(["../../sdds/caget_v2", "-St", "LLRF4:FILE0:FullFileName_RBV"], stdout=subprocess.PIPE, cwd=css_dir)
filepath = p.communicate()[0] # Get the output of the above command
# If this PV is given a relative path, then the IOC treats it relative to the 
#    location where the IOC was started.  I can't get this info, so I can't
#    handle relative paths.  Only absolute paths work
# filepath = os.path.abspath(filepath)

# Get the location of the bash script that will be run
script_path = workspace_dir + "atlas_opi/scripts/psd.sh"

# run plotPSD from the directory of the user's data file
runpath = os.path.split(filepath)[0] # Get just the directory of the data file
subprocess.Popen([rem(script_path) + " " + rem(plotpath) + " " + rem(filepath) + " " + rem(welch1) + " " + rem(welch2)], cwd=runpath, shell=True)
