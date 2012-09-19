#!/bin/python

# Description: get the directory of the css binary and set it as a system var

from java.lang import System # Get Java environment variables
import os # get environment variable

# Get the absolute path of the css binary
css_dir_var = System.getProperty("osgi.install.area")
css_dir = css_dir_var.split(":")[1]
System.setProperty("css.dir", css_dir)

# Define the medm directory
medm_dir= os.path.normpath(os.path.join(css_dir, "../../medm/"))
System.setProperty("medm.dir", medm_dir)

# Define the caxgui directory
caxgui_dir = os.path.normpath(os.path.join(css_dir, "../../caXGUI/"))
System.setProperty("caxgui.dir", caxgui_dir)

host_arch = os.environ['EPICS_HOST_ARCH']
System.setProperty("host.arch", host_arch)

System.setProperty("caxgui.full.dir", caxgui_dir + "/bin/" + host_arch + "/")