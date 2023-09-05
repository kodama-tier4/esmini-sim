import xml.etree.ElementTree as ET
import math

# XMLファイルを読み込む
tree = ET.parse("resources/esmini-sim/1-2.xosc")
root = tree.getroot()

v0_e = 15  # Egoの初速　単位はm/s
x_e = 0  # Egoの初期位置
v0_p = 10  # 歩行者の速度　単位はm/s
x_p = 80  # 歩行者の初期位置

a = 0.196  # 減速度
td = 0.7  # 空走時間

Dy = -10  # 歩行者がどれくらい車道から離れているか
Dy_w = abs(-Dy - 2)  # 歩行者から見た、車と接触しない奥側の位置
Dx = x_p - x_e  # Egoと歩行者の位置

tp = Dy / v0_p  # 歩行者が車道に到達する時間
tv = (
    v0_e / a + td - math.sqrt((v0_e / a + td) ^ 2 - 2 * (Dx / a + td ^ 2 / 2))
)  # 車両が「減速度 a」、「空走時間 td」で減速してA’-B’で停止する時間
s = v0_e ^ 2 / (2 * a) + v0_e * td  # 停止までの走行距離


if (Dy < 0) and (v0_e > abs(Dx / Dy * v0_p)):  # （１）
    for elem in root.iter("ParameterDeclaration"):
        if elem.attrib["name"] == "v0_e":
            elem.set("value", str(v0_e))
        elif elem.attrib["name"] == "EgoS":
            elem.set("value", str(x_e))
        elif elem.attrib["name"] == "v0_p":
            elem.set("value", str(v0_p))
        elif elem.attrib["name"] == "PedestrianS":
            elem.set("value", str(x_p))
        elif elem.attrib["name"] == "Dy":
            elem.set("value", str(Dy))
elif (tp > tv) and (s > Dx):  # （２）
    pass
elif v0_e > Dx / Dy * v0_p:  # （３）
    pass
elif v0_e > Dx / Dy * v0_p:  # （４）
    pass
elif v0_e > Dx / Dy * v0_p:  # （５）
    pass


# 特定の変数の内容を書き換える
for elem in root.iter("ParameterDeclaration"):
    if elem.attrib["name"] == "v0_e":
        elem.set("value", str(v0_e))
    elif elem.attrib["name"] == "EgoS":
        elem.set("value", str(x_e))
    elif elem.attrib["name"] == "v0_p":
        elem.set("value", str(v0_p))
    elif elem.attrib["name"] == "PedestrianS":
        elem.set("value", str(x_p))
# 変更をXMLファイルに保存する
tree.write("resources/esmini-sim/1-3.xosc")
