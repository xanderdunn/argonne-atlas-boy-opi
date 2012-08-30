from org.csstudio.opibuilder.scriptUtil import PVUtil, FileUtil
from java.lang import System

# This Python script finds the absolute path of the atlas_opi project
#   folder and sets it as the Java system property "atlas_opi.dir"

sysPath = FileUtil.workspacePathToSysPath("/atlas_opi")
System.setProperty("atlas_opi.dir", sysPath)
