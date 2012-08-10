from org.csstudio.opibuilder.scriptUtil import PVUtil

#PVs
# pvs[0] = loc://rescale
# pvs[1] = $(TS)LLRF4:STATS0:S$(CAV)_mean_ampl
# pvs[2] = $(TS)LLRF4:STATS0:S$(FWD)_mean_ampl
# pvs[3] = $(TS)LLRF4:STATS0:S$(REV)_mean_ampl
# pvs[4] = $(TS)LLRF4:STATS0:S$(REF)_mean_ampl
# pvs[5] = $(TS)LLRF4:STATS0:S$(CAV)_mean_phase
# pvs[6] = $(TS)LLRF4:STATS0:S$(FWD)_mean_phase
# pvs[7] = $(TS)LLRF4:STATS0:S$(REV)_mean_phase
# pvs[8] = $(TS)LLRF4:STATS0:S$(REF)_mean_phase
# pvs[9] = loc://offset1
# pvs[10] = loc://offset2
# pvs[11] = loc://offset3
# pvs[12] = loc://offset4

def main():
    # CAV/FWD Ampl
    if PVUtil.getLong(pvs[0]) == 1:
        axis = "1"
        graph = "TopGraph"
        chann1 = PVUtil.getDouble(pvs[1])
        chann2 = PVUtil.getDouble(pvs[2])
        offset = PVUtil.getDouble(pvs[9])
    
    # REV/REF Ampl
    if PVUtil.getLong(pvs[0]) == 2:
        axis = "2"
        graph = "TopGraph"
        chann1 = PVUtil.getDouble(pvs[3])
        chann2 = PVUtil.getDouble(pvs[4])
        offset = PVUtil.getDouble(pvs[10])
        
    # CAV/FWD Phase
    if PVUtil.getLong(pvs[0]) == 3:
        axis = "1"
        graph = "BottomGraph"
        chann1 = PVUtil.getDouble(pvs[5])
        chann2 = PVUtil.getDouble(pvs[6])
        offset = PVUtil.getDouble(pvs[11])
        
    # REF/REF Phase
    if PVUtil.getLong(pvs[0]) == 4:
        axis = "2"
        graph = "BottomGraph"
        chann1 = PVUtil.getDouble(pvs[7])
        chann2 = PVUtil.getDouble(pvs[8])
        offset = PVUtil.getDouble(pvs[12])
    
    if PVUtil.getLong(pvs[0]) != 0:
        # Get the graph widget and turn off autoscale
        display.getWidget(graph).setPropertyValue("axis_" + axis + "_auto_scale", "0")
            
        # Get the larger and smaller of the two current values
        if (chann1 > chann2):
            max = str(chann1 + offset)
            min = str(chann2 - offset)
        else:
            max = str(chann2 + offset)
            min = str(chann1 - offset)
            
        # Set the max and min values of the y-axis
        display.getWidget(graph).setPropertyValue("axis_" + axis + "_maximum", max)
        display.getWidget(graph).setPropertyValue("axis_" + axis + "_minimum", min)
            
        # Reset the rescale action indicator to 0
        pvs[0].setValue(0)

if __name__ == '__main__':
    main()
