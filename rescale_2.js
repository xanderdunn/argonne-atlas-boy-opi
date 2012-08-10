importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

// pvs[0] = loc://rescale2
// pvs[1] = $(TS)LLRF4:STATS0:S$(REV)_mean_ampl
// pvs[2] = $(TS)LLRF4:STATS0:S$(REF)_mean_ampl
// pvs[3] = loc://offset2

if (PVUtil.getLong(pvs[0]) == 1) {
	
	var offset = PVUtil.getDouble(pvs[3])
	
	// Get the graph widget and turn off autoscale
	display.getWidget("TopGraph").setPropertyValue("axis_2_auto_scale", "0");
	
	// Get the current values as doubles
	var rev = PVUtil.getDouble(pvs[1])
	var ref = PVUtil.getDouble(pvs[2])
	
	// Get the larger and smaller of the two current values
	if (rev > ref) 
		{
		var greater = rev
		var lesser = ref
		}
	else 
		{
		var greater = ref
		var lesser = rev
		}
	
	// Do math and convert to string
	var max = greater + offset + ''
	var min = lesser - offset + ''
	
	// Set the max value of the y-axis
	display.getWidget("TopGraph").setPropertyValue("axis_2_maximum", max);
	
	// Set the min value of the y-axis
	display.getWidget("TopGraph").setPropertyValue("axis_2_minimum", min);
	
	// Reset the action indicator to 0
	pvs[0].setValue(0);
}