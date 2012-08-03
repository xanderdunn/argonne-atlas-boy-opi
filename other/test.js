importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

// Useful functions.  Might need in future.

// Get a PV value as a string
var chann = PVUtil.getString(pvs[0]); //get the PV value

// Get a macro value
var ts = widget.getMacroValue("TS"); //get the macro value of "TS"

// 

// 
display.getWidget("TopGraph").setPropertyValue("trace_0_y_pv", ts + "LLRF4:STATS0:S" + chann + "_mean_ampl");