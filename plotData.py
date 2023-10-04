import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root

def plot_data(data_points, title):
    x_values = [int(data_point.attrib['x']) for data_point in data_points]
    y_values = [float(data_point.attrib['y']) for data_point in data_points]
    plt.plot(x_values, y_values, label=title)

def main():
    xml_file = "list_perf.xml"
    root = parse_xml(xml_file)
    
    plt.figure(figsize=(10, 6))
    plt.title(root.attrib['title'])
    plt.xlabel(root.find(".//XAxis").text)
    plt.ylabel(root.find(".//YAxis").text)
    
    sequences = root.findall(".//Sequence")
    for sequence in sequences:
        title = sequence.attrib['title']
        data_points = sequence.findall(".//DataPoint")
        plot_data(data_points, title)
    
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
