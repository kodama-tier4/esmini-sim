import xml.etree.ElementTree as ET

# XMLファイルを読み込む
tree = ET.parse("resources/esmini-sim/sample.xosc")
root = tree.getroot()

# 特定の変数の内容を書き換える
for elem in root.iter("ParameterDeclaration"):
    if elem.attrib["name"] == "Dx":
        elem.set("value", "30")
    elif elem.attrib["name"] == "Dy":
        elem.set("value", "40")

# 変更をXMLファイルに保存する
tree.write("resources/esmini-sim/ans.xosc")
