# Filename: pythonprogchallenge
# Author: Gan Jing Ying
# Created: 20130331
# Modified: 20130401
# Description: Program that extracts all the components in an XML file

# import stuff
from xml.dom import minidom
import json
import re
import urllib.request

# define variables
info = []

# get your files
response = urllib.request.urlopen('http://www.dhs.sg/rss/what%2527s-new%3F-19.xml')
xml = response.read()

# gets all XML as a string
# the "parseString" function will treat the stuff in 'xml' as a string
xml_data = minidom.parseString(xml).getElementsByTagName('channel')

# gets all items
parts = xml_data[0].getElementsByTagName('item')

# loop all items
for part in parts:
    # define dictionary
    group = {}
    # get description
    description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
    description = re.sub("<[^>]*>", "", description)
    description = description[:-10]
    group["description"] = description
    # get link
    link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    group["link"] = link
    # get title
    title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    group["title"] = title
    # add group into info
    info.append(group)

encoded = json.dumps(info, indent=2)
print(encoded)

# write info into JSON document
outfile = open("jsonfile.json", encoding='utf-8', mode='w')
outfile.write(encoded)

outfile.close()
