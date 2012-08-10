from org.csstudio.opibuilder.scriptUtil import PVUtil
import time

# pvs[0] = loc://scan = Is this a power scan or freq scan?
# pvs[1] = loc://startfreq
# pvs[2] = loc://stopfreq
# pvs[3] = loc://stepfreq
# pvs[4] = loc://startpwr
# pvs[5] = loc://stoppwr
# pvs[6] = loc://steppwr
# pvs[7] = loc://stepint
# pvs[8] = = PV that controls the device frequency
# pvs[9] = = PV that controls the device power

def main():
    scan = PVUtil.getLong(pvs[0])
    # Frequency Scan
    if (scan == 1):
        start = PVUtil.getDouble(pvs[1])
        stop = PVUtil.getDouble(pvs[2])
        step = PVUtil.getDouble(pvs[3])
        curr = PVUtil.getDouble(pvs[8])
    # Power Scan
    elif (scan == 2):
        start = PVUtil.getDouble(pvs[4])
        stop = PVUtil.getDouble(pvs[5])
        step = PVUtil.getDouble(pvs[6])
        curr = PVUtil.getDouble(pvs[9])

    stepint = PVUtil.getDouble(pvs[7])
    while (curr < stop):
        curr = curr + step
        # Set the device to achieve this value
        if (scan == 1):
            pvs[8].setValue(curr)
        elif (scan == 2):
            pvs[9].setValue(curr)
        # Wait stepint seconds before next scan
        time.sleep(stepint)
    
    # Reset the scan indicator to 0
    pvs[0].setValue(0)
    
if __name__ == '__main__':
    main()