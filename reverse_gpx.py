import xml.etree.ElementTree as ET

# Load the GPX file
tree = ET.parse('route_original.gpx')
root = tree.getroot()

# Define the namespace
namespace = {'default': 'http://www.topografix.com/GPX/1/1'}

# Find the trkseg element
trkseg = root.find('.//default:trkseg', namespaces=namespace)

# Reverse the order of its child nodes
if trkseg is not None:
    trkseg[:] = sorted(trkseg, key=lambda x: x.find('default:time', namespaces=namespace).text)
    trkseg[:] = trkseg[::-1]

# Remove the namespace prefix from the tags
for elem in root.iter():
    if elem.tag.startswith('{'):
        elem.tag = elem.tag.split('}', 1)[1]

# Save the modified XML back to the file
tree.write('route_result.gpx', encoding='utf-8', xml_declaration=True)