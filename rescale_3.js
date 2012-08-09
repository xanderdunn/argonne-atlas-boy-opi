importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

if (PVUtil.getLong(pvs[0]) == 1) {
	// Get the graph widget and turn off autoscale
	display.getWidget("BottomGraph").setPropertyValue("axis_1_auto_scale", "0");
	
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
	var max = greater + 5 + ''
	var min = lesser - 5 + ''
	
	// Set the max value of the y-axis
	display.getWidget("BottomGraph").setPropertyValue("axis_1_maximum", max);
	
	// Set the min value of the y-axis
	display.getWidget("BottomGraph").setPropertyValue("axis_1_minimum", min);
	
	// Reset the action indicator to 0
	pvs[0].setValue(0);
}