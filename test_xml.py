# http://lxml.de/tutorial.html
# http://effbot.org/zone/element-index.htm

# import xml.etree.cElementTree as ET
from lxml import etree

root = etree.Element("dataset")
doc = etree.SubElement(root, "images")

image = etree.SubElement(doc, "image", file="datasets/verslo32/2016.01.14/16_05_53_158_2_0_HBN788_.jpg")
box = etree.SubElement(image, "box", top="624", left='136', width='85', height='32')
box = etree.SubElement(image, "box", top="624", left='136', width='85', height='32')

# etree.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = etree.ElementTree(root)
tree.write("filename.xml", pretty_print=True)


# <?xml version='1.0' encoding='ISO-8859-1'?>
# <?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>
# <dataset>
# <name>imglab dataset</name>
# <comment>Created by imglab tool.</comment>
# <image file='datasets/verslo32/2016.01.14/16_05_53_158_2_0_HBN788_.jpg'>
#   <box top='624' left='136' width='85' height='32'/>
#   <box top='675' left='698' width='96' height='36'/>
#   <box top='639' left='1024' width='73' height='28'/>
# </image>