#!/bin/python

# Description: This is the script for the "Plot Last File" on front.opi

import subprocess # for executing shell commands
from java.lang import System # Get Java environment variables
import string # for removing new lines
from defs import * # local library with common definitions

# The EPICS extensions version of caget does not support -S string
#   output.  Hence, we use the EPICS base version.  A linux-x86_64
#   binary has been included in the sdds directory

# This script will be executed from the directory containing the css
#   binary.  All paths will be relative to this location.

# Get macros
fullpv = ts + llrf + ":FILE0:FullFileName_RBV" # concat

# Get the last saved data file full path
# This is run from ops/cavCtl/css/CSS_EPICS/
p = subprocess.Popen(["../../sdds/caget_v2", "-St", fullpv], stdout=subprocess.PIPE, cwd=css_dir)
filepath = p.communicate()[0]

# Execute the plotIQ script using the data file path
subprocess.Popen(["../../sdds/plotIQ", rem(filepath)], cwd=css_dir)
