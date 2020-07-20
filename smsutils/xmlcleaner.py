import xml.etree.ElementTree as ET

# Removes non SMS elements from the XML tree
# For some reason, it doesn't work in a single pass
# hence the while loop...
def remove_non_sms(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    mmsCount = 1
    while mmsCount > 0:
        mmsCount = 0
        for element in root:
            if element.tag != "sms":
                root.remove(element)
        for element in root:
            if element.tag != "sms":
                mmsCount += 1
    tree.write(output_file)