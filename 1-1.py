import xml.etree.ElementTree as ET

# XMLファイルを読み込む
tree = ET.parse("/home/kotoriyabe/esmini-1/resources/esmini-sim/1-2.xosc")
root = tree.getroot()

# ＝＝＝A'未達＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

# (1)
# v0_e = 15  # Egoの初速　単位はm/s
# x_e = 0  # Egoの初期位置
# v0_p = 1  # 歩行者の速度　単位はm/s
# x_p = 80  # 歩行者の初期位置

# (2)
v0_e = 30  # Egoの初速　単位はm/s
x_e = 0  # Egoの初期位置
v0_p = 1  # 歩行者の速度　単位はm/s
x_p = 80  # 歩行者の初期位置

# (3)

# ＝＝＝＝A-B間＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

# (4)

# (5)

# ＝＝＝＝B'到達＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

# (6)

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

a = 0.196  # 減速度
td = 0.7  # 空走時間

Dy = -10  # 歩行者がどれくらい車道から離れているか
Dy_w = abs(Dy - 3)  # 歩行者から見た、車と接触しない奥側の位置
Dx = x_p - x_e  # Egoと歩行者の位置


timeflag = 100
print("tp", tp)
print("tv", tv)
print("s", s)
print("Dx", Dx)


if Dy < 1:  # (1〜2)
    if (tp > tv) and (s > Dx):  # （2）
        timeflag = td
        for elem in root.iter("ParameterDeclaration"):
            if elem.attrib["name"] == "timeflag":
                elem.set("value", str(timeflag))
            elif elem.attrib["name"] == "v0_e":
                elem.set("value", str(v0_e))
            elif elem.attrib["name"] == "EgoS":
                elem.set("value", str(x_e))
            elif elem.attrib["name"] == "v0_p":
                elem.set("value", str(v0_p))
            elif elem.attrib["name"] == "PedestrianS":
                elem.set("value", str(x_p))
            elif elem.attrib["name"] == "Dy":
                elem.set("value", str(Dy))
    elif tp > tv:  # (1)
        for elem in root.iter("ParameterDeclaration"):
            if elem.attrib["name"] == "timeflag":
                elem.set("value", str(timeflag))
            elif elem.attrib["name"] == "v0_e":
                elem.set("value", str(v0_e))
            elif elem.attrib["name"] == "EgoS":
                elem.set("value", str(x_e))
            elif elem.attrib["name"] == "v0_p":
                elem.set("value", str(v0_p))
            elif elem.attrib["name"] == "PedestrianS":
                elem.set("value", str(x_p))
            elif elem.attrib["name"] == "Dy":
                elem.set("value", str(Dy))
    else:
        pass
elif (Dy >= 1) and (Dy < 3):  # (4)
    pass
else:  # （5〜6）
    if v0_e > Dx / Dy * v0_p:  # (5)
        pass
    elif v0_e > Dx / Dy * v0_p:  # (6)
        pass

# for elem in root.iter("ParameterDeclaration"):
#     if elem.attrib["name"] == "timeflag":
#         elem.set("value", str(timeflag))
#     elif elem.attrib["name"] == "v0_e":
#         elem.set("value", str(v0_e))
#     elif elem.attrib["name"] == "EgoS":
#         elem.set("value", str(x_e))
#     elif elem.attrib["name"] == "v0_p":
#         elem.set("value", str(v0_p))
#     elif elem.attrib["name"] == "PedestrianS":
#         elem.set("value", str(x_p))
#     elif elem.attrib["name"] == "Dy":
#         elem.set("value", str(Dy))
# 変更をXMLファイルに保存する
# tree.write("resources/esmini-sim/1-3.xosc")
tree.write("/home/kotoriyabe/esmini-1/resources/esmini-sim/1-3.xosc")
