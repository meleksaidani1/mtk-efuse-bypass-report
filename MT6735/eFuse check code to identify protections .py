import xml.etree.ElementTree as ET

def analyze_efuse_config(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    print("Analyzing eFuse settings...")
    for setting in root.findall(".//inner_value"):
        tag = setting.get('tag')
        attribute = setting.get('attribute')
        print(f"Found inner value: {tag} - {attribute}")

    for setting in root.findall(".//boolean"):
        tag = setting.get('tag')
        attribute = setting.get('attribute')
        print(f"Found boolean setting: {tag} - {attribute}")

analyze_efuse_config('efuse_definition.xml')
