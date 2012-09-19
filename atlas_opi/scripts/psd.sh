#!/bin/bash

# Description: This script executes the plotPSD script, but first it sets the
#   path to improve compatibility with llrf2

# Arguments
# $1 == path to plotPSD
# $2 == path to data file to be plotted
# $3 == welch1 parameter
# $4 == welch2 parameter

echo "I have been called."

# Fix for llrf2
export PATH=/usr/local/oag/apps/bin/linux-x86:$PATH
# export | grep PATH

echo "Current working directory:"
pwd

echo "Parameters:"
echo $1
echo $2
echo $3
echo $4

$1 $2 $3 $4
