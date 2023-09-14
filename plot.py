import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# XMLデータを解析
tree = ET.parse("resources/esmini-sim/dcase.xosc")
root = tree.getroot()

# EgoSpeedの値を取得
ego_speed = root.find(".//ParameterDeclaration[@name='EgoSpeed']").get("value")

# グラフを描画
times = list(range(0, 11))  # 例: 0秒から10秒まで
speeds = [float(ego_speed)] * len(times)

plt.plot(times, speeds, label="Ego Speed", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Speed")
plt.title("Ego Speed Over Time")
plt.legend()
plt.show()
