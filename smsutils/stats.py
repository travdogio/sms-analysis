import xml.etree.ElementTree as ET


class Stats:
    def __init__(self, input_filename):
        self.tree = ET.parse(input_filename)
        self.root = self.tree.getroot()

    def message_count(self, name):
        total = 0
        name_count = 0
        for element in self.root:
            total += 1
            if element.get('contact_name') == name:
                name_count += 1
                # print(element.get('body'))
        print(str(name_count) + "/" + str(total))
