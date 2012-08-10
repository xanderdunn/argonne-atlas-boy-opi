importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

// pvs[0] = loc://rescale1
// pvs[1] = $(TS)LLRF4:STATS0:S$(CAV)_mean_ampl
// pvs[2] = $(TS)LLRF4:STATS0:S$(FWD)_mean_ampl
// pvs[3] = loc://offset1

if (PVUtil.getLong(pvs[0]) == 1) {

	// Get the desired offset value
	var offset = PVUtil.getDouble(pvs[3])

	// Get the graph widget and turn off autoscale
	display.getWidget("TopGraph").setPropertyValue("axis_1_auto_scale", "0");
	
	// Get the current values as doubles
	var cav = PVUtil.getDouble(pvs[1])
	var fwd = PVUtil.getDouble(pvs[2])
	
	// Get the larger and smaller of the two current values
	if (cav > fwd) 
		{
		var greater = cav
		var lesser = fwd
		}
	else 
		{
		var greater = fwd
		var lesser = cav
		}
	
	// Do math and convert to string
	var max = greater + offset + ''
	var min = lesser - offset + ''
	
	// Set the max value of the y-axis
	display.getWidget("TopGraph").setPropertyValue("axis_1_maximum", max);
	
	// Set the min value of the y-axis
	display.getWidget("TopGraph").setPropertyValue("axis_1_minimum", min);
	
	// Reset the action indicator to 0
	pvs[0].setValue(0);
}