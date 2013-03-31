# Filename: pythonprogchallenge
# Author: Gan Jing Ying
# Created: 20130331
# Modified: 20130331
# Description: Program that extracts all the components in an XML file

# import stuff
from xml.dom import minidom
import re

# get your files
infile = open("file.xml", "r")
xml = infile.read()

# gets all XML as a string
# the "parseString" function will treat the stuff in 'xml' as a string
xml_data = minidom.parseString(xml).getElementsByTagName('channel')

# gets all items
parts = xml_data[0].getElementsByTagName('item')

# loop all items
for part in parts:
    # get title
    title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    # get link
    link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    # get description
    description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
    description = re.sub("<[^>]*>", "", description)
    description = description[:-10]
    # display info
    print "\n".join([title, link, description, ""])

infile.close()
