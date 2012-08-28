from org.csstudio.opibuilder.scriptUtil import PVUtil

#PVs
# pvs[0] = loc://rescale
# pvs[1] = $(TS)LLRF4:STATS0:S$(CAV)_mean_ampl
# pvs[2] = $(TS)LLRF4:STATS0:S$(FWD)_mean_ampl
# pvs[3] = $(TS)LLRF4:STATS0:S$(REV)_mean_ampl
# pvs[5] = $(TS)LLRF4:STATS0:S$(CAV)_mean_phase
# pvs[6] = $(TS)LLRF4:STATS0:S$(FWD)_mean_phase
# pvs[7] = $(TS)LLRF4:STATS0:S$(REV)_mean_phase
# pvs[9] = loc://offset1
# pvs[10] = loc://offset2
# pvs[11] = loc://offset3
# pvs[12] = loc://offset4
# pvs[13] = loc://offset5
# pvs[14] = loc://offset6

def main():
    # Ampl
    if PVUtil.getLong(pvs[0]) == 1:
        graph = "TopGraph"
        # CAV Ampl
        offset1 = PVUtil.getDouble(pvs[9])
        # FWD Ampl
        offset2 = PVUtil.getDouble(pvs[10])
        # REV Ampl
        offset3 = PVUtil.getDouble(pvs[11])
        
    # Phase
    if PVUtil.getLong(pvs[0]) == 2:
        graph = "BottomGraph"
        # CAV Phase
        offset1 = PVUtil.getDouble(pvs[12])
        # FWD Phase
        offset2 = PVUtil.getDouble(pvs[13])
        # REV Phase
        offset3 = PVUtil.getDouble(pvs[14])

    # Execute the commands only if the button has been pressed
    if PVUtil.getLong(pvs[0]) != 0:
        # Get the graph widget and turn off autoscale
        display.getWidget(graph).setPropertyValue("axis_1_auto_scale", "0")
        display.getWidget(graph).setPropertyValue("axis_2_auto_scale", "0")
        display.getWidget(graph).setPropertyValue("axis_3_auto_scale", "0")
            
        # Set the max and min values of the y-axis
        display.getWidget(graph).setPropertyValue("axis_1_maximum", PVUtil.getFloat(pvs[1]) + PVUtil.getLong(pvs[9]))
        display.getWidget(graph).setPropertyValue("axis_1_minimum", PVUtil.getFloat(pvs[2]) - PVUtil.getLong(pvs[10]))
        display.getWidget(graph).setPropertyValue("axis_2_maximum", PVUtil.getFloat(pvs[3]) + PVUtil.getLong(pvs[11]))
        display.getWidget(graph).setPropertyValue("axis_2_minimum", PVUtil.getFloat(pvs[4]) - PVUtil.getLong(pvs[12]))
        display.getWidget(graph).setPropertyValue("axis_3_maximum", PVUtil.getFloat(pvs[5]) + PVUtil.getLong(pvs[13]))
        display.getWidget(graph).setPropertyValue("axis_3_minimum", PVUtil.getFloat(pvs[6]) - PVUtil.getLong(pvs[14]))
            
        # Reset the rescale action indicator to 0
        pvs[0].setValue(0)

if __name__ == '__main__':
    main()

