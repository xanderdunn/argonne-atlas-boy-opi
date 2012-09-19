#!/bin/python

# Description: This is the script for the "Plot Last File" on front.opi

from org.csstudio.opibuilder.scriptUtil import PVUtil # CSS BOY tools
import subprocess # for 
from java.lang import System # Get Java environment variables
import string # for removing new lines

# The EPICS extensions version of caget does not support -S string
#   output.  Hence, we use the EPICS base version.  A linux-x86_64
#   binary has been included in the sdds directory

# This script will be executed from the directory containing the css
#   binary.  All paths will be relative to this location.

# Get macros
ts = display.getMacroValue("TS")
llrf = display.getMacroValue("LLRF")
fullpv = ts + llrf + ":FILE0:FullFileName_RBV" # concat

# Get the absolute path of the css binary
css_dir_var = System.getProperty("osgi.install.area")
css_dir = css_dir_var.split(":")[1]

# Get the last saved data file full path
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-St", fullpv], stdout=subprocess.PIPE, cwd=css_dir)
filepath = p.communicate()[0]

# Remove new lines
def rem(str0):
    return string.replace(str0, "\n", "")

# Execute the plotIQ script using the data file path
subprocess.Popen("../../sdds/plotIQ" + " " + rem(filepath), cwd=css_dir)
