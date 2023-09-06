import xml.etree.ElementTree as ET

v0 = 10  # Egoの初速　単位はm/s
vp = 50  # 歩行者の速度　単位はm/s
Dy = 10  # 歩行者がどれくらい車道から離れているか
Dy_w = -Dy - 2


# XMLファイルを読み込む
tree = ET.parse("/home/hideakikodama/esmini/resources/tier4/1-2.xosc")
root = tree.getroot()
