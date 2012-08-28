from org.csstudio.opibuilder.scriptUtil import PVUtil

#PVs
# pvs[0] = loc://rescale
# pvs[1] = $(TS)LLRF4:STATS0:S$(CAV)_mean_ampl
# pvs[2] = $(TS)LLRF4:STATS0:S$(FWD)_mean_ampl
# pvs[3] = $(TS)LLRF4:STATS0:S$(REV)_mean_ampl
# pvs[4] = $(TS)LLRF4:STATS0:S$(CAV)_mean_phase
# pvs[5] = $(TS)LLRF4:STATS0:S$(FWD)_mean_phase
# pvs[6] = $(TS)LLRF4:STATS0:S$(REV)_mean_phase
# pvs[7] = loc://offset1
# pvs[8] = loc://offset2
# pvs[9] = loc://offset3
# pvs[10] = loc://offset4
# pvs[11] = loc://offset5
# pvs[12] = loc://offset6

def main():
    # Ampl
    if PVUtil.getLong(pvs[0]) == 1:
        graph = "TopGraph"
        # CAV Ampl
        offset1 = PVUtil.getDouble(pvs[7])
        one = PVUtil.getDouble(pvs[1])
        # FWD Ampl
        offset2 = PVUtil.getDouble(pvs[8])
        two = PVUtil.getDouble(pvs[2])
        # REV Ampl
        offset3 = PVUtil.getDouble(pvs[9])
        three = PVUtil.getDouble(pvs[3])
        
    # Phase
    if PVUtil.getLong(pvs[0]) == 2:
        graph = "BottomGraph"
        # CAV Phase offset and magnitude
        offset1 = PVUtil.getDouble(pvs[10])
        one = PVUtil.getDouble(pvs[4])
        # FWD Phase offset and magnitude
        offset2 = PVUtil.getDouble(pvs[11])
        two = PVUtil.getDouble(pvs[5])
        # REV Phase offset and magnitude
        offset3 = PVUtil.getDouble(pvs[12])
        three = PVUtil.getDouble(pvs[6])

    # Execute the commands only if the button has been pressed
    if PVUtil.getLong(pvs[0]) != 0:
        # Get the graph widget and turn off autoscale
        display.getWidget(graph).setPropertyValue("axis_1_auto_scale", "0")
        display.getWidget(graph).setPropertyValue("axis_2_auto_scale", "0")
        display.getWidget(graph).setPropertyValue("axis_3_auto_scale", "0")

        # Set the max and min values of the y-axis
        display.getWidget(graph).setPropertyValue("axis_1_maximum", one + offset1)
        display.getWidget(graph).setPropertyValue("axis_1_minimum", one - offset1)
        display.getWidget(graph).setPropertyValue("axis_2_maximum", two + offset2)
        display.getWidget(graph).setPropertyValue("axis_2_minimum", two - offset2)
        display.getWidget(graph).setPropertyValue("axis_3_maximum", three + offset3)
        display.getWidget(graph).setPropertyValue("axis_3_minimum", three - offset3)
            
        # Reset the rescale action indicator to 0
        pvs[0].setValue(0)

if __name__ == '__main__':
    main()

