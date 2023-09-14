import xml.etree.ElementTree as ET
import math

# XMLファイルを読み込む
# tree = ET.parse("resources/esmini-sim/1-2.xosc")
tree = ET.parse("/home/kotoriyabe/esmini-1/resources/esmini-sim/1-2.xosc")

root = tree.getroot()

v0_e = 5  # Egoの初速　単位はm/s
x_e = 0  # Egoの初期位置
v0_p = 1  # 歩行者の速度　単位はm/s
x_p = 30  # 歩行者の初期位置

a = 2.5  # 減速度　単位はm/s^2 0.196?
td = 0.7  # 空走時間

Dy = -10  # 歩行者がどれくらい車道から離れているか
Dy_w = abs(Dy - 3)  # 歩行者から見た、車と接触しない奥側の位置
Dx = x_p - x_e  # Egoと歩行者の距離

tp = abs(Dy / v0_p)  # 歩行者が車道に到達する時間
tv = v0_e / a
# tv = (
#     v0_e / a + td - math.sqrt((v0_e / a + td) ** 2 - 2 * (Dx / a + td**2 / 2))
# )  # 車両が「減速度 a」、「空走時間 td」で減速してA’-B’で停止する時間
s = v0_e * (tv + v0_e / a) / 2  # 停止までの走行距離










timeflag1 = 100
timeflag2 = 100
print("歩行者が車道に到達する時間：tp", tp)
print("車両が「減速度 a」、「空走時間 td」で減速してA’-B’で停止する時間：tv", tv)
print("停止までの走行距離：s", s)
print("Egoと歩行者の距離：Dx", Dx)

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



if Dy < 1:  # (1〜3)
    if (tp > tv) and (s > Dx):  # （2）
        print("(2)を実施")
        timeflag2 = td
        for elem in root.iter("ParameterDeclaration"):
            if elem.attrib["name"] == "timeflag2":
                elem.set("value", str(timeflag2))
            elif elem.attrib["name"] == "DistanceToStop":
                elem.set("value", str(s))  # 止まるまでの距離
            # elif elem.attrib["name"] == "PedestrianS":
            #     elem.set("value", str(x_p))
            # elif elem.attrib["name"] == "v0_e":
            #     elem.set("value", str(v0_e))
            # elif elem.attrib["name"] == "EgoS":
            #     elem.set("value", str(x_e))
            # elif elem.attrib["name"] == "v0_p":
            #     elem.set("value", str(v0_p))
            # elif elem.attrib["name"] == "Dy":
            #     elem.set("value", str(Dy))
    
    elif tp > tv:  # (1)
        print("(1)を実施")
        # for elem in root.iter("ParameterDeclaration"):
            # if elem.attrib["name"] == "v0_e":
            #     elem.set("value", str(v0_e))
            # elif elem.attrib["name"] == "EgoS":
            #     elem.set("value", str(x_e))
            # elif elem.attrib["name"] == "v0_p":
            #     elem.set("value", str(v0_p))
            # elif elem.attrib["name"] == "PedestrianS":
            #     elem.set("value", str(x_p))
            # elif elem.attrib["name"] == "Dy":
            #     elem.set("value", str(Dy))


    else:  # (3)
        print("(3)を実施")
        timeflag1 = td
        for elem in root.iter("ParameterDeclaration"):
            if elem.attrib["name"] == "timeflag1":
                elem.set("value", str(timeflag1))                
            elif elem.attrib["name"] == "TimeToStop":
                elem.set("value", str(tv))  # 止まるまでの時間  

            # elif elem.attrib["name"] == "v0_e":
            #     elem.set("value", str(v0_e))
            # elif elem.attrib["name"] == "EgoS":
            #     elem.set("value", str(x_e))
            # elif elem.attrib["name"] == "v0_p":
            #     elem.set("value", str(v0_p))
            # elif elem.attrib["name"] == "PedestrianS":
            #     elem.set("value", str(x_p))
            # elif elem.attrib["name"] == "Dy":
            #     elem.set("value", str(Dy))


elif (Dy >= 1) and (Dy <= 4):  # (4)
    print("(4)を実施")
    timeflag1 = td
    for elem in root.iter("ParameterDeclaration"):
        if elem.attrib["name"] == "timeflag1":
            elem.set("value", str(timeflag1))
        elif elem.attrib["name"] == "TimeToStop":
            elem.set("value", str(tv))  # 止まるまでの時間
        # elif elem.attrib["name"] == "v0_e":
        #     elem.set("value", str(v0_e))
        # elif elem.attrib["name"] == "EgoS":
        #     elem.set("value", str(x_e))
        # elif elem.attrib["name"] == "v0_p":
        #     elem.set("value", str(v0_p))
        # elif elem.attrib["name"] == "PedestrianS":
        #     elem.set("value", str(x_p))
        # elif elem.attrib["name"] == "Dy":
        #     elem.set("value", str(Dy))

else:  # （5〜6）
    if (Dy > 4) and (Dy <= 6):  # (5)
        print("(5)を実施")
        timeflag2 = td
        for elem in root.iter("ParameterDeclaration"):
            if elem.attrib["name"] == "timeflag2":
                elem.set("value", str(timeflag2))
            elif elem.attrib["name"] == "DistanceToStop":
                elem.set("value", str(s))  # 止まるまでの距離
            # elif elem.attrib["name"] == "v0_e":
            #     elem.set("value", str(v0_e))
            # elif elem.attrib["name"] == "EgoS":
            #     elem.set("value", str(x_e))
            # elif elem.attrib["name"] == "v0_p":
            #     elem.set("value", str(v0_p))
            # elif elem.attrib["name"] == "PedestrianS":
            #     elem.set("value", str(x_p))
            # elif elem.attrib["name"] == "Dy":
            #     elem.set("value", str(Dy))

    else:  # (6)
        print("(6)を実施")
        # for elem in root.iter("ParameterDeclaration"):
        #     if elem.attrib["name"] == "v0_e":
        #         elem.set("value", str(v0_e))
        #     elif elem.attrib["name"] == "EgoS":
        #         elem.set("value", str(x_e))
        #     elif elem.attrib["name"] == "v0_p":
        #         elem.set("value", str(v0_p))
        #     elif elem.attrib["name"] == "PedestrianS":
        #         elem.set("value", str(x_p))
        #     elif elem.attrib["name"] == "Dy":
        #         elem.set("value", str(Dy))

# tree.write("resources/esmini-sim/1-3.xosc")
tree.write("/home/kotoriyabe/esmini-1/resources/esmini-sim/1-3.xosc")
