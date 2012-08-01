importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
// Set the color of the button to green
widget.setPropertyValue("background_color","Green");
// Reopen the current opi to change the macro
// Not sure how to use this function.  
// Also, perhaps not a good idea because we will have to have 4 .js files,
//  one for each channel number because we have to set the channel # in function
// openOPI(org.csstudio.opibuilder.editparts.AbstractBaseEditPart widgetController, "utilities.opi", 0, null) 
          Open an OPI.