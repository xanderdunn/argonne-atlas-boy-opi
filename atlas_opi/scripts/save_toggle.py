#!/bin/python

from org.csstudio.opibuilder.scriptUtil import PVUtil

# If it is taking data, then stop by writing 0
# It it is not taking data, then start by writing 1

get_pv = display.getWidget("Capture_Indicator").getPV()
set_pv = display.getWidget("Save_Button").getPV()

def main():
	# Get current PV value
	curr = PVUtil.getLong(get_pv)
	# If currently 0, then set to 1
	if curr == 0:
		print "Setting to 1"
		set_pv.setValue(1)
	# If currently 1, then set to 0
	if curr == 1:
		print "Setting to 0"
		set_pv.setValue(0)

if __name__ == '__main__':
    main()
