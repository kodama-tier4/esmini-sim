import xml.etree.ElementTree as ET

v0 = 10  # Egoの初速　単位はm/s
vp = 50  # 歩行者の速度　単位はm/s
Sx_p = 0  # 歩行者の初速
Dy = 10
B2y = Dy - 2


# XMLファイルを読み込む
tree = ET.parse("/home/hideakikodama/esmini/resources/tier4/1-1.xosc")
root = tree.getroot()
