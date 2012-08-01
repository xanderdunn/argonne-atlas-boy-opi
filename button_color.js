importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var GREEN = ColorFontUtil.getColorFromRGB(0,255,0);

// Reset all buttons to default
//display.getWidget("actionBtn1").setPropertyValue("background_color",DEFAULT,true);
//display.getWidget("actionBtn2").setPropertyValue("background_color",DEFAULT,true);
//display.getWidget("actionBtn3").setPropertyValue("background_color",DEFAULT,true);
//display.getWidget("actionBtn4").setPropertyValue("background_color",DEFAULT,true);

// Set color of clicked button
display.getWidget("CH1").setPropertyValue("background_color",GREEN,true);

// Put other actions to execute here...
//widget.executeAction(0);

// Closest we can get to macro expansion inside scripts?
//var macroValue = widget.getMacroValue("m1"); //get the macro value of "m1"