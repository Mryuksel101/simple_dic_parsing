import xml.etree.ElementTree as ET
with open("C:/Users/Mustafa Yüksel/Desktop/simple_dic_parsing/deneme.xml", "r", encoding="utf-8") as file:
    xml_text = file.read()
root = ET.fromstring(xml_text)
simple_dictionary = {}
simple_dictionary["words"] = []
entry_elements = root.findall(".//entry")
"""
orth_element = root.find(".//orth")
pos_element = root.find(".//pos")
simple_dictionary["words"].append({})
simple_dictionary["words"][-1]["word"] = orth_element.text
simple_dictionary["words"][-1]["type"] = pos_element.text
simple_dictionary["words"][-1]["polysemantic"] = pos_element.text
"""
print(entry_elements)