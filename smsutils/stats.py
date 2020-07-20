import xml.etree.ElementTree as ET
import csv


class Stats:
    def __init__(self, input_filename):
        self.tree = ET.parse(input_filename)
        self.root = self.tree.getroot()

    def contact_stats(self):
        contacts = {}
        for element in self.root:
            if element.get('contact_name') not in contacts:
                contacts[element.get('contact_name')] = 1
            else:
                contacts[element.get('contact_name')] += 1
        return contacts

    def message_count(self, name):
        total = 0
        name_count = 0
        for element in self.root:
            total += 1
            if element.get('contact_name') == name:
                name_count += 1
                # print(element.get('body'))
        print(str(name_count) + "/" + str(total))
