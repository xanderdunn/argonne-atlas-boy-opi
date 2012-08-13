from org.csstudio.opibuilder.scriptUtil import PVUtil
import time
import sys

# pvs[0] = loc://scan = Is this a power scan or freq scan?
# pvs[1] = loc://startfreq
# pvs[2] = loc://stopfreq
# pvs[3] = loc://stepfreq
# pvs[4] = loc://startpwr
# pvs[5] = loc://stoppwr
# pvs[6] = loc://steppwr
# pvs[7] = loc://stepint1
# pvs[8] = loc://stepint2
# TODO: Need to be changed to actual hardware PVs:
# pvs[9] = loc://freq = PV that controls the device frequency
# pvs10] = loc://pwr = PV that controls the device power

def main():
    scan = PVUtil.getLong(pvs[0])
    # Frequency Scan
    if (scan == 1):
        start = PVUtil.getDouble(pvs[1])
        stop = PVUtil.getDouble(pvs[2])
        step = PVUtil.getDouble(pvs[3])/1000 # Convert to GHz
        stepint = PVUtil.getDouble(pvs[7])
    # Power Scan
    else:
        start = PVUtil.getDouble(pvs[4])
        stop = PVUtil.getDouble(pvs[5])
        step = PVUtil.getDouble(pvs[6])
        stepint = PVUtil.getDouble(pvs[8])

    # Set initial current state
    curr = start
    # Step until reach stop
    while (curr < stop):
        # Set the device to achieve this value
        if (scan == 1):
            pvs[9].setValue(curr)
        elif (scan == 2):
            pvs[10].setValue(curr)
        curr = curr + step
        # Wait stepint seconds before next scan
        time.sleep(stepint)
    
    # Reset the scan indicator to 0
    pvs[0].setValue(0)
    # Reset the starting position
    if (scan == 1):
        pvs[9].setValue(start)
    elif (scan == 2):
        pvs[10].setValue(start)
    
    # time.sleep(10)
    
if __name__ == '__main__':
    main()