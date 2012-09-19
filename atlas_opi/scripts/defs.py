#!/bin/python

# Description: get common directories and set them as system macros

from org.csstudio.opibuilder.scriptUtil import PVUtil # CSS BOY tools
from java.lang import System # for getting Java environment variables
import os # for getting os environment variables
import string # rem()

def main():
    # Set Directories
    # ====================================

    # Get the absolute path of the css binary
    css_dir_var = System.getProperty("osgi.install.area")
    css_dir = css_dir_var.split(":")[1]
    System.setProperty("css.dir", css_dir)
    print "CSS binary dir:", css_dir

    # Define the medm directory
    medm_dir= os.path.normpath(os.path.join(css_dir, "../../medm/"))
    System.setProperty("medm.dir", medm_dir)
    print "MEDM dir:", medm_dir

    # Define the caxgui directory
    caxgui_dir = os.path.normpath(os.path.join(css_dir, "../../caXGUI/"))
    System.setProperty("caxgui.dir", caxgui_dir)

    # Define the epics host architecture
    host_arch = os.environ['EPICS_HOST_ARCH']
    System.setProperty("host.arch", host_arch)
    print "Host arch:", host_arch

    # Define the full caxgui directory
    full_caxgui = caxgui_dir + "/bin/" + host_arch + "/"
    System.setProperty("caxgui.full.dir", full_caxgui)
    print "Full caxgui dir:", full_caxgui

    # Define the location of the workspace
    workspace_dir_var = System.getProperty("osgi.instance.area")
    workspace_dir = workspace_dir_var.split(":")[1]
    System.setProperty("user.workspace", workspace_dir)
    print "User workspace:", workspace_dir

    # Set Macros
    # ====================================
    ts = display.getMacroValue("TS")
    System.setProperty("macro.ts", ts)
    llrf = display.getMacroValue("LLRF")
    System.setProperty("macro.llrf", llrf)

if __name__ == '__main__':
    main()

# Remove new line characters
def rem(str0):
    return string.replace(str0, "\n", "")

# Code to run as import module:
css_dir = System.getProperty("css.dir")
medm_dir = System.getProperty("medm.dir")
caxgui_dir = System.getProperty("caxgui.dir")
workspace_dir = System.getProperty("user.workspace")
ts = System.getProperty("macro.ts")
llrf = System.getProperty("macro.llrf")
