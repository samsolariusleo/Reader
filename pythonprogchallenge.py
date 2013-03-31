# Filename: pythonprogchallenge
# Author: Gan Jing Ying
# Created: 20130331
# Modified: 20130331
# Description: Program that extracts all the components in an XML file

from xml.dom import minidom

infile = open("file.xml", "r")
xml = infile.read()

print(xml)

infile.close()
